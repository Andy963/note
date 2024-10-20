### socket
wrap_socket 旧的接口不能用，改为使用context

```python
cert_file = str('')
key_file = str('')
context = ssl.SSLContext(ssl.ProTocol_SSLv23)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
context.load_cert_chain(cert,key)
_socket = context.wrap_socket()
```
