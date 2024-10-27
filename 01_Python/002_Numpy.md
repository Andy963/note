### 创建数组
```python
import numpy as np
arr = np.array([1,2,3])
```
如果创建多维数组就用多个中括号。在numpy中数组中的元素类型都相同，如果不同，numpy会强制转换

```python
np.zeros(10)
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

# 创建一个值域范围从10到49的向量
z = np.arange(10,50)  
array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
       44, 45, 46, 47, 48, 49])

# 反转一个向量  
z= np.arange(50)  
z = z[::-1]
array([49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33,
       32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16,
       15, 14, 13, 12, 11, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1,  0])

# 创建一个3*3的单位矩阵,且值从0到8  
z = np.arange(9).reshape(3,3)
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
```

### ndim

```python
a = np.array([1,2,3,4])
b = np.array([[1,2],[3,4]])
print("a的维度：",a.ndim, "b的维度:",b.ndim)

```

### shape

```python
a = np.array([1,2,3])
b = np.array([[1,2],[4,5]])
print("a的shape:",a.shape, "b的shape",b.shape)

a的shape: (3,) b的shape (2, 2)
```


### reshape
如果数量不够是会报错的

```python
a = np.arange(20)
print("a的shape:",a.shape)
b = a.reshape((4,5))
print("b的shape是:",b.shape, "a的shape:",a.shape)

a的shape: (20,)
b的shape是: (4, 5) a的shape: (20,)
```


### resize 
改变数组形状

```python
a = np.array([[2,3],[1,3]])
a = np.resize(a,(2,3))
a

# 从开始位置重复 即：2，3，1，3，2，3
array([[2, 3, 1],
       [3, 2, 3]])
```


reshape 是返回的副本，而resize则在原地修改
reshape 新开关不匹配时会报错，而resize则会调整

### astype

修改数据类型

```python
a = np.array([1.1, 1.2])
print("a dtype", a.dtype)
print("astype float32:", a.astype("float32").dtype)
print("原数据类型",a.dtype)
# 修改原数据类型
a = a.astype('float32')
print('修改后数据类型',a.dtype)

a dtype float64
astype float32: float32
原数据类型 float64
修改后数据类型 float32
```

### arange

```python
np.arange(0,100,9)
array([ 0,  9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99])
```

### linspace
linspace(from,to,num) 返回一个指定范围内的一维等差数列,它可以指定元素个数,但不能像arange 那样指定步长

```python
np.linspace(1,100,num=10)
array([  1.,  12.,  23.,  34.,  45.,  56.,  67.,  78.,  89., 100.])


```

### logspace

np.logspace(start,stop,num=50,endpoint=True, base=10,dtype=None)

```python
# 2的0到9次方间生成10个数
a = np.logspace(0,9,10,base=2)
a
array([  1.,   2.,   4.,   8.,  16.,  32.,  64., 128., 256., 512.])
```

### random
返回随机数组，size相当于shape指定了数组的行，列数
```python
np.random.randint(0,100,size=(3,4))
array([[50, 93, 18, 46],
       [72, 27, 38, 92],
       [36, 36, 17, 81]])
#random则只有一个size参数，不能指定范围，范围只能0~1
np.random.random(size=(4,5))
array([[0.94365774, 0.71249288, 0.13944588, 0.20441024, 0.80677842],
       [0.74175851, 0.51293879, 0.03104411, 0.93972059, 0.54942502],
       [0.62770764, 0.09163984, 0.23088541, 0.2154252 , 0.96221424],
       [0.84438567, 0.78581357, 0.28901496, 0.91072922, 0.46041454]])
```
如果你想只随机一次，后面再次生成与第一次相同，则需要固定seed
```python
np.random.seed(10) # 固定随机种子
np.random.randint(0,100,size=(3,5))
```


### zeros, ones
shape定义数组的形状，行，列。
zeros表示用0来填充元素，同样的还有ones
```python
np.zeros(shape=(3,4))
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])

np.ones(shape=(3,4))
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])
```

### where 

返回满足条件元素的索引

```python
arr = np.array([1, 3, 5, 7, 9, 2, 4, 6])

# 使用 np.where 找到大于 5 的元素的索引
indices = np.where(arr > 5)

print("大于 5 的元素的索引:", indices[0])
print("大于 5 的元素:", arr[indices])

大于 5 的元素的索引: [3 4 7]
大于 5 的元素: [7 9 6]
```

按条件替换

```python
arr = np.array([1, 3, 5, 7, 9, 2, 4, 6])  
  
# 使用 np.where 条件替换  
# 大于 5 的元素替换为 1，其他元素替换为 0  
result = np.where(arr > 5, 1, 0)  
  
print("原数组:", arr)  
print("条件替换后的结果:", result)

原数组: [1 3 5 7 9 2 4 6]
条件替换后的结果: [0 0 0 1 1 0 0 1]
```

生成新数组

```python
arr = np.array([-1, 2, -3, 4, -5, 6])  
  
# 将负数替换为0，正数保留  
result = np.where(arr < 0, 0, arr)  
  
print("原数组:", arr)  
print("将负数替换为0后的结果:", result)

原数组: [-1  2 -3  4 -5  6]
将负数替换为0后的结果: [0 2 0 4 0 6]
```


### 切片和索引

ndarray 可以通过索引或者切片来访问和修改，与python中list 切片操作一样。
但数组切片是原始数组视图，任何修改都会修改原始数据。如果不想修改需要使用copy.


### 广播机制

让所有输入数组都向其中形状最长的数组看齐，形状中不足的部分都通过在前面加1补齐。
输出数组的形状是输入数组形状的各个维度上的最大值。
如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为1时，这个数组能够用来计算，否则出错。
当输入数组的某个维度的长度为1时，沿着此维度运算时都用此维度上的第一组值。

```python
a = np.array([1,2,3,4])
b = np.array([4,5,6,7])
c = a * b  # 对应位置相乘
print(c)

[ 4 10 18 28]
```

如果两个形状不同的数组，numpy设计了一种广播机制，对开关较小的数组，在横向或者纵向上进行一定次数的重复，使其与形状较大的数组拥有相同的维度。


```python
c = np.array([[0,0,0],[10,10,10],[20,20,20],[30,30,30]])
d = np.array([1,2,3])
print(c + d)

[[ 1  2  3]
 [11 12 13]
 [21 22 23]
 [31 32 33]]

```

上面的例子将较小的d数组在行上进行了重复，然后进行的的计算。

```python
e = np.array([2,3])
f = np.array([1,])
print(e+f)

[3 4]
```

因为其中一个数值为1，故可以进行运算。

### 平均值 mean

当指定axis 时，则将对应的坐标轴进行累加然后平均，得到的是一给数组


### 中位数 median

按顺序排列的一组，取居于中间位置的数

### 标准差 std

平均值分散程度。 各数值与平均数的差平方再求算术平方根


### 方差 var

### 加权平均 average

将各数值乘以相应的权数，然后求和，再除以总的单位数

numpy.average(a, axis=None, weights=None, returned=False)

### 最大值 max
