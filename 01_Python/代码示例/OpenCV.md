### 提取银行卡上的卡号

```python
def cv_show(img,name=None):
    """展示图片"""
    if name is None:
        name = str(name)
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def sort_contours(cnts, method='left-to-right'):
    """根据传入参数的不同，对边界按x或y轴进行排序"""
    reverse = False
    i = 0
    if method == 'right-to-left' or method == "bottom-to-top":
        reverse = True
    if method == 'top-to-bottom' or method == "bottom-to-top":
        i = 1
    # cv2.boundingRect(c) 返回值为 (x, y, width, height)
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    cnts, boundingBoxes = zip(*sorted(zip(cnts, boundingBoxes), key=lambda b: b[1][i], reverse=reverse))
    return cnts, boundingBoxes

template = r'D:\code\langchain\ocr_template_match\template.jpg'
img = cv2.imread(template)

# cv_show(img,'template')

# 灰度图
ref = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv_show(ref,'ref')

# 二值图像
# 小于10的值设置为255,大于10的则设置为0（因为使用的是二值反转inverse）, 返回值为：（阈值, 新的图像）
ref = cv2.threshold(ref, 10, 255, cv2.THRESH_BINARY_INV)[1]
# cv_show(ref,'ref')

# 计算轮廓
# findContours 接受的参数为二值图而非灰度图
# RETR_EXTERNAL 表示只检测外轮廓
# CHAIN_APPROX_SIMPLE 表示只保留终点坐标
# refCnts 表示轮廓的列表，每个值是一个坐标点的numpy数组
# hierarchy 表示轮廓间的关系，包含：1. Next: 下一个轮廓的索引 2. Previous: 上一个轮廓的索引 3. First Child: 第一个子轮廓的索引 4. Parent: 父轮廓的索引
refCnts, hierarchy = cv2.findContours(ref.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# -1 轮廓索引，表示画出所有轮廓
cv2.drawContours(img,refCnts, -1, (0,0,255),2)
# cv_show(img,'img')

# 对轮廓进行排序
refCnts = sort_contours(refCnts,method='left-to-right')[0]

digits = {}
for i, c in enumerate(refCnts):
    (x,y,w,h) = cv2.boundingRect(c)
    # 在原图像中取出对应的区域
    roi = ref[y:y + h, x:x+w]
    roi = cv2.resize(roi,(57,88))
    digits[i] = roi
# print(digits)
# 形态学操作，初始化卷积核
# 长方形卷积核连接较长的物体或消除细小的噪声
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(9,3))
# 正方形卷积核：平滑图像或消除小物体
sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

# 读取图像,预处理
img_file = r'D:\code\langchain\ocr_template_match\1.jpg'
image = cv2.imread(img_file)
# cv_show(image)
# 重新定义一个宽度并计算出对应的高度
width=300
height = int((width / image.shape[1]) * image.shape[0])

# 调整图像大小
# image_resized = cv2.resize(image, (width, height))
# image = resize(image, width=300)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv_show(gray)


# 礼帽操作突出更明亮的区域
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT,rectKernel)
# cv_show(tophat,'tophat')

# ddepthe 表示图像深度32位符点型高精度计算
# dx= 1 表示计算x轴方向梯度 dy=0 表示 不计算y轴方向梯度
# ksize = -1 表示 使用默认的核大小通常是3 * 3
gradX = cv2.Sobel(tophat, ddepth=cv2.CV_32F, dx = 1 ,dy=0, ksize = -1)
# 求绝对值表示不关心方向只关注大小
gradX = np.absolute(gradX)

# 进行归一化处理(0,255)之间
(minVal,maxVal) = (np.min(gradX), np.max(gradX))
gradX = (255 * ((gradX-minVal) / (maxVal -minVal)))
gradX = gradX.astype('uint8')

# print(np.array(gradX).shape)
# cv_show(gradX,'gradx')

# 通过闭操作先膨胀再腐蚀将数字连在一起
gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE,rectKernel)
# cv_show(gradX, 'gradx')

# THRESH_OTSU 自动寻找合适的阈值适合双峰需把阈值参数设置为0
thresh = cv2.threshold(gradX, 0, 255,cv2.THRESH_BINARY|cv2.THRESH_OTSU )[1]
# cv_show(thresh, 'thresh')

thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,sqKernel)
# cv_show(thresh, 'thresh')

# 计算轮廓
threshCnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = threshCnts
cur_img = image.copy()
cv2.drawContours(cur_img, cnts, -1, (0,0,255),3)
# cv_show(cur_img,'cur')

locs = []
# 遍历轮廓
for i,c in enumerate(cnts):
    x,y,w,h = cv2.boundingRect(c)
    ar = w /float(h)
    # print('ar',ar)
    if ar > 1 and ar < 5.0:
        if (w > 40 and w < 70) and (h > 8 and h < 25):
            locs.append((x,y,w,h))
# print('locs',locs)
# 将符合的轮廓从左到右排序 
locs = sorted(locs,key=lambda x:x[0])
# print(locs)
output = []

# 遍历每一个轮廓中的数字
for (i, (gX, gY, gW, gH)) in enumerate(locs):
    groupOutput = []
    group = gray[gY -5:gY+gH+5, gX-5:gX+gW+5]
    # cv_show(group,str(i))
    group = cv2.threshold(group, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # cv_show(group,str(i))
    digitCnts, hierarchy = cv2.findContours(group.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    digitCnts = sort_contours(digitCnts, method='left-to-right')[0]

    for c in digitCnts:
        (x,y,w,h) = cv2.boundingRect(c)
        roi = group[y:y+h, x:x+w]
        roi = cv2.resize(roi,(57,88))
        # cv_show(roi,'roi')
        # 计算得分
        scores = []

        for digit,digitROI in digits.items():
            result = cv2.matchTemplate(roi, digitROI, cv2.TM_CCOEFF)
            _, score, _, _ = cv2.minMaxLoc(result)
            scores.append(score)
        #print(np.argmax(scores))
        groupOutput.append(str(np.argmax(scores)))
        #print(groupOutput)
    cv2.rectangle(image, (gX-5, gY-5), (gX+gW+5, gY+gH+5), (0,0,255),1)
    cv2.putText(image,"".join(groupOutput), (gX, gY-15), cv2.FONT_HERSHEY_SIMPLEX,0.65,(0,0,255),2)
    
    output.extend(groupOutput)
# 打印结果
print("credit card :{}".format("".join(output)))
```