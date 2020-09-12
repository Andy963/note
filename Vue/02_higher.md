
### filter and moment.js
```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">

</div>

</body>
<!--import-->
<script src="../Vue.js"></script>
<script src="../moment.js"></script>
<script>
    // 全局过滤器
    Vue.filter('myTimeFilter', function (val, formatStr) {
        return moment(val).format(formatStr);
    })

    // init a object
    let App = {
        data() {
            return {
                msg: 'hello world',
                now: new Date()
            }
        },
        template: `
        <div>我是app,反转后的hello world ==> {{ msg | reverseWorld }}
        <h2>{{ now | formatTime('YYYY-MM-DD') }}</h2>
        </div>
        `,
        filters: {
            reverseWorld: function (val) {
                console.log(val);
                return val.split('').reverse().join('');
            },
            formatTime: function (val, formatStr) {
                return moment(val).format(formatStr);
            }
        }
    }
    new Vue({
        el: '#app',
        // bind data
        data: {},
        template: `
        <div>
        <App></App>
        </div>
        `,
        components: {
            App
        }
    })
</script>
</html>
```