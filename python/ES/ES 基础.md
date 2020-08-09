
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

### 分页
```
GET a1/doc/_search
{
  "query": {
    "match_all": {}
  },
  "from":0,
  "size":2
}
```

### must should
**准备数据**
```
PUT ms/doc/1
{
  "name":"andy",
  "age":30,
  "from": "hb",
  "desc": "皮肤黑、性格直",
  "tags": ["黑", "长", "直"]
}

PUT ms/doc/2
{
  "name":"Amy",
  "age":18,
  "from":"hn",
  "desc":"肤白貌美，娇憨可爱",
  "tags":["白", "富","美"]
}

PUT ms/doc/3
{
  "name":"jack",
  "age":22,
  "from":"hb",
  "desc":"mmp，没怎么看，不知道怎么形容",
  "tags":["造数据", "真","难"]
}

PUT ms/doc/4
{
  "name":"lili",
  "age":29,
  "from":"bj",
  "desc":"健美 运行",
  "tags":["苗条", "美"]
}

PUT ms/doc/5
{
  "name":"Andrew",
  "age":25,
  "from":"hebei",
  "desc":"强壮 跑酷",
  "tags":["高大","威猛"]
}
```
**查询所有湖北（hb)的人
```
GET ms/doc/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "from": "hb"
          }
        }
      ]
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
    "max_score" : 0.2876821,
    "hits" : [
      {
        "_index" : "ms",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 0.2876821,
        "_source" : {
          "name" : "andy",
          "age" : 30,
          "from" : "hb",
          "desc" : "皮肤黑、性格直",
          "tags" : [
            "黑",
            "长",
            "直"
          ]
        }
      },
      {
        "_index" : "ms",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 0.2876821,
        "_source" : {
          "name" : "jack",
          "age" : 22,
          "from" : "hb",
          "desc" : "mmp，没怎么看，不知道怎么形容",
          "tags" : [
            "造数据",
            "真",
            "难"
          ]
        }
      }
    ]
  }
}
```
**来自hb,并且年龄为30岁的
```
GET ms/doc/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "from": "hb"
          }
        },
        {
            "match":{
              "age":30
            }
          }
      ]
    }
  }
}
```

** 来自湖北的或者北京的 should**
```
GET ms/doc/_search
{
  "query": {
    "bool": {
      "should": [
        {
          "match": {
            "from": "hb"
          }
        },
        {
          "match": {
            "from": "bj"
          }
        }
      ]
    }
  }
}
```

**不是湖北的，年龄也不是30岁的
```
GET ms/doc/_search
{
  "query": {
    "bool": {
      "must_not": [
        {
          "match":{
            "from":"hb"
          }
        },
        {
          "match":{
            "age":30
          }
        }
      ]
    }
  }
}
```
**filter**
前面一直是某个条件等于，那么要大于/小于怎么办呢？
来自湖北，且年龄在20-30之间。
```
GET ms/doc/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "from": "hb"
          }
        }
      ],
      "filter": {
        "range": {
          "age": {
            "gte": 20,
            "lte": 30
          }
        }
      }
    }
  }
}
```

### _source
默认情况下，会把所有字段都查出来，但如果我们只需要其中几个字段呢？指定_source
```
GET ms/doc/_search
{
  "query": {
    "bool":{
      "must": [
        {
          "match": {
            "from": "hb"
          }
        }
      ]
    }
  }
  , "_source": ["name","age"]
}

```