## BOM
Browser object model

### window对象 
所有浏览器都支持 window 对象。 
- 概念上讲.一个html文档对应一个window对象. 
- 功能上讲: 控制浏览器窗口的. 
- 使用上讲: window对象不需要创建对象,直接使用即可. 

#### method
alert()            显示带有一段消息和一个确认按钮的警告框。 
confirm()          显示带有一段消息以及确认按钮和取消按钮的对话框。 
prompt()           显示可提示用户输入的对话框。 
open()             打开一个新的浏览器窗口或查找一个已命名的窗口。 
close()            关闭浏览器窗口。 
setInterval()      按照指定的周期（以毫秒计）来调用函数或计算表达式。 
clearInterval()    取消由 setInterval() 设置的 timeout。 
setTimeout()       在指定的毫秒数后调用函数或计算表达式。 
clearTimeout()     取消由 setTimeout() 方法设置的 timeout。 
scrollTo()         把内容滚动到指定的坐标。 

alert confirm prompt以及open函数 
```
var result = confirm("您确定要删除吗?");
alert(result); 

//prompt 参数1 : 提示信息. 参数2:输入框的默认值. 返回值是用户输入的内容.
// var result = prompt("请输入一个数字!","haha");
// alert(result);

open方法 打开和一个新的窗口 并 进入指定网址.参数1 : 网址.
//调用方式1
//open("http://www.baidu.com");
参数1 什么都不填 就是打开一个新窗口. 参数2.填入新窗口的名字(一般可以不填). 参数3: 新打开窗口的参数.
open('','','width=200,resizable=no,height=100'); // 新打开一个宽为200 高为100的窗口
//close方法 将当前文档窗口关闭.
//close();
```

