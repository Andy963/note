## CURD
Create,Update,Retrieve,Delete
### Create
```
POST /my_index/_doc/1
{
  "name":"Amy",
  "age":19
}

POST /my_index/_doc/2
{
  "name":"jack",
  "age":18
}

```

### Update
```
GET /my_index/_search
{
  "took" : 268,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "name" : "Amy",
          "age" : 19
        }
      },
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "name" : "jack",
          "age" : 18
        }
      }
    ]
  }
}

```
**将Amy 更改为amy
这里使用POST请求，按restful接口中post为create,但此处配合_update
```
POST /my_index/_update/1
{
  "doc":{
      "name":"amy",
      "age":19
  }
}
```
### Retrieve
```
{
  "took" : 295,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "name" : "jack",
          "age" : 18
        }
      },
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "name" : "Amy",
          "age" : 19
        }
      }
    ]
  }
}

```

### Delete
```
DELETE /my_index/_doc/1

GET /my_index/_search
{
  "took" : 995,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "name" : "jack",
          "age" : 18
        }
      }
    ]
  }
}

```
### Retrieve url

#### url params
```
GET /my_index/_search/?q=age:19
{
  "took" : 11,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 0,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  }
}
```

#### match
```
GET /my_index/_search
GET /my_index/_search
{
  "query": {
    "match": {
      # age是字段名，18是值
      "age": "18"
    }
  }
}
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "my_index",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "name" : "jack",
          "age" : 18
        }
      }
    ]
  }
}
#添加数据
PUT /my_index/_doc/3
{
  "name":"Mary",
  "desc":["可爱","漂亮"]
}

PUT /my_index/_doc/4
{
  "name":"Amy",
  "desc":["可爱","乖巧","阳光"]
}

#查询
GET /my_index/_search
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
```
#### match_all
```
GET /my_index/_doc/_search
{
  "query": {
    "match_all": {}
  }
}
# match_all后面的条件为空，相当于select * from table;
```
#### match_phrase
```
# 查某个具体的词
GET /my_index/_search
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
PUT /my_index/_doc/1
{
  "title":"中国是世界上最的国家"
}
#直接查中国世界是查不到的，因为它们中间隔了一个"是"字，指定slop就可以查到了
GET /my_index/_search
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

#### match_phrase_prefix
最左前缀查询
```python
GET /my_index/_search
{
  "query": {
    "match_phrase_prefix": {
      "name": "M"
    }
  }
}
#output
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
    "total" : 1,
    "max_score" : 0.2876821,
    "hits" : [
      {
        "_index" : "a1",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 0.2876821,
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
```
结果就是将M开头的名字选出来了，但使用前缀查询会非常消耗性能，最好对结果进行限制：max_expansions
```
GET /my_index/_search
{
  "query": {
    "match_phrase_prefix": {
      "name": {
        "query": "A",
        "max_expansions": 1
      }
    }
  }
}
```
#### multi_match
多字段查询：
我们可以通过must来限定多个字段,但如果字段太多，这样就比较麻烦
```
GET /my_index/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "name": "Amy"
          }
        },
        {
          "match": {
            "desc": "可爱"
          }
        }
      ]
    }
  }
}
```
使用multi_match
```
PUT /my_index/_doc/4 
{
  "name":"Amy",
  "desc":[
    "Amy",
    "可爱",
    "乖巧",
    "阳光"
    ]
}
GET /my_index/_search
{
  "query": {
    "multi_match": {
      "query": "Amy",
      "fields": ["name","desc"]
    }
  }
}
```
mutil_match还可以当做match_phrase和match_phrase_prefix使用，只需要指定type类型即可
```
GET a/my_index/_search
{
  "query": {
    "multi_match": {
      "query": "Am",
      "fields": ["name","desc"],
      "type": "phrase_prefix" # 或者phrase
    }
  }
}
```

#### term /terms
通常我们用math是在es经过分词之后解析之后的查询，如果我需要的是没经过分词的词条。
```
PUT /b
{
  "mappings": {
      "properties":{
        "t1":{
          "type": "text"
        }
      }
    }
}

PUT /b/_doc/1
{
  "t1": "Beautiful girl!"
}
PUT /b/_doc/2
{
  "t1": "sexy girl!"
}

GET /b/_search
{
  "query": {
    "match": {
      "t1": "Beautiful girl!"
    }
  }
}
# 这样是查不到结果的，因为t1是text类型，es会对它的内容进行分析，分析之后就没有：Beautiful girl了，它存的是小写的，所以**不要用term对text类型的数据查询**。
GET /b/_search
{
  "query": {
    "term": {
      "t1": "Beautiful girl!"
    }
  }
}
#output
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 0,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  }
}

#使用小写就能查询出结果：
GET /b/_search
{
  "query": {
    "term": {
      "t1": "beautiful"
    }
  }
}
#output
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 0.6931471,
    "hits" : [
      {
        "_index" : "b",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 0.6931471,
        "_source" : {
          "t1" : "Beautiful girl!"
        }
      }
    ]
  }
}

# 查询多个值：
GET /b/_search
{
  "query": {
    "terms": {
      "t1": ["beautiful","sexy"]
    }
  }
}
#output
{
  "took" : 0,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "b",
        "_type" : "_doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "t1" : "Beautiful girl!"
        }
      },
      {
        "_index" : "b",
        "_type" : "_doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "t1" : "sexy girl!"
        }
      }
    ]
  }
}

```
#### bool
must,must not,should 相当于：and,or,not,filter为过滤
**准备数据**
```
PUT /ms/_doc/1
{
  "name":"andy",
  "age":30,
  "from": "hb",
  "desc": "皮肤黑、性格直",
  "tags": ["黑", "长", "直"]
}

PUT /ms/_doc/2
{
  "name":"Amy",
  "age":18,
  "from":"hn",
  "desc":"肤白貌美，娇憨可爱",
  "tags":["白", "富","美"]
}

PUT /ms/_doc/3
{
  "name":"jack",
  "age":22,
  "from":"hb",
  "desc":"mmp，没怎么看，不知道怎么形容",
  "tags":["造数据", "真","难"]
}

PUT /ms/_doc/4
{
  "name":"lili",
  "age":29,
  "from":"bj",
  "desc":"健美 运行",
  "tags":["苗条", "美"]
}

PUT /ms/_doc/5
{
  "name":"Andrew",
  "age":25,
  "from":"hebei",
  "desc":"强壮 跑酷",
  "tags":["高大","威猛"]
}
```
**查询所有湖北（hb)的人**
```
GET /ms/_search
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
**来自hb,并且年龄为30岁的**
```
GET /ms/_search
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

**来自湖北的或者北京的should**
```
GET /ms/_search
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
### sort
```
# 查desc中含有"可爱"的，然后近id倒序排列，但id排序将会废除，除非在mapping中指定 了。 order 可以指定为desc,aes
GET /my_index/_search
{
  "query": {
    "match_all": {}
  },
  "sort":{
    "_id": {
        "order": "desc"  
      }
  }
}
```

### paginate
分页通过from,size指定，from:从哪条(id)开始查，size返回几条结果
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

### highlight
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

### _source
默认情况下，会把所有字段都查出来，但如果我们只需要其中几个字段呢？指定_source对应的字段
```
GET ms/_search
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

### avg/max/min

**数据准备**
```
PUT /ms/_doc/1
{
  "name":"andy",
  "age":30,
  "from": "hb",
  "desc": "皮肤黑、性格直",
  "tags": ["黑", "长", "直"]
}

PUT /ms/_doc/2
{
  "name":"Amy",
  "age":18,
  "from":"hn",
  "desc":"肤白貌美，娇憨可爱",
  "tags":["白", "富","美"]
}

PUT /ms/_doc/3
{
  "name":"jack",
  "age":22,
  "from":"hb",
  "desc":"mmp，没怎么看，不知道怎么形容",
  "tags":["造数据", "真","难"]
}

PUT /ms/_doc/4
{
  "name":"lili",
  "age":29,
  "from":"bj",
  "desc":"健美 运行",
  "tags":["苗条", "美"]
}

PUT /ms/_doc/5
{
  "name":"Andrew",
  "age":25,
  "from":"hebei",
  "desc":"强壮 跑酷",
  "tags":["高大","威猛"]
}
```
**avg**
湖北人的平均年龄
```
GET /ms/_search
{
  "query": {
    "match_all": {
    }
  },
   "aggs":{
     "My_avg":{  # My_avg为最后在结果中显示的字段
       "avg": {
         "field": "age"
       }
     }
   }
}
# 在默认情况下，如果不对结果进行限制，它会将所有内容显示出来，如果只想得到My_avg数据，则需要指定：`size=0`,而如果想看有哪些数据，但又不想看所有字段，那么指定`_source`
GET /ms/_search
{
  "query": {
    "match_all": {
    }
  },
   "aggs":{
     "My_avg":{
       "avg": {
         "field": "age"
       }
     }
   },
   "size": 0
}
#output:
{
  "took" : 3,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 5,
    "max_score" : 0.0,
    "hits" : [ ]
  },
  "aggregations" : {
    "My_avg" : {
      "value" : 24.8
    }
  }
}
```
**max**
min同样的道理
```
GET ms/doc/_search
{
  "query": {
    "match_all": {
    }
  },
   "aggs":{
     "My_max":{
       "max": {
         "field": "age"
       }
     }
   },
   "from":0,
   "size": 0
}
# 指定`"from":0,"size":0`与仅仅指定`"size:0`相同。即从0开始，向后取0个。

#指定`_source`的情况
GET /ms/_search
{
  "query": {
    "match_all": {
    }
  },
   "aggs":{
     "My_max":{
       "max": {
         "field": "age"
       }
     }
   },
"_source": ["name"]
}
#output
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
    "total" : 5,
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "ms",
        "_type" : "doc",
        "_id" : "5",
        "_score" : 1.0,
        "_source" : {
          "name" : "Andrew"
        }
      },
      {
        "_index" : "ms",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 1.0,
        "_source" : {
          "name" : "Amy"
        }
      },
      {
        "_index" : "ms",
        "_type" : "doc",
        "_id" : "4",
        "_score" : 1.0,
        "_source" : {
          "name" : "lili"
        }
      },
      {
        "_index" : "ms",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "name" : "andy"
        }
      },
      {
        "_index" : "ms",
        "_type" : "doc",
        "_id" : "3",
        "_score" : 1.0,
        "_source" : {
          "name" : "jack"
        }
      }
    ]
  },
  "aggregations" : {
    "My_max" : {
      "value" : 30.0
    }
  }
}
```

### group
通过aggs字段来指定分组，通过range来指定from,to指定范围。
```
GET /ms/_search
{
  "query": {
    "match_all": {}
  },
  "size": 0,
  "aggs": {
    "my_group": {
      "range": {
        "field": "age",
        "ranges": [
          {
            "from": 15,
            "to": 20
          },
          {
            "from": 20,
            "to": 25
          },
           {
            "from": 25,
            "to": 30
          }
        ]
      }
    }
  }
}

#output
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
    "total" : 5,
    "max_score" : 0.0,
    "hits" : [ ]
  },
  "aggregations" : {
    "my_group" : {
      "buckets" : [
        {
          "key" : "15.0-20.0",
          "from" : 15.0,
          "to" : 20.0,
          "doc_count" : 1
        },
        {
          "key" : "20.0-25.0",
          "from" : 20.0,
          "to" : 25.0,
          "doc_count" : 1
        },
        {
          "key" : "25.0-30.0",
          "from" : 25.0,
          "to" : 30.0,
          "doc_count" : 2
        }
      ]
    }
  }
}

# 在上面的基本上，求每一组的平均年龄
这里的`my_avg`所对应的aggs是`my_group`的子项，因为是对组求平均
GET ms/_search
{
  "query": {
    "match_all": {}
  },
  "size": 0,
  "aggs": {
    "my_group": {
      "range": {
        "field": "age",
        "ranges": [
          {
            "from": 15,
            "to": 20
          },
          {
            "from": 20,
            "to": 25
          },
           {
            "from": 25,
            "to": 30
          }
        ]
      },
    "aggs":{
      "my_avg":{
        "avg": {
          "field": "age"
        }
      }
    }
    }
  }
}
#output
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
    "total" : 5,
    "max_score" : 0.0,
    "hits" : [ ]
  },
  "aggregations" : {
    "my_group" : {
      "buckets" : [
        {
          "key" : "15.0-20.0",
          "from" : 15.0,
          "to" : 20.0,
          "doc_count" : 1,
          "my_avg" : {
            "value" : 18.0
          }
        },
        {
          "key" : "20.0-25.0",
          "from" : 20.0,
          "to" : 25.0,
          "doc_count" : 1,
          "my_avg" : {
            "value" : 22.0
          }
        },
        {
          "key" : "25.0-30.0",
          "from" : 25.0,
          "to" : 30.0,
          "doc_count" : 2,
          "my_avg" : {
            "value" : 27.0
          }
        }
      ]
    }
  }
}
```