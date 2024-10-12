## 009_ionic

使用步骤
```sh
# 安装脚手架
npm i -g ionic
# 用脚手架创建项目
ionic start p_name
```
进入项目目录，启动开发服务器: `ionic serve`

app.component.html

```html
<ion-app> <!--保证始终铺满全民的容器 -->
  <ion-header>
    <ion-toolbar>
      <ion-title>标题</ion-title>
    </ion-toolbar>
  </ion-header>
  <ion-content>

  </ion-content>
  <ion-footer>
    <ion-toolbar>
      <ion-title>底部</ion-title>
    </ion-toolbar>
  </ion-footer>
  <ion-router-outlet></ion-router-outlet>
</ion-app>
```

特点：
1.列可以不指定宽度占比，在一行中的多个列的宽度会平均分配，一行中列的数量取决于屏幕宽度。
2.可以使用size属性指定一列的宽度占比一一总分为12；6就是6/12， 4就是4／12
3.可以使用offset（偏移量）属性指定一列向右偏移指定的宽度,底层是用margin-left实现的，故会影响当前列及后续的列
4.可以使用push(向右推）和pull向左拉）属性调整一列的出现位置，底层是用绝对定位实现的，故不会影响同一行的其它列。

考虑到短期不会用到本框架，真到用时估计已经忘记了，故暂停后面的视频学习