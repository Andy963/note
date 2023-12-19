
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

##### 获取某列的数字索引

```python
import pandas as pd

df = pd.read_excel('data.xlsx') 

col_index = df.columns.get_loc('随访时间')
col_index = df.columns.to_list().index('随访时间')
col_index = df.columns.get_indexer_for(['随访时间'])[0]
```

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

##### 取行
loc,iloc
df.loc['a'] 这里面是取索引为 'a'的行，取的一是一行数据，而不是列:

|  | 0 |
| :--- | :--- |
| name | 郭瑞华 |
| 是否 | 否 |
| s\_14 | 2023-12-28 |
| s\_7 | 2024-01-04 |
| s\_1 | 2024-01-10 |

而对于iloc，df.iloc[0] 与上面的效果相同，因为i是取数字索引，而这里的数字索引0与上面的loc相同,那么为什么会有两个呢？ 因为数据的索引不一定是数值类型，也可能是其它非数值类型，而iloc只能使用整型。

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

匹配到相等的修改：

```python
import pandas as pd  
  
dybl = pd.read_csv('./dongyuanbinglilijiajieguo.csv',encoding='gbk')  
dy = pd.read_excel('./东院.xlsx')  
  
for i in range(len(dybl)):  
    row = dybl.iloc[i]  
    id = row[0] # 如果有玩名，这里可以通过列名取数据如：row['检查号'] 
    dy.loc[dy['检查号'] == id, ['病理']] = row[6] # 匹配到相等，并赋值到'病理' 这一列
  
dy.to_excel('./东院1026.xlsx')
```


### 修改dataframe

df.loc, df.iloc都可以修改

```python
data = pd.read_excel('rs.xlsx')  
data.loc[0, 'name'] = '周'
data.iloc[0, 0] = '王'

# 上面两种效果相同，但为什么用法不一样呢，具体就是要理解 loc与iloc的区别，iloc中只能是数值索引，所以不能用data.iloc[0, 'name'], 而 loc[0, 'name'] 修改的是第0行，name这一列的值，同样的道理，iloc[0,0] 因为只能用数值索引，所以第一个0表示 0 行，而'name'对应的列索引也是0，所以是[0,0]
```

同样通过条件去修改元素

```python
data.loc[data.name=='陈剑','name'] = '王'
# name是它的列名，可以通过data.name=='陈剑'定位到具体的行，第二个name则表明修改它的name属性为王

data.iloc[data.name=='陈剑',0] = '周' 
# 因为是iloc,所以第二个不能用'name'，而是用它对应的索引数字0
```


ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

```python
df1.loc[(df1['姓名'] == name) & (df1['性别'] == gender) & (df1['年龄'] == age), '病理诊断'] = row['病理诊断']

# 注意加括号，并且在pandas中使用 & 不要使用and
```

ref:https://stackoverflow.com/questions/36921951/truth-value-of-a-series-is-ambiguous-use-a-empty-a-bool-a-item-a-any-o




