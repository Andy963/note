
pandas中两个常用的类：Series, DataFrame

### Series
Series是一个类似一维数组的结构，有两部分组成：index,values
Series创建由列表或者numpy数组创建，也可以由字典创建

#### Series创建
```python
#Series数据源必须为一维
#列表
Series(data=[1,2,34])
0     1
1     2
2    34
dtype: int64

#numpy数组
Series(data=np.random.randint(0,100,size=(4,))) #如果size指定了两个维度就会报错
0    51
1    10
2    95
3    13
dtype: int32

#data为字典，key被当作索引，value为值
dic={'a':1,'b':2}
Series(data=dic)
a    1
b    2
dtype: int64
```
#### Series索引与切片
Series索引分为隐式索引，显式索引，它的索引可以是字符串
```python
s =Series(data=[1,2,3],index=['数学','语文','英语'])
数学    1
语文    2
英语    3
dtype: int64
```

索引与切片操作：
```
s[-1]
3
s[1:] # 切片操作
语文    2
英语    3
dtype: int64
```
#### Series属性
shape,size,index.values
```python
s.shape
(3,)
s.size
3
s.index
Index(['数学', '语文', '英语'], dtype='object')
s.values
array([1, 2, 3], dtype=int64)
```
#### Series常用方法
head,tail,unique,isnull,notnull,add,sub, mul,div
```python
s.head(2)  # 显示前两条数据
数学    1
语文    2
dtype: int64
s.tail(2)  # 显示后两条数据
语文    2
英语    3
dtype: int64
s.unique（）  # 去重
s =Series(data=[1,2,2,1])
s.unique()
array([1, 2], dtype=int64)

算术运算：add,sub,mul,div 
运算规则：索引匹配的值进行算术运算，否则补空,注意最后的索引项相当于并集
s1=Series(data=[1,2,3,4])
s2=Series(data=[3,2,1])
s1.add(s2)
0    4.0
1    4.0
2    4.0
3    NaN
dtype: float64
s3=Series(data=[1,2,3,4],index=['a','b','c','d'])
s4=Series(data=[1,2,3,4],index=['a','e','c','f'])
s3.mul(s4)
a    1.0
b    NaN
c    9.0
d    NaN
e    NaN
f    NaN
dtype: float64

bool可以作为索引取值：True表示取，False表示舍
s5 = Series(data=[1,2,3,4],index=['a','b','c','d'])
s5[[True,False,True,False]]
a    1
c    3
dtype: int64

# 获取bool值
s5.isnull()
a    False
b    False
c    False
d    False
dtype: bool
将这组bool值作为索引，用来清洗数据
s5[s5.notnull()]
s5=s3.mul(s4)
s5
a    1.0
b    NaN
c    9.0
d    NaN
e    NaN
f    NaN
dtype: float64
s5[s5.notnull()]
a    1.0
c    9.0
dtype: float64
```

### DataFrame
DataFrame是一个表格型数据，将Series从一维扩展到多维，有行索引，也有列索引
行索引：index
列索引：columns
值：values

#### DataFrame创建
numpy，字典两种创建方式

```python
df=DataFrame(data=np.random.randint(1,50,size=(3,4))) # size只能指定2维，可以通过index,columns指定行，列索引
	0	1	2	3
0	8	30	43	32
1	22	8	21	26
2	31	13	32	6

dic={
    'name':['andy','zhou'],
    'age':[20,30]
}
df = DataFrame(data=dic)  # key作为列索引，行索引默认为数字
df
	name	age
0	andy	20
1	zhou	30
显式指定行索引：
df = DataFrame(data=dic,index=['a','b'])
	name	age
a	andy	20
b	zhou	30
```

#### DataFrame属性
values,columns,index,shape
```python
df.values
array([['andy', 20],
       ['zhou', 30]], dtype=object)
       
df.columns
Index(['name', 'age'], dtype='object')
df.index
Index(['a', 'b'], dtype='object')
df.shape
(2, 2)
```

#### DataFrame索引与切片
对行/列进行索引，对元素进行索引
当设定了显式索引，就不能用隐式索引

##### 取列
直接通过括号取的不是行，而是列：
```python
df
	name	age
a	andy	20
b	zhou	30

df['a']  # 报错没有
df['name']
a    andy
b    zhou
Name: name, dtype: object
```
取一列时直接写列索引即可，如果取多列，为了表示多列，用一个列表
```python
df[['name','age']]
	name	age
a	andy	20
b	zhou	30
```
##### 取列
loc,iloc
```python
df.loc['a']  # 显式索引
name    andy
age       20
Name: a, dtype: object
df.iloc[0]  # 隐式索引
name    andy
age       20
Name: a, dtype: object
```
同样的道理，取多行，要用一个列表表示 
```python
df.loc[['a','b']]
	name	age
a	andy	20
b	zhou	30

df.iloc[[0,1]] 
	name	age
a	andy	20
b	zhou	30
```
##### 取元素
取单个元素
```python
df.loc['a','name']  # 括号内分别表示 行列
'andy'
df.iloc[0,1]  # 使用iloc时行列都得使用隐式索引
20
```
取多个元素：记住逗号左边为行，右边为列
```python
df.loc[['a','b'],['name']]
	name
a	andy
b	zhou

df.iloc[[0,1],[0]]
	name
a	andy
b	zhou
```
##### 切片
一个中括号表示 切行,切列一定要用loc/iloc
```python
df[0:1]
	name	age
a	andy	20

#列
df.loc[:,'name':'age']  # 注意是开区间
	name	age
a	andy	20
b	zhou	30
df.iloc[:,0:1]
	name
a	andy
b	zhou
```