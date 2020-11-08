
### XHR API

1. XMLHttpResponse(); create XHR object function
2. status: response status code, like 200,404
3. statusText: response text
4. readyState: status of request status 
    0. 0  初始
    1. open()之后
    2. send()之后
    3. 请求中
    4. 请求完成 

5. onreadystatechange:绑定readyState改变的临川
6. respnseType:指定响应数据类型，如果是'json‘得到响应后会自动解析 响应体数据
7. response 响应体数据，类型取决于responseType
8. timeout:指定请求超时时间，默认0代表无限制
9. ontimeout:绑定超时时的监听
10. onerror:绑定请求错误的监听
11. open() 初始化一个请求,参数为method,url, async
12. send(data): 发送请求
13. abort();中断请求
14. getResponseHeader(name); 获取指定名称的响应头值
15. getAllResponseHeader():获取所有响应头组成的字符串
16. setRequestHeader(name,value);设置请求头

### 用XHR封装axios函数

#### 发送请求：
```js
function axios({
                   url,
                   method = 'GET',
                   params = {},
                   data = {},

               }) {
    // 返回一个promise对象
    return new Promise((resolve, reject) => {
        // 执行异步ajax请求
        // 创建 xhr对象
        const request = new XMLHttpRequest();
        // 打开连接（初始化对象，没有请求)
        request.open(method, url, true)
        // 发送请求
        request.send()
        //2.1 如果成功了，调用resolve()
        // 2.2如果请求失败了，调用reject()
    })

}
```
#### 发送POST数据
```js
function axios({
                   url,
                   method = 'GET',
                   params = {},
                   data = {},

               }) {
    // 返回一个promise对象
    return new Promise((resolve, reject) => {
        // 执行异步ajax请求
        // 创建 xhr对象
        const request = new XMLHttpRequest();
        // 打开连接（初始化对象，没有请求)
        request.open(method, url, true)
        // 发送请求
        if (method === 'GET') {
            request.send();
        } else if (method === 'POST') {
            request.setRequestHeader('Content-Type', 'application/json;charset=utf-8');
            request.send(JSON.stringify({data})); // json 格式， 一旦发json格式数据要加请求头
        }
        //2.1 如果成功了，调用resolve()
        // 2.2如果请求失败了，调用reject()
    })

}
```
#### 发送GET数据
```js
function axios({
                   url,
                   method = 'GET',
                   params = {},
                   data = {},

               }) {
    // 返回一个promise对象
    return new Promise((resolve, reject) => {
        // 执行异步ajax请求
        // 创建 xhr对象
        const request = new XMLHttpRequest();

        // 处理query 参数 拼接到url上 id=1&name=zhou
        /*
        {
          id:1,
          name:'zhou'
         }
         */
        let queryString = '';
        Object.keys(params).forEach(key => {
            queryString += `${key}=${params[key]}&`;
        })
        if (queryString) {
            // 去掉最后面的&
            queryString = queryString.substring(0, queryString.length - 1);
            // 接到url上
            url += "?" + queryString;
        }
        // 打开连接（初始化对象，没有请求)
        request.open(method, url, true)
        // 发送请求
        if (method === 'GET') {
            request.send();
        } else if (method === 'POST') {
            request.setRequestHeader('Content-Type', 'application/json;charset=utf-8');
            request.send(JSON.stringify({data})); // json 格式， 一旦发json格式数据要加请求头
        }
        //2.1 如果成功了，调用resolve()
        // 2.2如果请求失败了，调用reject()
    })

}
```

#### 处理响应
```js
function axios({
                   url,
                   method = 'GET',
                   params = {},
                   data = {},

               }) {
    // 返回一个promise对象
    return new Promise((resolve, reject) => {
        // 执行异步ajax请求
        // 创建 xhr对象
        const request = new XMLHttpRequest();

        // 处理query 参数 拼接到url上 id=1&name=zhou
        /*
        {
          id:1,
          name:'zhou'
         }
         */
        let queryString = '';
        Object.keys(params).forEach(key => {
            queryString += `${key}=${params[key]}&`;
        })
        if (queryString) {
            // 去掉最后面的&
            queryString = queryString.substring(0, queryString.length - 1);
            // 接到url上
            url += "?" + queryString;
        }
        // 打开连接（初始化对象，没有请求)
        request.open(method, url, true)
        // 发送请求
        if (method === 'GET') {
            request.send();
        } else if (method === 'POST') {
            request.setRequestHeader('Content-Type', 'application/json;charset=utf-8');
            request.send(JSON.stringify({data})); // json 格式， 一旦发json格式数据要加请求头
        }
        request.onreadystatechange = function () {
            // 如果请求没有完成，直接结束
            if (request.readyState !== 4) {
                return
            }
            // 如果响应状态码在[200,300)之间代表成功，否则失败
            const {status, statusText} = request
            //2.1 如果成功了，调用resolve()
            if (status >= 200 && status <= 299) {
                // 准备结果数据对象response
                const response = {
                    data: JSON.parse(request.response),
                    status,
                    statusText
                }
                resolve(response)
            } else {
                // 2.2如果请求失败了，调用reject()
                reject(new Error('request error status is' + status));
            }
        }

    })

}
```

### axios使用
```js
//不同请求不同使用方式：对象/函数
axios.defaults.baseURL = 'http://localhost:3000';


// GET请求
function testGet() {
    axios.get('http://localhost:3000/posts?id=1')
        .then(res => {
            console.log('/posts get', res.data);
        })
    // 函数的方式
    axios({
        url: '/posts',
        params: {
            id: 1
        }
    }).then(res => {
        console.log('/posts get', res.data);
    })
}

// POST请求
// 在axios中如果data为对象类型，axios默认发json格式
function testPost() {
    axios.post('http://localhost:3000/posts', {"name": "zhou"})
        .then(res => {
            console.log('/posts post', res.data);
        })
    // 函数的方式
    axios({
        method: 'POST',
        url: '/posts',
        data: {
            name: "zhou"
        }
    }).then(res => {
        console.log('/posts post', res.data);
    })
}

// PUT请求
// 在axios中如果data为对象类型，axios默认发json格式
function testPut() {
    axios.put('http://localhost:3000/posts/1', {"name": "zhou"})
        .then(res => {
            console.log('/posts put', res.data);
        })
    // 函数的方式
    axios({
        method: 'PUT',
        url: '/posts/1',
        data: {
            name: "zhou"
        }
    }).then(res => {
        console.log('/posts put', res.data);
    })
}

// DELETE请求
// 在axios中如果data为对象类型，axios默认发json格式
function testDelete() {
    axios.put('http://localhost:3000/posts/1')
        .then(res => {
            console.log('/posts delete', res.data);
        })
    // 函数的方式
    axios({
        method: 'DELETE',
        url: '/posts/1',

    }).then(res => {
        console.log('/posts delete', res.data);
    })
}
```