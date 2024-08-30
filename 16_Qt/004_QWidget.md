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