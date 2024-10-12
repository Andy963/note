## paramiko

### ssh
```python
def ssh_func(hostname, command):
    """
    通过 paramiko 连接远程主机，并执行指定的命令
    :param hostname:hostname 主机ip
    :param command:要执行的指令
    :return: 返回执行指令后返回的信息
    """
    private_key = paramiko.RSAKey.from_private_key_file(settings.SSH_PRIVATE_KEY_PATH, password='zjgisadmin')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USER, pkey=private_key)
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read()
    ssh.close()
    return result.decode('utf-8')
```

### sshProxy
```python
#!usr/bin/env python
# *- coding:utf-8 -*-
# Author: Andy
import paramiko


class SSHProxy(object):

    def __init__(self, hostname, port, username, private_key_path=None, password=None):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.private_key_path = private_key_path
        self.password = password

        self.transport = None

    def open(self):
        # 通过密钥连接
        private_key = paramiko.RSAKey.from_private_key_file(self.private_key_path)
        self.transport = paramiko.Transport((self.hostname, self.port))
        self.transport.connect(username=self.username, pkey=private_key)

    def open_with_password(self):
        # 通过密码连接
        self.transport = paramiko.Transport((self.hostname, self.port))
        self.transport.connect(username=self.username, password=self.password)

    def close(self):
        self.transport.close()

    def command(self, cmd):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh._transport = self.transport
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        ssh.close()
        return result

    def upload(self, local_path, remote_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.put(local_path, remote_path)
        sftp.close()


    def __enter__(self):
        if self.password:
            self.open_with_password()
        else:
            self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

# if __name__ == '__main__':
# with SSHProxy('127.0.0.1', 2222, 'root', password='zjgisadmin') as ssh:
#     v1 = ssh.command('sudo ifconfig')
#     print(v1)

```