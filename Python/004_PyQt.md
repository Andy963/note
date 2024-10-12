## 环境安装
```pyhon
pip install PyQt5 -i https://pypi.douban.com/simple
pip install PyQt5-tools -i https://pypi.douban.com/simple
```

## 主要内容

- 基本程序结构
- 控件的特性和使用
- 控件的样式
- 资源加载
- 控件的布局
- 事件和信号
- 动画特效
- 界面跳转
- 设计工具使用
- 额外

## 基本实例

```python
#1创建一个应用程序对象
app = QApplication(sys.argv)
print(app.arguments())
print(qApp.arguments())

#2控件操作
创建控件，操作控件，信号处理等等。

#3进入主消息循环，不要停止
sys.exit(app.exec_())
```

## QObject
QObject 是所有QT对象的基类
### 对象名称，属性

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

### 父子对象

setParent(p) 设置父对象，父对象只能设置一个
parent() 获取父对象
children() 获取所有子对象
findChild(a,b,c) // 参数a可以是类型QObject, 或者类型元组如：(QPushButton, QLabel)
//参数b可以是ObjectName, 参数c 查找选项，只有两种值，FindChildrenRecursively, FindDirectChildrenOnly 默认是前者，会递归查找
findChildren(a,b,c)

QObject 继承树，所有的Qt对象都直接或者间接的继承自QObject,当一个QObject被创建出来时，如果使用了其它对象作为父对象，那么它本身就会被添加到父对象的children列表中。
当这个父对象被销毁时，这个QObject对象也会被销毁。

QWidget 扩展了父子关系，当一个控件设置了父控件时，会被包含在父控件内部，受父控件区域裁剪（子控件不会超出父控件的范围），父控件被删除时，子控件会自动被删除。


### 信号

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

### 类型判定

o.isWidgetType()
o.inherits('QWidget')


### 对象删除

obj.deleteLater() 删除一个对象时，也会解除它与父对象之间的关系，而deleteLater并没有立即将对象销毁，而是向主消息循环发送了一个event, 下一次消息循环收到这个event之后才会销毁对象。它有两个后果：好处是可以在延迟删除的过程中完成一些操作，坏处是内存释放不及时。


### 事件处理

childEvent
customEvent
eventFilter
installEventFilter
removeEventFilter
event


### 定时器

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

## QWidget

所有可视控件的基类

每个控件都是矩形的，它们按照z轴顺序排列
控件由父控件和前面的控件裁剪（限制）
没有父控件的控件，称为窗口

### 控件的创建


### 大小位置

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


### 最大最小尺寸

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

### 内容边距

设置内容边距  setContentsMargins(左，上，右，下)
获取内容边距 getContentsMargins(左，上，右，下) 
获取内容区域 contentsRect()

注意是控件本身留够对应的大小

### 鼠标
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

### 事件消息
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

父子关系：
childAt(x,y) 获取在指定坐标的控件
parentWidget() 获取指定控件的父控件
childrenRect() 所有子控件组成的边界矩形


层级控制：
lower()将控件降低到最底层
raise_()将控件提升到最上层
a.stackUnder(b) 让a放在b 下面

图标i：
setWindowIcon() 设置图标
windowIcon()

标题：
setWindowTitle('标题')
windowTitle() 获取标题

不透明度：
setWindowOpacity(float)
windowOpacity() 获取透明度

窗口状态：
setWindowState():
	Qt.WindowNoState 无状态
	Qt.WindowMinimized 最小化
	Qt.WindowMaximized 最大化
	Qt.WindowFullScreen 全屏
	Qt.WindowActive 活动窗口
windowState() 获取状态

最大化最小化：
showFullScreen()
showMaximized()
showMinimized()
showNormal()
判定状态：
isMinimized()
isMaximized()
isFullScreen()

### 控件交互
是否可用：
setEnabled(bool) 设置控件禁用状态
isEnabled() 获取是否可用状态

显示与隐藏：
setVisible(bool)  对应的有setHidden(bool), show(), hide() 但其实都是调用setVisible(bool)
isHidden()
isVisible()
isVisibleTo(widget) 是否随widget显示而显示

注意：
visible 代表控件最终的状态，是否被我们所见(被其他控件遮挡也属于可见)
hide: 可理解为相对于父组件是否可见，隐藏的一定是不可见的，反之不一定成立


是否编辑：
setWindowModified(bool) 在标题中添加 "[*]"  编辑时会显示星号，否则不会显示
isWindowModified()

关闭：
setAttribute(Qt.WA_DeleteOnClose, True) 关闭时将控件删除
close() 关闭时只是不显示了，但控件没有被销毁。

状态提示：涉及到懒加载
statusTip()
setStatusTip(str) 当鼠标停留在窗口控件上时，在状态栏显示文本

工具提示：
toolTip()
setToolTip(str) 鼠标放在控件上一小段时间之后显示文本
	toolTipDuration()
	setToolTipDuration(msec)

焦点控件：
setFocus()
setFocusPolicy() 
	Qt.TabFocus
	Qt.ClickFocus
	Qt.StrongFocus  上面两种方式均可以获得焦点
	Qt.NoFocus 不能通过上面两种方式
clearFocus() 清空焦点

focusWidget() 获取子控件中当前聚集的控件
focusNextChild() 聚集下一个子控件
focusPreviousChild() 聚集上一个子控件
focusNextPrevChild(bool) 下一个：True，False:上一个
setTabOrder(pre_widget, next_widget) 设置获得焦点的顺序 
## AbstractButton
抽象类，无法直接使用，如果继承需要实现paint事件

### QPushButton

创建按钮:
QPushButton()
QPushButton(parent)
QPushButton(text, parent)
QPushButton(icon, text, parent)

菜单：
setMenu(QMenu) 设置菜单
menu() 获取菜单
showMenu() 显示菜单

边框是否保持扁平
setFlat(True) 扁平化，扁平化状态时其背景色不再绘制
isFlat()

默认：
setAutoDefault() 设置自动默认按钮，即选中状态
autoDefault()
setDefault()
isDefault() 


#### 信号： QPushButton 部分
继承自QAbstractButton:
- pressed()
- released()
- clicked()
- toggled()

继承自QWidget :
- WindowTitleChanged(QString)
- WindowIconChanged(QIcon)
- customContextMenuRequested(QPoint)

```python

class Window(QWidget):  
    def __init__(self):  
        super().__init__()  
        self.setWindowTitle("按钮的功能")  
        self.resize(500, 500)  
        self.setup_ui()  
  
    def setup_ui(self):  
        btn = QPushButton(self)  
        btn.setText("按钮")  
        btn.move(100, 100)  
  
        menu = QMenu()  
  
        new_action = QAction("新建", menu)  
        new_action.setShortcut("Ctrl+N")  
        # new_action = QAction(QIcon('a.png'),'文件',menu) 写在一行  
        new_action.triggered.connect(lambda: print("新建"))  # 添加对应的槽函数  
        menu.addAction(new_action)  # 添加到菜单  
  
        btn.setMenu(menu)
```

右键菜单

```python
from PyQt5.Qt import *  
  
  
class Window(QWidget):  
    def __init__(self):  
        super().__init__()  
        self.setWindowTitle("右键菜单")  
        self.resize(500, 500)  
        self.setup_ui()  
  
    def setup_ui(self):  
        pass  
  
    def contextMenuEvent(self, evt):  
        # 显示右键菜单，所以重写contextMenuEvent  
        menu = QMenu(self)  
        action1 = QAction("新建", menu)  
        action2 = QAction("打开", menu)  
        action3 = QAction("保存", menu)  
        menu.addAction(action1)  
        menu.addSeparator()  
        menu.addAction(action2)  
        menu.addAction(action3)  
        menu.exec_(evt.globalPos())  # 要用相对于屏幕的坐标，即全局坐标  
  
  
if __name__ == "__main__":  
    import sys  
  
    app = QApplication(sys.argv)  
  
    window = Window()  
    window.show()  
  
    sys.exit(app.exec_())
```

### QCommandLinkButton
创建命令链接按钮,类似单选按钮，在一组互斥按钮中选择一个。不应该单独使用，可以作为向导或者对话框中单选按钮的替代选项，与普通按钮的不同之处是，这允许描述性文本。

QCommandLinkButton(parent)
QCommandLinkButton(text, parent)
QCommandLinkButton(text,description, parent)

关于description:
setDescription(str)
description()

### QToolButton

提供快速访问功能，通常在工具栏内部。如果同时设置文本和图标，那么文本将不会显示。

- setText(str)
- setIcon(QIcon)
- setIconSize(QSize)
- setToolTip(str)

设置按钮风格：
setToolButtonStyle
- Qt.ToolButtonIconOnly  仅显示图标
- Qt.ToolButtonTextOnly  仅显示文字 
- Qt.ToolButtonTextBesideIcon 文本显示在图标旁边 
- Qt.ToolButtonTextUnderIcon 文本显示在图标下方
- Qt.ToolButtonFollowStyle 遵循风格

toolButtonStyle() 获取按钮风格

设置箭头：
setArrowType
- Qt.NoArrow 无箭头
- Qt.UpArrow 向上箭头
- Qt.DownArrow 向下箭头
- Qt.LeftArrow 向左箭头
- Qt.RightRrrow 向右箭头

arrowType() 获取箭头类型

自动提升：
setAutoRaise(bool) 在自动提升模式下，该按钮仅在鼠标指向它时才会绘制3D帧。
autoRaise()

菜单设置：

setMenu(QMenu)
menu()


setPopupMode
- QToolButton.delayedPopup  鼠标按住一会儿才显示
- QToolButton.MenuButtonPopup 有一个专门的指示箭头，点击箭头才显示
- QToolButton.InstantPopup  点按钮就显示，点击信号不会发射

popupMode() 


信号：
triggered()
当点击某个action时触发，并会将action传递出来。
Action 对象可以通过setData(Any) 绑定数据，data()获取数据


### QRadioButton

QRadioButton(parent)
QRadioButton(text, parent)

继承自QAbstractButton的方法如setIcon, setShortcut

### QButtonGroup
提供一个抽象的按钮容器，将多个按钮划分为一组。（不具体可视化效果）

addButton(QAbstractButton, id=-1)  添加按钮
buttons() 查看所有按钮组中的按钮
button(id ) 根据id获取对应按钮，如果没有则返回None
checkedButton() 获取选中的那个按钮
removeButton(QAbstractButton)  移除按钮，移除的按钮无法选择，但仍显示

setId(QAbstractButton, int) 为按钮设定id
id(QAbstractButton) 获取按钮的id, 不存在则返回-1
checkedId(QAbstractButton) 选中按钮的id,不存在则返回-1

setExclusive() 按钮组内按钮是否独占，如果False,则可以同时选则多个
exclusive() 独占设置的值

信号：
buttonClicked()  按钮被点击时
buttonPressed()  按钮被按下时
buttonReleased()  按钮被释放时
buttonToggled()  按钮被切换状态时

如果一个对象向外界提供的信号名称一样，但参数不一样，可以使用如下方式：
signal_name[type] 如buttonClicked[int].connect(click)  那么传递的就是int类型的数据如id

### QCheckBox

QCheckBox(parent)
QCheckBox(text,parent)
setIcon()
setShortcut()
setTristate(bool=True) 设置是否三态
isTristate()

setCheckState()
- Qt.Unchecked
- Qt.PartiallyChecked
- Qt.Checked
checkState()

信号：
stateChanged


## QLineEdit
纯键盘输入，单行文本编辑器。继承自QWidget

创建：
QLineEdit('text', parent)

文本设置与获取：
setText(str)  设置文本
insert(str) 光标处插入文本
text() 获取文本内容
displayText() 获取用户能看到的文本

输出模式：
setEchoMode(QLineEditEchoMode) 
- NoEcho
- Normal
- Password
- PasswordEchoOnEdit  编辑时明文，结束后密文

占位提示字符串：
setPlaceholderText(notice_str)
placeholderText()

清空按钮提示：
setClearButtonEnabled(bool)
isClearButtonEnabled()

添加操作行为：
addAction(QAction, QLineEdit.ActionPostion)
- QLineEdit.LeadingPosition 前面
- QLineEdit.TrailingPostion 后面
addAction(QIcon,QLineEditActionPostion)

自动补全：
setCompleter(QCompleter)
completer()


输入限制 ：
内容长度：
- setMaxLength(int) 最大输入长度
- maxLength()
只读限制：
- setReadOnly(bool)
- isReadOnly()
规则验证：
- setValidator(QValidator) 设置验证器
- setInputMask(mask_str) 掩码验证

验证器返回的状态有三种：
QValidator.Acceptable 验证通过
QValidator.Intermediate  中间状态,可以通过fixup再次处理
Qvalidator.Invalid 验证不通过

```python
from PyQt5.Qt import *  
  
  
class AgeValidator(QValidator):  
    def validate(self, input_str, pos_int):  
        print(input_str)  
        if 18 <= int(input_str) <= 60:  
            return QValidator.Acceptable, input_str, pos_int  
        elif 1 <= int(input_str) <= 17:  
            return QValidator.Intermediate, input_str, pos_int  
        else:  
            return QValidator.Invalid, input_str, pos_int  
  
    def fixup(self, p_str):  
        if p_str == "":  
            return "18"  
        elif int(p_str) < 18:  
            return "18"  
        else:  
            return p_str  
  
  
class Window(QWidget):  
    def __init__(self):  
        super().__init__()  
        self.setWindowTitle("")  
        self.resize(500, 500)  
        self.setup_ui()  
  
    def setup_ui(self):  
        le = QLineEdit(self)  
        le.move(100, 100)  
        av = AgeValidator()  
        le.setValidator(av)  
  
        le2 = QLineEdit(self)  
        le2.move(100, 200)  
        av2 = QIntValidator()  
        le2.setValidator(av2)  
  
  
if __name__ == "__main__":  
    import sys  
  
    app = QApplication(sys.argv)  
  
    window = Window()  
    window.show()  
  
    sys.exit(app.exec_())
```

内置的Validator:
- QIntValidator(bottom,top, parent)
- QDoubleValidator 浮点数数据限制，实际可能无效
- QRegExpValidator 通过正则表达式限制

hasAcceptableInput() 文本是否通过输入验证

掩码设置：
掩码指特定位置的特定类型，比如电话027-123 ip地址中的点

是否被编辑：主要用来标识文本内容是否被修改setModified(bool)
isModified()

光标控制：
cursorBackwark(bool mark, int steps)  向左移动int个字符， bool 决定是否带选中效果
cursorForward(bool, int steps)
cursorWordBackward(bool) 向左移动一个单词
cursorWordForward(bool)
home(bool) 移动到行首
end(bool) 移动到行尾
setCursorPosition(int)  设置光标位置
cursorPosition() 获取光标位置
cursorPositionAt(const QPoint & pos)

文本边距：
getTextMargins()
setTextMargins(int left, top ,right, bottom)

对齐方式：
setAlignment(Qt.Alignment)
水平：
- Qt.AlignLeft
- Qt.AlignRight
- Qt.AlignHCenter
- Qt.AlignJustify
垂直：
-  Qt.AlignTop
- Qt.AlignBottom
- Qt.AlignVCenter
- Qt.AlignBaseline
Qt.AlignCenter  垂直水平都居中

常用编辑功能：
backspace()  退格 
del_()
clear()
copy()
cut()
paste()
isUndoAvailable()、undo()
isRedoAvailable()、redo()
setDragEnabled(bool) 选中文本后是否可以拖拽

文本选中：
setSelection(start, length) 选中指定长度
selectAll()  全选
deselect() 取消已经选中的文本
hasSelectedText() 是否有选中文本
selectedText() 获取选中的文本
selectionStart() 选中的开始位置
selectionEnd() 
selectionLength() 选中的长度

信号：
textEdited 指的是用户编辑，而不是开发人员通过setText
textChanged 
returnPressed() 回车键被按下
editingFinished 按下回车，焦点切换会触发
cursorPositionChanged 光标位置改变
selectionChanged 选择文本发生改变

## QFrame
主要用来控制边框的效果

框架形状：
setFrameShape:
- QFrame.NoFrame
- QFrame.Box  围绕内容绘制一个框
- QFrame.Panel  绘制一个面板，使内凸起或凹陷
- QFrame.HLine  水平线
- QFrame.VLine  垂直线
- QFrame.StylePanel  矩形面板
- QFrame.WinPanel

frameShape() 

QAbstractScrollArea

设置滚动条：


滚动条策略：
setHorizontalScrollBarPolicy
setVerticalScrollBarPolicy()
horizontalScrollBarPolicy
verticalScrollBarPolicy()

## QTextEdit
文本编辑器

te = QTextEdit('text', parent)
setPlaceholderText()
placeholderText()
setPlainText()
insertPlainText()
toPlainText() 获取输入的文本内容
setHtml()
insertHtml()
toHtml()
append() 追加文本
textCursor() 获取文本光标

document() 通过文本光标，可以操作编辑文本文档对象，获取整个文档
QTextDocument

**后面操作的前提是要先获取到textCursor()对象**

插入图片：
insertImage(QTextImageFormat)
- setName('xxx.png')
- setWidth(20)
- setHeight(20)
insertImage(QTextImageFormat,QTextFrameFormat.Position)
insertImage(name_str)
insertImage(Qimage,name_str=None)

插入文件：
insertFragment
- fromHtml(html_str)
- fromPlainText(str)

插入列表
insertList(QTextListFormat) 在当前位置创建一个列表，返回列表
insertList(QTextListFormat.Style)
createList(QTextListFormat) 创建指定格式的列表，并且光标位于第一个列表项中
createList(QTextListFormat.style)

QTextListFormat:
- setIndent(int)
- setNumberPrefix(str)
- setNumberSuffix(str)
- setStyle(QTextListFormat_style)

QTextListFormat.Style:
- QTextListFormat.ListDisc  圆圈 
- QTextListFormat.ListCircle  空心圆 
- QTextListFormat.ListSquare  方块 
- QTextListFormat.ListDecimal  数字排列
- QTextListFormat.ListLowerAlpha 小写拉丁字符 
- QTextListFormat.ListUpperAlpha
- QTextListFormat.ListLowerRoman 小写罗马数字
- QTextListFormat.List UpperRoman 

table:
insertTable(5,3,QTextFrameFormat)  插入表格，5行3列
setAlignment(Qt.AlignRight)
setCellSpacing
setCellPadding
appendColumns(2) 追加两列
setColumnsWidthConstraints() 可以传多列宽度，中间可以传一个元组

插入文本块：
inserBlock() 空的文本块
inserBlock(QTextBlockFormat) 插入文本块同时，设置文本块格式
insertBlock(QTextBlockFormat, QTextCharFormat) 同时设置块格式的文本字符格式
setCharFormat()
mergeBlockCharFormat(QTextBlockFormat)
mergeBlockFormat(QTextBlockFormat)
mergeCharFormat(QTextFormat)
currentFrame() 获取当前所在的框架
currentList() 获取当前所在的 文本列表
currentTable() 获取当前的表格

setPosition(int pos, QTextCursor.MoveMode=MoveAnchor) 设置光标位置，需要反向设置回去
movePosition(QTextCursor.MoveOperation, QTextCursor.MoveMode=MoveAnchor, int n=1)
select(QTextCursor.SelectionType) 需要反向设置


信号：
textChange() 文本内容发生改变时，发射的信号
selectionChanged() 选中内容发生改变时
cursorPositionChanged 光标位置发生改变时
currentCharFormatChanged() 当前字符格式发生变化时
copyAvailable(bool yes) 复制可用时
redoAvailable(bool available) 重做可用时
undoAvailable(bool available) 撤销可用时