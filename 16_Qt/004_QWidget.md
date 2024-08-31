所有可视控件的基类

每个控件都是矩形的，它们按照z轴顺序排列
控件由父控件和前面的控件裁剪（限制）
没有父控件的控件，称为窗口

## 控件的创建


## 大小位置

坐标系统

x() 相对于父控件的x位置，如果没有父控件即它是一个顶层控件，那么将相对于桌面的x位置

y() 相对于父控件的y位置，顶层控件相对于桌面的y位置

pos() x,y 的组合， QPoint(x,y)

width() 控件的宽度，不包含窗口框架
height() 控件的高度，不包含窗口框架

size() width 与height的结合，QSize(width, height)

geometry 用户区域相对于父控件的位置和尺寸组件 QRect(x,y, width, height)，要在控件显示完成后获取，具体的位置或者尺寸才是正确的

rect() 0,0, width,height的组件  QRect(x,y, width, height)

frameSize 框架大小
frameGeometry 框架尺寸

move(x,y) 操作的是x,y, 也就是Pos 包括窗口框架
resize(width, height) 操作的宽高，但不包括窗口框架
setGeometry(x_noFrame, y_noFrame, width, height) 参照的是用户区域
adjustSize() 根据内容自适应大小
setFixedSize() 设置固定尺寸


## 最大最小尺寸

获取：
minimumWidth() 最小尺寸的宽度
minimumHeight() 最小尺寸的高度
minimumSize()
maximumWidth()
maximumHeight()
maximumSize()

设置：
setMaxmimumWidth()
setMaximumHeight()
setMaximumSize()
setMinimumWidth()
setMinimumHeight()
setMinimumSize()

设置了最大最小之后无法通过拖拽或者resize来修改其大小。

## 内容边距

设置内容边距  setContentsMargins(左，上，右，下)
获取内容边距 getContentsMargins(左，上，右，下) 
获取内容区域 contentsRect()

注意是控件本身留够对应的大小

## 鼠标
设置鼠标形状
Qt.ArrowCursor
Qt.UpArrowCursor
Qt.CrossCursor
Qt.IBeamCursor
Qt.WaitCursor
Qt.BusyCursor
Qt.ForbiddenCursor

QCursor  自定义

```python
pixmap = QPixmap("cursor.png")  
new_pixmap = pixmap.scaled(50, 50)  # 设置鼠标图标的大小  
cursor = QCursor(new_pixmap, 0, 0)  # 后面的两个参数是鼠标图标的偏移量  
window.setCursor(cursor)
```

window.unsetCursor() 将重置鼠标的样式
pos() 获取鼠标位置信息
setPos(x,y)设置鼠标的位置

鼠标跟踪
setMouseTracking(True)

## 事件消息
showEvent() 显示事件
closeEvent() 关闭事件


moveEvent() 移动事件
resizeEvent() 调整大小事件

鼠标事件：

enterEvent() 鼠标进入事件
leaveEvent() 鼠标离开事件
mousePressEvent() 鼠标被按下，通过button来获取是哪个键被按下
mouseReleaseEvent() 鼠标被释放
mouseDoubleClickEvent() 鼠标双击
mouseMoveEvent() 鼠标移动

键盘事件：

keyPressEvent()  键盘按下
keyReleaseEvent()  键盘释放

```python
def keyPressEvent(self, evt):
	if evt.key() == Qt.Key_Tab:
		print('点击了tab键')
```

当有多个组合键时：
```python
if evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and evt.key() == Qt.Key_A:
	pass
# 这里ctrl 与shift 进行与运算，与前面的modifiers 进行比较可以判断是否两个键都按下了
```

焦点事件：

focusInEvent() 获得焦点事件
focusOutEvent()  失去焦点事件


拖拽事件：

dragEnterEvent() 拖拽进入控件时
dragLeaveEvent() 拖拽离开控件时
dragMoveEvent() 拖拽在控件内移动时
dropEvnet() 拖拽入下时

绘制事件：

paintEvent 显示控件，更新控件时

 改变事件：
 changeEvent() 窗体改变，字体改变

右键菜单：

contextMenuEvent() 访问右键菜单时调用

inputMethodEvent() 输入切换

如果元素的处理了事件消息，那么它不会往父组件传递，但是如果元素没有处理事件，那么事件会往父组件 传递。
例如：当界面中有一个QPushButton,一个QLabel, button有实现点击事件，而label没有，所以点击QPushButton时不会将事件向父组件传递，而lable因为没有实现点击事件，那么点击时事件会向父组件传递。

如果要阻止事件向父组件传递，此时可以在对应的事件中，通过event.accept() 就不会向父组件传递。类似js中的preventDefault(), 但是如何使用event.ignore() 事件会继续上传。

