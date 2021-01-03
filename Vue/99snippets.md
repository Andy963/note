### show html but not source code
```js
   show_html(str) {
                return marked(str
                    .replace(str ? /&(?!#?\w+;)/g : /&/g, '&amp;')
                    .replace(/&lt;/g, "<")
                    .replace(/&gt;/g, ">")
                    .replace(/&quot;/g, "\"")
                    .replace(/&#39;/g, "\\'"))
            },
```