
### 读取图像

cv2.IMREAD_COLOR 彩色图像

cv2.IMREAD_GRAYSCALE  灰度图像

```python
img = cv2.imread('cat.jpg')  
img

  [169, 174, 172],
	[170, 175, 173],
	[170, 175, 173]],

   [[195, 201, 196],
	[197, 203, 198],
	[188, 194, 189],
	...,
	[171, 176, 174],
	[172, 177, 175],
	[172, 177, 175]]], dtype=uint8)
```


```python
cv2.imshow('image',img)  
# 等待时间，毫秒级，0表示任意键终止  
cv2.waitKey(1000)  
cv2.destroyAllWindows() 
```


### 图像平滑

```python
cat = cv2.imread('cat.jpg')

# 均值滤波
blur = cv2.blur(cat,(3,3))
cv_show(blur)

# 方框
# 可以选择归一化，容易越界, normalize = False 时，只要越界了，就取255
box = cv2.boxFilter(cat,-1,(3,3),normalize=False)
cv_show(box)

# 高斯滤波
gaussian = cv2.GaussianBlur(cat,(3,3),0)
cv_show(gaussian)

# 中值滤波
median = cv2.medianBlur(cat,3)
cv_show(median)

# 双边滤波
bilateral = cv2.bilateralFilter(cat,9,75,75)
cv_show(bilateral)
```

### 腐蚀操作

```python
dg = cv2.imread('dige.jpg')  
cv_show(dg)  

kernel = np.ones((3,3),np.uint8)  
erosion = cv2.erode(dg,kernel,iterations = 2)  
cv_show(erosion)
```

### 膨胀操作

```python
kernel = np.ones((3,3),np.uint8)  
dilation = cv2.dilate(dg,kernel,iterations = 1)  
cv_show(dilation)
```


### 开运算与闭运算

```python
# 开运算：先腐蚀再膨胀  
img = cv2.imread('dige.jpg')  
  
kernel = np.ones((3,3),np.uint8)  
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)  
cv_show(opening)


# 闭运算：先膨胀再腐蚀  
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)  
cv_show(closing)
```


### 梯度计算

```python
# 梯度：膨胀-腐蚀  
pie = cv2.imread('pie.jpg')  
  
kernel = np.ones((7,7),np.uint8)  
dilate = cv2.dilate(pie,kernel,iterations = 1)  
erosion = cv2.erode(pie,kernel,iterations = 1)  
res = np.hstack((dilate, erosion))  
cv_show(res)  
  
# 内置方法实现  
# gradient = cv2.morphologyEx(pie, cv2.MORPH_GRADIENT, kernel)  
# cv_show(gradient)
```

📚 梯度的作用
1. 边缘检测：膨胀和腐蚀生成的梯度图像通常能更有效地突出边缘和轮廓，有助于后续的边缘检测，比如使用Canny边缘检测等方法。
2. 特征提取：在图像处理中，梯度可以帮助提取图像中的重要特征，这些特征可以被用于物体识别、跟踪和分类任务。
3. 形态学操作的应用：通过形态学梯度，能够分析物体的形状和结构，适用于分割和检测。

📚 应用场景
1. 医学图像处理：可以用来检测并提取血管、肿瘤等医学影像中的边缘特征。
2. 目标检测：在监控视频流中，通过提取物体的边缘特征，进行运动检测和目标识别。
3. 形状分析：用于自动计数颗粒或细胞，以及其他形状分析任务。
4. 焊接图像分析：用于检测焊接缝的质量，分析焊缝的边缘特征


### 黑帽 礼帽

📚 黑帽操作（Black Hat Transform）

定义：
黑帽操作是通过从原始图像中减去开运算结果来实现的：

作用：
1. 提取暗区特征：突出那些比周围亮背景暗的结构，例如图像中的小孔、缺陷等。
2. 强调细节：有效提取细小的特征，尤其是在高对比度的图像背景下。

应用场景：
⦁ 缺陷检测：在工业检测中突出亮背景下的暗缺陷，如裂缝、凹坑等。
⦁ 医学图像：识别暗区病变或异常，帮助医生进行诊断。
⦁ 文档分析：从亮色背景中提取暗文字或图形。

📚 礼帽操作（White Hat Transform）

定义：
礼帽操作是通过从闭运算（Closing）中减去原始图像的结果来实现的：

作用：
1. 提取亮区特征：突出那些比周围暗背景亮的结构，例如图像中的小高光、亮斑等。
2. 强调整体形状：帮助识别物体的边界和轮廓。

应用场景：
⦁ 目标检测：在复杂背景下，可以用来增强检测亮区物体或特征。
⦁ 医学影像：帮助识别亮斑或高反差区域，例如在X光图像中突出某些特征。
⦁ 文档处理：从深色背景中提取亮文字或形状，助于OCR（光学字符识别）等处理。

```python
# 礼帽：原始输入 - 开运算  
img = cv2.imread('dige.jpg')  
kernel = np.ones((5,5),np.uint8)  
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)  
cv_show(top_hat)

# 黑帽：闭运算 - 原始输入  
img = cv2.imread('dige.jpg')  
kernel = np.ones((5,5),np.uint8)  
black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)  
cv_show(black_hat)
```

### 梯度 sobel 算子

```python
img = cv2.imread('pie.jpg',cv2.IMREAD_GRAYSCALE)  
  
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  
cv_show(sobelx)

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  
cv_show(sobely)

# 分别求x,y,再求和  
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)  
  
cv_show(sobelxy)


# 内置方法  不建议直接使用内置方法  
sobelxy = cv2.Sobel(img, cv2.CV_64F,1,1,ksize=3)  
sobelxy = cv2.convertScaleAbs(sobelxy)  
cv_show(sobelxy)
```

### Canny 边缘检测

1. 高斯滤波器，平滑图像，去除噪声
2. 计算梯度强度和方向
3. 使用非极大值抑制,消除边缘检测带来的杂散响应
4. 应用双阈值检测确定真实的和潜在的边缘
5. 抑制孤立的弱边缘，完成边缘检测


### 金字塔制造方法

高斯金字塔（Gaussian Pyramid）：
通过对原始图像进行逐层模糊和下采样（通常是以2的倍数减少图像的尺寸），生成一系列低分辨率版本的图像。每一层都比上一层更加模糊且尺寸更小

```python
img = cv2.imread('cat.jpg')

up = cv2.pyrUp(img)
down = cv2.pyrDown(img)

up_down = cv2.pyrDown(up)
cv_show(up_down) # 每次都损失了部分数据会变模糊
```

拉普拉斯金字塔（Laplacian Pyramid）：

通过从高斯金字塔的每一层生成差异图像，得到的金字塔。 提取了图像的细节和边缘信息，从而能够在图像重构和图像增强等任务中提供帮助

```python
img = cv2.imread('cat.jpg')
down = cv2.pyrDown(img)
down_up = cv2.pyrUp(down,dstsize=(img.shape[1], img.shape[0]))
rs = img - down_up
cv_show(rs)

# laplacian = cv2.subtract(img, down_up)
```

### 轮廓检测

findContours(img, mode, method)

mode：轮廓检索模式
·RETR_EXTERNAL：只检索最外面的轮廓；
·RETR_LIST：检索所有的轮廓，并将其保存到一条链表当中；
·RETR_CCOMP：检索所有的轮廓，并将他们组织为两层：顶层是各部分的外部边界，第二层是空洞的边界；
·RETR_TREE：检索所有的轮廓，并重构嵌套轮廓的整个层次；

method：轮廓逼近方法
·CHAIN_APPROX_NONE：以Freeman链码的方式输出轮廓，所有其他方法输出多边形（顶点的序列）。
·CHAIN_APPROX_SIMPLE：压缩水平的、垂直的和斜的部分，也就是，函数只保留他们的终点部分。

```python
img = cv2.imread('cat.jpg')
# 转灰度图
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 二值处理
ret, threshold = cv2.threshold(gray, 127,255, cv2.THRESH_BINARY)

cv_show(threshold)

contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
```

轮廓绘制：

```python
# 注意会直接修改原始图片所以copy一下
img_copy = img.copy()
# -1 表示 全部的轮廓
# (0,0,255) 表示 bgr 中的r
# 2 表示宽度
res = cv2.drawContours(img_copy, contours, -1, (0,0,255),2)
cv_show(res)
```

轮廓特征:

面积：
```python
cnt = contours[0]
cv2.contourArea(cnt)
```

周长：

```python
# 周长
cv2.arcLength(cnt,True) # true表示 “闭合” 的轮廓
```

#### 边界矩形

```python
cnt = contours[1]
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv_show(img)
```

#### 外接圆

```python
(x,y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cr = cv2.circle(img,center,radius,(0,255,9),2)
cv_show(cr)
```

### 模板匹配

TM_SQDIFF：计算平方不同，计算出来的值越小，越相关
TMCCORR：计算相关性，计算出来的值越大，越相关
TM_CCOEFF：计算相关系数，计算出来的值越大，越相关
TM_SQDIFF_NORMED：计算归一化平方不同，计算出来的值越接近O，越相关
TM_CCORR_NORMED：计算归一化相关性，计算出来的值越接近1，越相关
TM_CCOEFF_NORMED：计算归一化相关系数，计算出来的值越接近1，越相关

```python
img = cv2.imread('lina.jpg',0)
#face = cv2.imread('face.jpg',0)

template = cv2.imread('face.jpg',0)
res = cv2.matchTemplate(img, template, 1)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)

# 在匹配位置画矩形
top_left = min_loc  # 对于 TM_SQDIFF_NORMED 方法
bottom_right = (top_left[0] + w, top_left[1] + h)
# 在原图上标注出来
cv2.rectangle(img, top_left,bottom_right, 255, 2)
```

### 直方图
cv2.calcHist:
images:原图像图像格式为uint8或float32。当传入函数时应用中括号[]括来例如[img]
·channels:同样用中括号括来它会告函数我们统幅图像的直方图。如果入图像是灰度图它的值就是[0]如果是彩色图像的传入的参数可以是` [0] [1] [2] `它们分别
对应着BGR。
·mask:掩模图像。统整幅图像的直方图就把它为None。但是如果你想统图像某一分的直方图的你就制作一个掩模图像并使用它。
·histSize:BIN的数目。也应用中括号括来
·ranges:像素值范围常为[0,256]

```python
img = cv2.imread('cat.jpg',0)
his = cv2.calcHist([img],[0],None, [256],[0,256])
his.shape

plt.hist(img.ravel(),256);
plt.show()
```

#### 均衡化

```python
img = cv2.imread('cat.jpg', 0)
plt.hist(img.ravel(), 256)
plt.show()
# 均衡化后的直方图
equ = cv2.equalizeHist(img)
plt.hist(equ.ravel(),256)
plt.show()


# 自适应走廊图均衡化 应用到原图上
clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
res_clahe = clahe.apply(img)
res = np.hstack((img,res_clahe))
cv_show(res)
```

### 傅里叶变换