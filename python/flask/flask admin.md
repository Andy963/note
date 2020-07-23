### 安装
```shell
pip install Flask-Admin
pip install flask-babelex # 国际化
```
汉化设置
```python
from flask_babelex import Babel

app = Flask(__name__)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
```
### BaseView
```python
from flask_admin import Admin,BaseView, expose
flask_admin = Admin()
def create_app(object_name):
    """Create the app instance via `Factory Method`"""
    flask_admin.init_app(app)
    flask_admin.add_view(CustomView(name='Custom'))

class CustomView(BaseView):
    @expose('/')  # 类似route
    def index(self):
        return self.render('admin/custom.html')

    @expose('/second_page')
    def second_page(self):
        return self.render('admin/second_page.html')
# BaseView 子类必须定义一个路由 URL 为 / 的视图函数, 在 Admin 界面中只会默认显示该视图函数, 其他的视图函数是通过 / 中的链接来实现跳转的
```
html
```html
{% extends 'admin/master.html' %}
{% block body %}
  This is the custom view!
  <a href="{{ url_for('customview.second_page') }}">Link</a>
{% endblock %}
```

### modelView
```python
from flask.ext.admin.contrib.sqla import ModelView

class CustomModelView(ModelView):
    """View function of Flask-Admin for Models page."""
    pass

def create_app(object_name):
    flask_admin.init_app(app)
    # Register view function `CustomView` into Flask-Admin
    flask_admin.add_view(CustomView(name='Custom'))
    # Register view function `CustomModelView` into Flask-Admin
    models = [Role, Tag, Reminder, BrowseVolume]
    for model in models:
        flask_admin.add_view(
            CustomModelView(model, db.session, category='Models'))  
```