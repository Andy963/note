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
```
#### match
```
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
```
#### match_all
```
GET a1/doc/_search
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

#### match_phrase_prefix
最左前缀查询
```python
GET a1/doc/_search
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
```python
GET a1/doc/_search
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
```python
GET a1/doc/_search
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
```python
PUT a1/doc/4 
{
  "name":"Amy",
  "desc":[
    "Amy",
    "可爱",
    "乖巧",
    "阳光"
    ]
}
GET a1/doc/_search
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
```python
GET a1/doc/_search
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

### term /terms
通常我们用math是在es经过分词之后解析之后的查询，如果我需要的是没经过分词
```
PUT b
{
  "mappings": {
    "doc":{
      "properties":{
        "t1":{
          "type": "text"
        }
      }
    }
  }
}

PUT b/doc/1
{
  "t1": "Beautiful girl!"
}
PUT b/doc/2
{
  "t1": "sexy girl!"
}

GET b/doc/_search
{
  "query": {
    "match": {
      "t1": "Beautiful girl!"
    }
  }
}
# 这样是查不到结果的，因为t1是text类型，es会对它的内容进行分析，分析之后就没有：Beautiful girl了，它存的是小写的，所以**不要用term对text类型的数据查询**。
GET b/doc/_search
{
  "query": {
    "term": {
      "t1": "Beautiful girl!"
    }
  }
}

#使用小写就能查询出结果：
GET b/doc/_search
{
  "query": {
    "term": {
      "t1": "beautiful"
    }
  }
}
# 查询多个值：
GET b/doc/_search
{
  "query": {
    "terms": {
      "t1": ["beautiful","sexy"]
    }
  }
}
```

### suggest
准备数据
```
PUT s1
{
  "mappings": {
    "doc": {
      "properties": {
        "title": {
          "type": "text",
          "analyzer": "standard"
        }
      }
    }
  }
}

PUT s1/doc/1
{
  "title": "Lucene is cool"
}

PUT s1/doc/2
{
  "title":"Elasticsearch builds on top of lucene"
}

GET s1/doc/_search
{
  "query": {
    "match": {
      "title": "Lucene"
    }
  },
  "suggest": {
    "my_suggest": {
      "text": "Elasticsear lucen",
      "term": {
        "field": "title"
      }
    }
  }
}
```

让我们注意suggest，每个建议器都有自己名称my-suggestion，es根据text字段返回建议结果。建议类型是term。从field字段生成建议。正如结果所示。对于输入的每个词条的建议结果，es都会放在options中，如果没有建议结果，options将会为空。
如果我们仅需要建议而不需要查询功能，我们可以忽略query而直接使用suggest对象返回建议
```

GET s1/doc/_search
{
  "suggest": {
    "my_suggest": {
      "text": "Elasticsear lucen",
      "term": {
        "field": "title"
      }
    }
  }
}
#output
{
  "took" : 8,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : 0,
    "max_score" : 0.0,
    "hits" : [ ]
  },
  "suggest" : {
    "my_suggest" : [
      {
        "text" : "elasticsear",
        "offset" : 0,
        "length" : 11,
        "options" : [
          {
            "text" : "elasticsearch",
            "score" : 0.8181818,
            "freq" : 1
          }
        ]
      },
      {
        "text" : "lucen",
        "offset" : 12,
        "length" : 5,
        "options" : [
          {
            "text" : "lucene",
            "score" : 0.8,
            "freq" : 2
          }
        ]
      }
    ]
  }
}
```
哪颗需要多组建议器：
```
GET s1/doc/_search
{
  "suggest": {
    "my_suggest1": {
      "text": "Elasticsear",
      "term": {
        "field": "title"
      }
    },
    "my_suggest2": {
      "text": "lucen",
      "term": {
        "field": "title"
      }
    }
  }
}
# 当text字段一致时，还可以提取出来
GET s1/doc/_search
{
  "suggest": {
    "text": "Elasticsear lucen",
    "my_sugget1": {
      "term": {
        "field": "title"
      }
    },
    "my_suggest2": {
      "term": {
        "field": "title"
      }
    }
  }
}
```
suggester也有多种：
- 词条建议器（term suggester）：对于给定文本的每个词条，该键议器从索引中抽取要建议的关键词，这对于短字段（如分类标签）很有效。
- 词组建议器（phrase suggester）：我们可以认为它是词条建议器的扩展，为整个文本（而不是单个词条）提供了替代方案，它考虑了各词条彼此临近出现的频率，使得该建议器更适合较长的字段，比如商品的描述。
- 完成建议器（completion suggester）：该建议器根据词条的前缀，提供自动完成的功能（智能提示，有点最左前缀查询的意思），为了实现这种实时的建议功能，它得到了优化，工作在内存中。所以，速度要比之前说的match_phrase_prefix快的多！
- 上下文建议器（context suggester）：它是完成建议器的扩展，允许我们根据词条或分类亦或是地理位置对结果进行过滤。
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

### 数据准备
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

### avg/max/min
** 湖北人的平均年龄**
```
GET ms/doc/_search
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
GET ms/doc/_search
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

# max
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
```
GET ms/doc/_search
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
GET ms/doc/_search
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