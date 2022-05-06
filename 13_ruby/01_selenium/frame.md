## frames
```html
<div id="modal">
  <iframe id="buttonframe"name="myframe"src="https://seleniumhq.github.io">
   <button>Click here</button>
 </iframe>
</div>
```

```ruby
# 这不会工作
driver.find_element(:tag_name,'button').click
```

### 使用iframe并切换
```ruby
# Store iframe web element
iframe = driver.find_element(:css,'#modal> iframe')

### 切换到 frame
driver.switch_to.frame iframe

# 单击按钮
driver.find_element(:tag_name,'button').click
  
```
### 如果frame有id 或者name
```ruby
# Switch by ID
driver.switch_to.frame 'buttonframe'

# 单击按钮
driver.find_element(:tag_name,'button').click
  
```
### 使用索引
```ruby
# 基于索引切换到第 2 个 iframe
iframe = driver.find_elements_by_tag_name('iframe')[1]

# 切换到选择的 iframe
driver.switch_to.frame(iframe)
```
### 离开
```ruby
# 回到顶层
driver.switch_to.default_content
```
