## QAbstractButton

抽象类，无法直接使用，如果继承需要实现paint事件


## QPushButton




快捷键设置:
```python
# 快捷键设定  
# 第一种方式：通过&符号  
btn2 = QPushButton(window)  
btn2.move(100, 200)  
btn2.pressed.connect(lambda: print("btn被按下了"))  
  
btn2.setText("ab&c")  # 此时按下alt+c 就触发了按下事件  
  
# 当没有字符串时，则需要通过组合设置  
btn2.setShortcut("Alt+b")
```

setAutoRepeat(bool) 设置自动重复，即按住不放时自动重复
setAutoRepeatInterval(msec) 设置自动重复的间隔
setAutoRepeatDelay(msec) 设置自动重复的延时，即等一段时间后开始自动重复
autoRepeat()
autoRepeatInterval()
autoRepeatDelay()

状态：
isDown() 是否按下
setDown(bool) 设置按下，点下去还没松手的状态

isChecked() 是否选中了按钮
setChecked(bool) 设置选中按钮
toggle() 在选与非选中间切换
isCheckable() 是否可以设置选中
setCheckable() 设置是否可以选中

```python
btn.setStyleSheet("QPushButton:pressed {background-color:red}” )

# 这里的press 类似于前端中的伪类
```

排他性：
如果同时存在多个按钮，如果所有按钮设置了排他性，那么在同一时刻只有一个按钮可以被选中。
autoExclusive() 自动排他性
setAutoExclusive() 设置自动排他

点击：
click() 普通点击
animationClick(msec)  带动画效果的点击


hitButton() 返回True时，当用户点击按钮时会产生信号，并根据信号响应，而如果返回False,则不会产生信号响应

信号：
pressed() 鼠标按下
released() 控件内松开鼠标或者移出 控件范围松开鼠标
click() 控件内按下+控件内松开
toggled() 切换信号，一般在单选或者多选中使用
## QRadioButton



## QCheckBox



## QToolButton