# ajax

### ajax请求参数


data
>data: //当前ajax请求要携带的数据，是一个json的object对象，ajax方法就会默认地把它编码成某种格式(urlencoded:?a=1&b=2)发送给服务端；此外，ajax默认以get方式发送请求。

processData:
>processData：声明当前的data数据是否进行转码或预处理，默认为true，即预处理；if为false，那么对data：{a:1,b:2}会调用json对象的toString()方法，即{a:1,b:2}.toString(),最后得到一个［object，Object］形式的结果。

contentType
>contentType：默认值: "application/x-www-form-urlencoded"。发送信息至服务器时内容编码类型。用来指明当前请求的数据编码格式；urlencoded:?a=1&b=2；如果想以其他方式提交数据，比如contentType:"application/json"，即向服务器发送一个json字符串.注意：contentType:"application/json"一旦设定，data必须是json字符串，不能是json对象               

traditional
>traditional：一般是我们的data数据有数组时会用到 ：data:{a:22,b:33,c:["x","y"]},traditional为false会对数据进行深层次迭代；

dataType：
>预期服务器返回的数据类型,服务器端返回的数据会根据这个值解析后，传递给回调函数。默认不需要显性指定这个属性，ajax会根据服务器返回的content Type来进行转换；比如我们的服务器响应的content Type为json格式，这时ajax方法就会对响应的内容.进行一个json格式的转换，if转换成功，我们在success的回调函数里就会得到一个json格式的对象；转换失败就会触发error这个回调函数。如果我们明确地指定目标类型，就可以使用data Type。dataType的可用值：html｜xml｜json｜text｜script
