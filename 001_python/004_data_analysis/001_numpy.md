

### 数据分析三剑客
numpy
pandas
matplotlib

notebook 快捷键：
* a,b在上/下添加插入cell
* x删除cell
* shift enter 执行cell
* tab 补全
* 切换模式 y,m
* 打开帮助文档shift + tab

### numpy

#### 创建数组
```python
import numpy as np
arr = np.array([1,2,3])
```
如果创建多维数组就用多个中括号。在numpy中数组中的元素类型都相同，如果不同，numpy会强制转换

#### zeros,ones
shape定义数组的形状，行，列。
zeros表示用0来填充元素，同样的还有ones
```python
np.zeros(shape=(3,4))
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])
```

#### linspace，arange
linspace(from,to,num) 返回一个指定范围内的一维等差数列,它可以指定元素个数，而arange则指定步长
```python
np.linspace(1,100,num=10)
array([  1.,  12.,  23.,  34.,  45.,  56.,  67.,  78.,  89., 100.])

np.arange(0,100,9)
array([ 0,  9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99])
```

#### random
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