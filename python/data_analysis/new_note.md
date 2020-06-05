
### to_datetime && set_index && drop

#### to_datetime
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

#### set_index
```
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
#### drop
手动删除列：注意在drop方法中 axis=1时表示列，axis=0表示行
```python
df.drop(labels='time',axis=1)
```