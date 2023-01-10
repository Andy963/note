## flask

### 基本使用流程

* 导入flask
* 实例化flask对象
* 写视图函数
* run()

```py
from flask import Flask

# 创建flask对象
app = Flask(__name__)

@app.route('/index',methods=['GET','POST'], endpoint='index')
def index():
    return 'hello world'


@app.route('/login')
def login():
    return 'login'

if __name__ == '__main__':
    app.run()
```


### 路由

```python
#  endpoint不能重名,写装饰器时要加functools.wraps()
@app.route('/login',methods=['GET','POST'],endpoint="login")
def login():
    pass

#  动态路由
@app.route('/index')
def login():
    pass

@app.route('/index/<name>')
def login(name):
    pass

@app.route('/index/<int:nid>')
def login(nid):
    pass
```

### 视图

#### 获取参数

```python
@app.route('/index')
def login():
    request.args # GET形式传递的参数
    request.form # POST形式提交的参数
```

#### 返回数据

```python
@app.route('/index')
def login():
    return render_template('模板文件')
    return jsonify()
    reutrn redirect('/index/') # reutrn redirect(url_for('idx')) 别名
    return "...."
```

### 前端渲染

dict.items()需要加括号
dict['name'] 也可以
dict.get('name', None)


### session
加密的形式保存在浏览器的cookie上

导入session, 但需要设置secret_key
app.secret_key = '随机字符串'

### 蓝图

构建业务功能可拆分的目录结构，模块化，结构清晰。

