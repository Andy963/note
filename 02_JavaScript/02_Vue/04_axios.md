
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

### axios instance
```js
/*
axios.create(config)
1. 根据指定配置创建一个axios
2.新axios没有取消请求和批量发送请求的方法，其它所有语法都一样
3.设计是为了部分接口有不同配置考虑
 */

axios.defaults.baseURL ='http://localhost:3000'
//使用axios发请求
axios({
    url:'/posts', //默认的3000端口
})
// 如果有另一个请求需要请求4000端口

const instance = axios.create({
    baseURL : 'http://localhost:4000'
})

// instance({
//     url: '/comments/1'
// })

instance.get('/comments/1') // 从端口4000获取请求

/*
为了区分不同配置，而不用每个请求都指定配置
上面的axios 可以指定一些通用的配置
而instance 又指定另一套配置
 */
```
### axios interceptor
```js
// 添加请求拦截器
// 请求拦截器后添加，先执行
// 请求拦截器必须返回 config,向下传递
axios.interceptors.request.use(
    config => {
        console.log('request  interceptors1 onResolved()');
        return config;
    },
    error => {
        console.log('request interceptors1 onRejected()');
        return config
    }
)

axios.interceptors.request.use(
    config => {
        console.log('request  interceptors2 onResolved()');
        return config;
    },
    error => {
        console.log('request interceptors2 onRejected()');
        return config
    }
)

// 添加响应拦截器
// 响应拦截器先添加先执行
// 响应拦截器必须返回response
axios.interceptors.response.use(
    response => {
        console.log('response interceptors1 onResolved()');
        return response
    },
    function (error) {
        console.log('response interceptors1 onRejected()')
        return Promise.reject(error);
    }
)

axios.interceptors.response.use(
    response => {
        console.log('response interceptors2 onResolved()');
        return response
    },
    function (error) {
        console.log('response interceptors2 onRejected()')
        return Promise.reject(error);
    }
)

axios.get('http://localhost:3000/posts')
    .then(res => {
        console.log('data', res.data);
    })
    .catch(err => {
        console.log('err', err.msg);
    })
```
### axios cancel

```js
axios.defaults.baseURL = 'http://localhost:3000';

function getProducts1() {
    axios({
        url: '/products1'
    }).then(
        response => {
            console.log('请求1成功', response.data);
        }
    )
}

let cancel = '';// 用于保存取消请求的函数
function getProducts2() {
    // 在准备发送新的请求前，取消未完成的请求
    if (typeof cancel === 'function') {
        cancel('取消请求')
    }
    axios({
        url: '/products2',
        cancelToken: new axios.CancelToken((f) => { // f是用于取消当前请求的函数
            // 保存取消函数，用于之后可能需要取消当前请求
            cancel = f;
        })
    }).then(
        response => {
            cancel = null; //如果成功了清空函数，无法取消
            console.log('请求2成功', response.data);
        },
        error => {
            // 一旦取消请求，request即失败了
            cancel = null; //如果失败了也清空，无法取消
            console.log(error)
        }
    )
}

function cancelReq() {
    // 执行取消请求的函数
    if (typeof cancel === 'function') {
        cancel('强制取消请求');
    } else {
        console.log('没有可取消的请求');
    }
}
```

### axios cancel with interceptor
```js
axios.defaults.baseURL = 'http://localhost:3000';


// 添加请求拦截器
axios.interceptors.request.user((config) => {
    // 在准备发送新的请求前，取消未完成的请求
    if (typeof cancel === 'function') {
        cancel('取消请求')
    }
    // 添加一个cancelToken的配置
    config.cancelToken = new axios.CancelToken((f) => { // f是用于取消当前请求的函数
        // 保存取消函数，用于之后可能需要取消当前请求
        cancel = f;
    })
    return config
})

// 添加响应拦截器
axios.interceptors.response.use(
    (response) => {
        cancel = null; //如果成功了清空函数，无法取消
        return response;
    },
    error => {
        if (axios.isCancel(error)) {
            // 如果是取消请求的错误，不能将cancel置空，否则后续的取消将无法执行
            console.log("请求取消的错误", error.message);
            return new Promise(() => {
            })
        } else {
            console.log(error)
            cancel = null; //如果失败了也清空，无法取消
            // 将错误向下传递
            // 一旦取消请求，request即失败了
            // throw error;
            return Promise.reject(error);

        }
    })

function getProducts1() {
    axios({
        url: '/products1'
    }).then(
        response => {
            console.log('请求1成功', response.data);
        }
    )
}

let cancel = '';// 用于保存取消请求的函数
function getProducts2() {
    axios({
        url: '/products2',
    }).then(
        response => {
            console.log('请求2成功', response.data);
        },
        error => {
            // 只处理请求失败的情况，取消请求的错误不用处理
            console.log(error)
        }
    )
}

function cancelReq() {
    // 执行取消请求的函数
    if (typeof cancel === 'function') {
        cancel('强制取消请求');
    } else {
        console.log('没有可取消的请求');
    }
}
```

### use axios request
#### basic
axios.request(config)
```js
//原始的Axios请求方式
axios({
  method: 'post',
  url: '/user/12345',
  data: {
    firstName: 'Fred',
    lastName: 'Flintstone'
  },
  timeout: 1000,
  ...//其他相关配置
});
```

#### get 
axios.get(url[, config])
```js
axios.get('demo/url', {
    params: {
        id: 123,
        name: 'Henry',
    },
   timeout: 1000,
  ...//其他相关配置
})
```
### delete
axios.delete(url[, config])
```js
//如果服务端将参数作为java对象来封装接受
axios.delete('demo/url', {
    data: {
        id: 123,
        name: 'Henry',
    },
     timeout: 1000,
    ...//其他相关配置
})
//如果服务端将参数作为url参数来接受，则请求的url为:www.demo/url?a=1&b=2形式
axios.delete('demo/url', {
    params: {
        id: 123,
        name: 'Henry',
    },
     timeout: 1000,
    ...//其他相关配置
})
```

#### post
axios.post(url[, data[, config]])
```js
axios.post('demo/url', {
    id: 123,
    name: 'Henry',
},{
   timeout: 1000,
    ...//其他相关配置
})
```

#### put
axios.put(url[, data[, config]])
```js
axios.put('demo/url', {
    id: 123,
    name: 'Henry',
},{
   timeout: 1000,
    ...//其他相关配置
})
```

#### patch
axios.patch(url[, data[, config]])
```js
axios.patch('demo/url', {
    id: 123,
    name: 'Henry',
},{
   timeout: 1000,
    ...//其他相关配置
})
```
ref:https://www.jianshu.com/p/53deecb09077
使用时习惯使用原始的方式，如果指定方法还得指定参数，其中get,delete是不同情况，需要指定data || params, 而其它方法则是url +json + other config