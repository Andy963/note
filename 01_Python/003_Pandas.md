Jupyter Notebook 快捷键：
* a,b在上/下添加插入cell
* x删除cell
* shift enter 执行cell
* tab 补全
* 切换模式 y,m
* 打开帮助文档shift + tab
## Series
Series是一个类似一维数组的结构，有两部分组成：index,values
Series创建由列表或者numpy数组创建，也可以由字典创建

### Series创建

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
### Series索引与切片

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
### Series属性
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
### Series常用方法

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

## DataFrame
DataFrame是一个表格型数据，将Series从一维扩展到多维，有行索引，也有列索引
行索引：index
列索引：columns
值：values

### DataFrame创建
numpy，字典两种创建方式

```python

data = [('Andy',18),('Lisa', 19),('Bob',27)]  
df = pd.DataFrame(data=data, columns = ['Name', 'Age'])
  Name Age
0,Andy,18
1,Lisa,19
2,Bob,27

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

### DataFrame属性
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

### DataFrame索引与切片
对行/列进行索引，对元素进行索引
当设定了显式索引，就不能用隐式索引

#### 索引

```python
import pandas as pd

df = pd.read_excel('data.xlsx') 

col_index = df.columns.get_loc('随访时间')
col_index = df.columns.to_list().index('随访时间')
col_index = df.columns.get_indexer_for(['随访时间'])[0]
```

#### 取列
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

#### 取行
loc,iloc, loc是基于label, 而iloc是基于整数位置（integer)

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
#### 取元素

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
#### 切片

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


#### set_index

```python
#将time作为行索引
df.set_index(df['time'])
	time	salary
time		
2020-06-01	2020-06-01	10000
2020-06-02	2020-06-02	11000
2020-06-04	2020-06-04	11100

# 将它作用到原数据上：inplace=True
df.set_index(df['time'],inplace=True)
df
	time	salary
time		
2020-06-01	2020-06-01	10000
2020-06-02	2020-06-02	11000
2020-06-04	2020-06-04	11100
```
关于index的一点补充:
set_index中第一个参数为字段名，如果直接写的字段名如：time,此时drop参数才有效，默认行为是drop=True,此时指定time为索引，即删除了time这一列，将它用来作为索引。而如果是像上面那样使用的
df['time']这样指定，则drop失去作用。

```python
#
df.set_index('time',inplace=True,drop=False)
df
	time	salary
time		
2020-06-01	2020-06-01	10000
2020-06-02	2020-06-02	11000
2020-06-04	2020-06-04	11100
```
### drop

手动删除列：注意在drop方法中 axis=1时表示列，axis=0表示行

```python
df.drop(labels='time',axis=1)
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

to_datetime

将字符串转成时间序列：to_datetime
设置索引：set_index
```python
dic = {
    'time':['2020-06-01','2020-06-02','2020-06-04'],
    'salary':[10000,11000,11100]
}
df = pd.DataFrame(data=dic)

# to_datetime方法
df['time'] = pd.to_datetime(df['time'])
df.dtypes
time      datetime64[ns]
salary             int64
dtype: object
```

### where 

返回一个与原数据相同大小的新对象，满足条件的元素保持原值，不满足条件的元素将被替换为NaN。这个方法常常用于数据清洗、过滤和条件筛选

```python
# 创建示例 DataFrame  
data = {  
    'A': [1, 2, 3, 4, 5],  
    'B': [5, 4, 3, 2, 1]  
}  
df = pd.DataFrame(data)  
  
# 使用 where 进行条件筛选  
result = df.where(df > 2)  
print(result)

     A    B
0  NaN  5.0
1  NaN  4.0
2  3.0  3.0
3  4.0  NaN
4  5.0  NaN
```

应用场景：

数据清洗：异常值或不符合条件的数值过滤掉

```python
# 假设我们要保留所有大于0的数，其余置为NaN
cleaned_data = df.where(df > 0)
```

条件替换: 比如将某列中的负值替换为0。

```python
df['A'] = df['A'].where(df['A'] > 0, 0)
```

生成过滤后的数据集: 通过条件筛选并得到一个新数据集

```python
filtered_data = df.where((df['A'] > 2) & (df['B'] < 4))
```

### apply
可以沿着指定的轴（行或列）应用一个函数

```python
def func(x):  
    return x + 5  
data = {  
    'A': [1, 2, 3, 4, 5],  
    'B': [5, 4, 3, 2, 1]  
}  
df = pd.DataFrame(data)  
df['A'].apply(func)

0,6
1,7
2,8
3,9
4,10

df.apply(lambda x: x.sum())  # 按列求和
df.apply(lambda x: x + 1, axis=1)  # 对每行加1
  
```


### map
对 Series 进行元素级别的转换

```python
# 对 Series 进行元素级别的转换  
def func(x):  
    return x + 5  
data = {  
    'A': [1, 2, 3, 4, 5],  
    'B': [5, 4, 3, 2, 1]  
}  
df = pd.DataFrame(data)  
df.map(func)

0,6,10
1,7,9
2,8,8
3,9,7
4,10,6

df['A'].map(lambda x: x * 2)  # 对 Series A 中的每个元素乘以2
```


### applymap

与map类似，deprecated

```python
df.applymap(lambda x: x * 2)  # 对 DataFrame 中的每个元素乘以2
```

### concat 
axis=0表示按行拼接，axis=1表示按列拼接

```python
data1 = [('Andy', 18),('Lisa', 19),('Bob', 27)]  
data2 = [('安迪', 81),('丽莎', 91),('鲍博', 72)]  
df1 = pd.DataFrame(data=data1, columns = ['Name', 'Age'])  
df2 = pd.DataFrame(data=data2, columns = ['Name', 'Age'])  
# df1  
# df2  
# 按行拼接  
result = pd.concat([df1, df2], axis=0, ignore_index=True)

   Name  Age
0  Andy   18
1  Lisa   19
2   Bob   27
3    安迪   81
4    丽莎   91
5    鲍博   72

# 按行拼接  
result = pd.concat([df1, df2], axis=1, ignore_index=True)
      0   1   2   3
0  Andy  18  安迪  81
1  Lisa  19  丽莎  91
2   Bob  27  鲍博  72
```


### merge

```python
df1 = pd.DataFrame({'key': ['K0', 'K1', 'K2'],  
                    'A': ['A0', 'A1', 'A2']})  
  key A  
0,K0,A0
1,K1,A1
2,K2,A2

df2 = pd.DataFrame({'key': ['K0', 'K1', 'K3'],  
                    'B': ['B0', 'B1', 'B3']})
  key B
0,K0,B0
1,K1,B1
2,K3,B3

# 基于 'key' 列进行合并，默认 how='inner'  
result = pd.merge(df1, df2, on='key')
  key   A   B
0  K0  A0  B0
1  K1  A1  B1
```