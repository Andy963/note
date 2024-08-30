QObject 是所有QT对象的基类


## 对象名称，属性

setObjectName(str) 给一个qt对象设置一个名称,一般当作id使用
objectName() 获取qt对象的名称
setProperty('k', v) 给一个qt对象动态的添加一个属性与值
property('k') 获取一个对象的属性值
dynamicPropertyNames() 获取一个对象中所有通过setProperty()设置的属性名称

设置样式：
setStyleSheet("font-size:20px; color:red;")
如果要写在独立文件中：文件后缀必须是qss
a.qss
```css
QLabel {
	font-size:20px;
	color:red;
}

/* 如果是QLabel#notice 这里的Notice表示对应的组件名称，即通过setObjectName设置的，当作id使用
*/

/*里的notice_level 表示这个组件有一个notice_level属性，并且值是normal 
这里的notice_level 可以通过setProperty 设置，如setProperty('notice_level', 'normal')
*/
QLabel#notic[notice_level='normal'] {
	color:green;
	border-color:green;
}
QLabel#notic[notice_level='warning'] {
	color:yellow;
	border-color:yellow;
}
```

在文件中：
```python
with open('a.qss', 'r') as f:
app.setStyleSheet(f.read())
```

## 父子对象

setParent(p) 设置父对象，父对象只能设置一个
parent() 获取父对象
children() 获取所有子对象
findChild(a,b,c) // 参数a可以是类型QObject, 或者类型元组如：(QPushButton, QLabel)
//参数b可以是ObjectName, 参数c 查找选项，只有两种值，FindChildrenRecursively, FindDirectChildrenOnly 默认是前者，会递归查找
findChildren(a,b,c)

QObject 继承树，所有的Qt对象都直接或者间接的继承自QObject,当一个QObject被创建出来时，如果使用了其它对象作为父对象，那么它本身就会被添加到父对象的children列表中。
当这个父对象被销毁时，这个QObject对象也会被销毁。

QWidget 扩展了父子关系，当一个控件设置了父控件时，会被包含在父控件内部，受父控件区域裁剪（子控件不会超出父控件的范围），父控件被删除时，子控件会自动被删除。


## 信号

信号（signal)与槽（slot)是qt中的核心机制，主要作用在对象之间进行通讯。
信号：当一侦控件的状态发生改变时，向外界发出的信息
槽：一个执行某些操作的函数/方法

所有继承自QWidget的控件都支持信号与槽的机制

例如内置的信号，QPushButton 的pressed, clicked 也可以自定义pyqtSignal

连接方式： object.信号.connect(函数)

一个信号可以连接多个函数
一个信号也可以连接另一个信号
信号的参数可以是任何python类型
一个槽可以监听多个信号

widget.信号.connect(slot)
obj.disconnect() 取消连接信号与槽
widget.blockSignals(bool) 临时阻止指定控件与它所有的信号与槽的连接
widget.singalsBlocked() 查看当前信号与槽的连接是否被阻止
widget.receivers('signal')

对于QObject 内置的信号有：ObjectNameChange(objectName) 对象名字被修改时触发, destroyed(obj) 对象销毁时触发

## 类型判定

o.isWidgetType()
o.inherits('QWidget')


## 对象删除

obj.deleteLater() 删除一个对象时，也会解除它与父对象之间的关系，而deleteLater并没有立即将对象销毁，而是向主消息循环发送了一个event, 下一次消息循环收到这个event之后才会销毁对象。它有两个后果：好处是可以在延迟删除的过程中完成一些操作，坏处是内存释放不及时。


## 事件处理

childEvent
customEvent
eventFilter
installEventFilter
removeEventFilter
event


## 定时器

timer_id = startTimer(ms, Qt.TimerType)， Qt.PreciseTimer 毫秒准确，Qt.CoarseTimer 5% 误差间隔， Qt.VeryCoarseTimer 只能到秒级
killTimer(timer_id) 根据定时器Id， 杀死定时器
timerEvent  定时执行事件

```python
class MyLabel(QLabel):  
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        self.setText("10")  
        self.move(100, 100)  
        self.timer_id = self.startTimer(1000)  
  
    def timerEvent(self, *args, **kwargs):  
        cur_sec = int(self.text())  
        cur_sec -= 1  
        self.setText(str(cur_sec))  
        if cur_sec == 0:  
            print("停止")  
            self.killTimer(self.timer_id)
```
## 语言翻译