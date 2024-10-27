### 显示多条线

```python
import numpy as np
from matplotlib import pyplot as plt

# 设置字体样式用来显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 默认使用Unicode负号设置正常显示字符
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(-10,10)
y1 = x ** 2
y2 = x
plt.title("y=x^2", fontsize=16)
plt.xlabel("x轴", fontsize=12)
plt.ylabel("y轴")

plt.plot(x,y1)
plt.plot(x,y2)
```