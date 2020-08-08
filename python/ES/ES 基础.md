
### 基本操作：
```
#添加数据
PUT a1/doc/1
{
  "name":"andy",
  "age":16
}

# 再次添加,因为用的同一个索引，所以会修改前面插入的数据
PUT a1/doc/1
{
  "name":"andy jack",
  "age":18
}

PUT a1/doc/2
{
  "name":"andy",
  "age":16
}

#获取数据
GET a1/doc/1

{
  "_index" : "a1",
  "_type" : "doc",
  "_id" : "1",
  "_version" : 2,
  "_seq_no" : 1,
  "_primary_term" : 1,
  "found" : true,
  "_source" : {
    "name" : "andy jack",
    "age" : 18
  }
}

#获取所有数据
GET a1/doc/_search
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 2,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "a1",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "name" : "andy",
          "age" : 16
        }
      },
      {
        "_index" : "a1",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "name" : "andy jack",
          "age" : 18
        }
      }
    ]
  }
}

#删除数据
DELETE a1/doc/2
{
  "_index" : "a1",
  "_type" : "doc",
  "_id" : "2",
  "_version" : 2,
  "result" : "deleted",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 1,
  "_primary_term" : 1
}

GET a1/doc/_search
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 1,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "a1",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "name" : "andy jack",
          "age" : 18
        }
      }
    ]
  }
}

# 查询所有索引
GET _cat/indices/?v
health status index                uuid                   pri rep docs.count docs.deleted store.size pri.store.size
yellow open   a1                   jmrwzYLeQWuxS-YlkF1NqQ   5   1          1            0      4.7kb          4.7kb
green  open   .kibana_1            AOPzLpBATDaJHLCyGnv9fg   1   0          4            0     17.2kb         17.2kb
green  open   .kibana_task_manager fqYdzvyaR3OLrSznlSFYCQ   1   0          2            0     12.5kb         12.5kb

#查看索引是否存在，返回状态码
HEAD a1
```

### 两种查询方式

**url**
```
GET a1/_search/?q=age:18
{
  "took" : 18,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 1,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "a1",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "name" : "andy jack",
          "age" : 18
        }
      }
    ]
  }
}
```

**结构化查询**
```
GET a1/_search
{
  "query": {
    "match": {
      # age是字段名，18是值
      "age": "18"
    }
  }
}

#添加数据
PUT a1/doc/3
{
  "name":"Mary",
  "desc":["可爱","漂亮"]
}

PUT a1/doc/4
{
  "name":"Amy",
  "desc":["可爱","乖巧","阳光"]
}

#查询
GET a1/doc/_search
{
  "query": {
    "match": {
        "desc":"可 漂"
    }
  }
}
#这种情况下Es会对"可 漂" 做分词
{
  "took" : 5,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 2,
    "max_score" : 0.5753642,
    "hits" : [
      {
        "_index" : "a1",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 0.5753642,
        "_source" : {
          "name" : "Mary",
          "desc" : [
            "可爱",
            "漂亮"
          ]
        }
      },
      {
        "_index" : "a1",
        "_type" : "doc",
        "_id" : "4",
        "_score" : 0.2876821,
        "_source" : {
          "name" : "Amy",
          "desc" : [
            "可爱",
            "乖巧",
            "阳光"
          ]
        }
      }
    ]
  }
}

# 查某个具体的词
GET a1/doc/_search
{
  "query": {
    "match_phrase": {
        "desc":"可爱"
    }
  }
}

{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 2,
    "max_score" : 0.5753642,
    "hits" : [
      {
        "_index" : "a1",
        "_type" : "doc",
        "_id" : "4",
        "_score" : 0.5753642,
        "_source" : {
          "name" : "Amy",
          "desc" : [
            "可爱",
            "乖巧",
            "阳光"
          ]
        }
      },
      {
        "_index" : "a1",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 0.5753642,
        "_source" : {
          "name" : "Mary",
          "desc" : [
            "可爱",
            "漂亮"
          ]
        }
      }
    ]
  }
}

# 间隔词
PUT a1/doc/1
{
  "title":"中国是世界上最的国家"
}
#直接查中国世界是查不到的，因为它们中间隔了一个"是"字，指定slop就可以查到了
GET a1/doc/_search
{
  "query": {
    "match_phrase": {
      "title": {
        "query": "中国世界",
        "slop":1
      }
    }
  }
}

```

### 排序
```
# 查desc中含有"可爱"的，然后近id倒序排列
GET a1/doc/_search
{
  "query": {
    "match": {
      "desc": "可爱"
    }
  },
  "sort": [
    {
      "_id": {
        "order": "desc"
      }
    }
  ]
}
```

### 高亮
默认添加em标签
```
GET a1/doc/_search
{
  "query": {
    "match": {
      "desc": "可爱"
    }
  },
  "highlight": {
    "fields": {
      "desc":{}
    }
  }
}

{
  "took" : 2,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 2,
    "max_score" : 0.5753642,
    "hits" : [
      {
        "_index" : "a1",
        "_type" : "doc",
        "_id" : "4",
        "_score" : 0.5753642,
        "_source" : {
          "name" : "Amy",
          "desc" : [
            "可爱",
            "乖巧",
            "阳光"
          ]
        },
        "highlight" : {
          "desc" : [
            "<em>可</em><em>爱</em>"
          ]
        }
      },
      {
        "_index" : "a1",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 0.5753642,
        "_source" : {
          "name" : "Mary",
          "desc" : [
            "可爱",
            "漂亮"
          ]
        },
        "highlight" : {
          "desc" : [
            "<em>可</em><em>爱</em>"
          ]
        }
      }
    ]
  }
}

# 自定义标签，并添加样式
GET a1/doc/_search
{
  "query": {
    "match": {
      "desc": "可爱"
    }
  },
  "highlight": {
    "pre_tags": "<b style='color:red;'>", 
    "post_tags": "</b>", 
    "fields": {
      "desc":{}
    }
  }
}

# 加样式

```