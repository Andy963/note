### server 端
/etc/ssh/sshd_config
```shell
ClientAliveCountMax 600
```
运行 `service sshd reload`

### 客户端
在.ssh目录下键config文件
```
ServerAliveInterval 60
```
保存后重新打开ssh