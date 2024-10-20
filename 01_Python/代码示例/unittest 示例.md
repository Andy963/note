## 测试（unittest）

```python
import unittest

class MyTestCase(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('andy'.upper(), 'ANDY')

    def test_is_upper(self):
        self.assertTrue('ANDY'.isupper())
        self.assertFalse('Andy'.isupper())

if __name__ == '__main__':
    unittest.main()
```

通过继承unittest.TestCase来实现一个测试用例，在这个类中，定义的以test开关的方法，测试框架将把它当作独立的测试来执行。

如果我们希望在测试前做一些准备工作，在测试之后做一些清理工作，我们就用到了fixtures(固定装置)，指的测试开始前的准备工作setUp和测试完成后的清理工作tearDown
#### 方法级别的fixtures

```python
class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_sth(self):
        pass

    def tearDown(self):
        pass
```

#### 类级别的fixtures

```python
class MyTestCase(unittest.TestCase):
    def setUpClass(self):
        pass

    def tearDownClass(self):
        pass
```
#### 模块级别的fixtures
```python
def setUpModule():
    pass

def tearDownModule():
    pass
```

### 跳过测试和预计失败
unittest 支持直接跳过或按条件跳过测试，也支持预计测试失败：

通过 skip 装饰器或 SkipTest 直接跳过测试
通过 skipIf 或 skipUnless 按条件跳过或不跳过测试
通过 expectedFailure 预计测试失败
```python
class MyTestCase(unittest.TestCase):

    @unittest.skip("直接跳过")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),"满足条件跳过")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "满足条件不跳过")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("跳过")
        # test code that depends on the external resource
        pass

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "这个目前是失败的")

```

### 子测试
用不同的参数来测试同一段逻辑，但又不希望被视作同一个测试。就可以使用子测试
示例中使用了 with self.subTest(i=i) 的方式定义子测试，这种情况下，即使单个子测试执行失败，也不会影响后续子测试的执行。这样，我们就能看到输出中有三个子测试不通过
```python
class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

```

