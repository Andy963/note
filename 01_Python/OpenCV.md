
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