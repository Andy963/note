
### Fixture

#### 方法级
```python
class MyTestCase(unittest.TestCase):
	def setUp(self):
        # 每个方法执行一次
		pass
	def tearDown(self):
		pass
```

#### 类级

```python
class MyTestCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
        # 每个测试类执行一次
		pass
    @classmethod
	def tearDownClass(cls):
		pass
```


#### 模块级

```python
def setUpModule():
    # 在本模块所有用例前执行
	pass

def tearDownModule():
	pass
```