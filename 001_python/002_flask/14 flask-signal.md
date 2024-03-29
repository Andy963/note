## 信号笔记：
使用信号分为3步，第一是定义一个信号，第二是监听一个信号，第三是发送一个信号。以下将对这三步进行讲解：

1. 定义信号：定义信号需要使用到blinker这个包的Namespace类来创建一个命名空间。比如定义一个在访问了某个视图函数的时候的信号。示例代码如下：
    ```python
    # Namespace的作用：为了防止多人开发的时候，信号名字冲突的问题
    from blinker import Namespace

    mysignal = Namespace()
    visit_signal = mysignal.signal('visit-signal')
    ```
2. 监听信号：监听信号使用singal对象的connect方法，在这个方法中需要传递一个函数，用来接收以后监听到这个信号该做的事情。示例代码如下：
    ```python
    def visit_func(sender,username):
        print(sender)
        print(username)
    mysignal.connect(visit_func)
    ```
3. 发送信号：发送信号使用singal对象的send方法，这个方法可以传递一些其他参数过去。示例代码如下：
  ```python
  mysignal.send(username='zhiliao')
  ```

### Flask内置的信号：
1. template_rendered：模版渲染完成后的信号。
2. before_render_template：模版渲染之前的信号。
3. request_started：模版开始渲染。
4. request_finished：模版渲染完成。
5. request_tearing_down：request对象被销毁的信号。
6. got_request_exception：视图函数发生异常的信号。一般可以监听这个信号，来记录网站异常信息。
7. appcontext_tearing_down：app上下文被销毁的信号。
8. appcontext_pushed：app上下文被推入到栈上的信号。
9. appcontext_popped：app上下文被推出栈中的信号
10. message_flashed：调用了Flask的`flashed`方法的信号。