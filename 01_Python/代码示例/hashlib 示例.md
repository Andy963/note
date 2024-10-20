### hashlib简单实例

```python
import hashlib
string = 'hello'
md = hashlib.md5()
md.update(string.encode('utf-8'))
md5string = md.hexdigest()
```

