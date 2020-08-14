### 批量写入

```python
import time
from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch()

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print('共耗时约 {:.2f} 秒'.format(time.time() - start))
        return res
    return wrapper
    
@timer
def batch_data():
    """ 批量写入数据 """
    for i in range(1, 100001, 1000):
        action = (
        {
            "_index": "s2",
            "_type": "doc",
            "_source": {
                "title": k
            }
        } for k in range(i, i + 1000))
        helpers.bulk(es, action)


@timer
def gen():
    """ 使用生成器批量写入数据 """
    action = ({
        "_index": "s2",
        "_type": "doc",
        "_source": {
            "title": i
        }
    } for i in range(100000))
    helpers.bulk(es, action)

if __name__ == '__main__':
    # create_data()
    batch_data()
```