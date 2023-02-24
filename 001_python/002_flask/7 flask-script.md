## click 笔记
flask_scipt 已经快10年没有维护了，新版本migrate也已经不支持了，所以这里转换到使用click,下面是一个相对稍高级的用法，将命令直接注册到蓝图上，对于app
同理（理解blueprint和app的关系）

```python

@user_bp.cli.command('create_user')
@click.argument('nick_name')
@click.argument('password')
def create_user(nick_name, password):
    """
    Func: 在蓝图上注册命令：命令行添加user
    Args: user必须的参数:nick_name, password
    Example: flask user create_user 'andy' '123456'
    Return: None
    :Author:  Andy
    :Version: 1.0
    :Created:  2022/3/26 下午9:08
    :Modified: 2022/3/26 下午9:08
    """
    user = User()
    user.nick_name = nick_name
    user.password = password
    with db.auto_commit():
        db.session.add(user)

#对应蓝图
# 因为指定了cli_group所以在命令行时要使用flask user,指定 cli_group=None 会删除嵌套并把命令直接合并到应用级别
user_bp = Blueprint('user', __name__, url_prefix='/user', cli_group='user')

```

## flask_script笔记：
Flask-Script的作用是可以通过命令行的形式来操作Flask。例如通过命令跑一个开发版本的服务器、设置数据库，定时任务等。要使用Flask-Script，可以通过`pip install flask-script`安装最新版本。

### 命令的添加方式：
1. 使用`manage.commad`：这个方法是用来添加那些不需要传递参数的命令。示例代码如下：
    ```python
    manager = Manager(app)
    manager.add_command("db",db_manager)

    @manager.command
    def greet():
        print('你好')
    ```
2. `使用manage.option`：这个方法是用来添加那些需要传递参数的命令。有几个参数就需要写几个`option`。示例代码如下：
    ```python
    @manager.option("-u","--username",dest="username")
    @manager.option("-e","--email",dest="email")
    def add_user(username,email):
        user = BackendUser(username=username,email=email)
        db.session.add(user)
        db.session.commit()
    ```

3. 如果有一些命令是针对某个功能的。比如有一堆命令是针对ORM与表映射的，那么可以将这些命令单独放在一个文件中方便管理。也是使用`Manager`的对象来添加。然后到主manage文件中，通过`manager.add_command`来添加。示例代码如下：
db_script.py

```python
from flask_script import Manager

db_manager = Manager()

@db_manager.command
def init():
    print('迁移仓库创建完毕！')

@db_manager.command
def revision():
    print('迁移脚本生成成功！')

@db_manager.command
def upgrade():
    print('脚本映射到数据库成功！')
```

manage.py
```python
from db_script import db_manager

manager = Manager(app)
manager.add_command("db",db_manager)
```
### 实例
```python
from flask_script import Manager
from models import app
from models import NewUser,db

manager = Manager(app)

@manager.command
def greet():
    print('hello')

@manager.option("-n", "--name", dest="name")
@manager.option('-a', '--age', dest='age')
def add_user(name,age):
    print("你要输入的用户名是：%s 年龄是 %s" %(name, age))
    user = NewUser(name=name,age=age)
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
```
然后在shell中运行：`python manage.py add_user -n "andy" -a "18"`