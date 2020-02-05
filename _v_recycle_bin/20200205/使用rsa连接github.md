#### 添加rsa

前提条件：
- （已经配置了账号，用户名，并将rsa添加到github）

##### 1 运行ssh-agent
```shell
 eval $(ssh-agent -s)
```
##### 2 修改id_rsa文件权限
```shell
chmod 600 id_rsa
```
##### 3 将id_rsa交给ssh-agent
```shell
ssh-add id_rsa
```
测试是否成功
```shell
ssh -vT git@github.com
```

ref: https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent

##### 戴丽连接github

```shell
#如果是http 就替换socks5， https同理
git config --global http.proxy socks5://127.0.0.1:10808  
git config --global https.proxy socks5://127.0.0.1:10808 
```
```shell
#取消
git config --global --unset https.github.com.proxy
git config --global --unset http.github.com.proxy
```
