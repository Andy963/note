在之前的示例中，都没有关注mapping,因为当我们插入数据时，Es会去猜测字段的类型。但如果要自定义，应该怎么做呢？

### 映射类型
- 元字段（meta-fields）：元字段用于自定义如何处理文档关联的元数据，例如包括文档的_index、_type、_id和_source字段
- 字段或属性（field or properties）：映射类型包含与文档相关的字段或者属性的列表

** 数据类型**
- 简单类型，如文本（text）、关键字（keyword）、日期（date）、整形（long）、双精（double）、布尔（boolean）或ip。
- 可以是支持JSON的层次结构性质的类型，如对象或嵌套。
- 或者一种特殊类型，如geo_point、geo_shape或completion

对同一字段，可能会有不同索引方式：比如：字符串字段可能作为全文检索的字段进行索引，也可能作为排序或者聚合的字段进行索引。

** 映射约束**
- index.mapping.total_fields.limit：索引中的最大字段数。字段和对象映射以及字段别名都计入此限制。默认值为1000。
- index.mapping.depth.limit：字段的最大深度，以内部对象的数量来衡量。例如，如果所有字段都在根对象级别定义，则深度为1.如果有一个子对象映射，则深度为2，等等。默认值为20。
- index.mapping.nested_fields.limit：索引中嵌套字段的最大数量，默认为50.索引1个包含100个嵌套字段的文档实际上索引101个文档，因为每个嵌套文档都被索引为单独的隐藏文档。

### 创建
```
PUT my_mapping # 索引名称
{
  "mappings": {
    "doc":{ # 映射类型
    "properties":
    {
     "name":{"type":"text"}, # 字段与字段类型
     "age": {"type":"long"}
    }
    }
  }
}
# 查看下刚创建的mapping
GET my_mapping/_mapping
{
  "my_mapping" : {
    "mappings" : {
      "doc" : {
        "properties" : {
          "age" : {
            "type" : "long"
          },
          "name" : {
            "type" : "text"
          }
        }
      }
    }
  }
}
# 添加数据
POST my_mapping/doc/1
{
  "name":"andy",
  "age":18
}
{
  "_index" : "my_mapping",
  "_type" : "doc",
  "_id" : "1",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 0,
  "_primary_term" : 1
}
```

### dynamic
干啥的？
dynamic用来限制在字义好映射好后，添加新的字段的行为。
默认为dynamic,添加新的字段时，会主动添加新的映射关系
dynamic:false, 添加新的字段时，可以添加，但不会对它进行分词，无法通过新添加的字段查询
dynamic:strict, 无法添加新的字段，但添加数据时可以忽略某些字段。
有啥用？
比如标签 img,本身有src属性，你可以添加id,class等属性。
怎么用？
#### dynamic
```
PUT a2
{
  "mappings": {
    "doc": {
      "dynamic": true,
      "properties": {
        "name": {
          "type": "text"
        },
        "age": {
          "type": "long"
        }
      }
    }
  }
}
```

#### static
```
# 设置为false,此时如果新增字段，它不会对该字段进行分词，导致如果对该新增的字段进行查询，会查不出结果
PUT a3
{
  "mappings": {
    "doc": {
      "dynamic": false,
      "properties": {
        "name": {
          "type": "text"
        },
        "age": {
          "type": "long"
        }
      }
    }
  }
}
POST a3/doc/1
{
  "name":"andy",
  "age":28
}

POST a3/doc/2
{
  "name":"andy",
  "age":28,
  "grade":10
}
# 此时根据后面添加的`grade`字段进行查询，查不出结果，因为Es不会对它进行分词,但可以对其它之前定义好的字段进行查询 
GET a3/doc/_search
{
  "query": {
    "match": {
      "grade": 10
    }
  }
}
#output
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
    "total" : 0,
    "max_score" : null,
    "hits" : [ ]
  }
}
```
#### strict
```如果设置为strict，将导致无法新增字段
PUT a4
{
  "mappings": {
    "doc": {
      "dynamic": "strict",
      "properties": {
        "name": {
          "type": "text"
        },
        "age": {
          "type": "long"
        }
      }
    }
  }
}
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "a4"
}
# 字段对应，添加数据没问题
POST a4/doc/1
{
  "name":"andy",
  "age":28
}
{
  "_index" : "a4",
  "_type" : "doc",
  "_id" : "1",
  "_version" : 1,
  "result" : "created",
  "_shards" : {
    "total" : 2,
    "successful" : 1,
    "failed" : 0
  },
  "_seq_no" : 0,
  "_primary_term" : 1
}
# 增加额外的字段，导致报错，但少一个字段则正常
POST a4/doc/2
{
  "name":"andy",
  "age":28,
  "grade":10
}
{
  "error": {
    "root_cause": [
      {
        "type": "strict_dynamic_mapping_exception",
        "reason": "mapping set to strict, dynamic introduction of [grade] within [doc] is not allowed"
      }
    ],
    "type": "strict_dynamic_mapping_exception",
    "reason": "mapping set to strict, dynamic introduction of [grade] within [doc] is not allowed"
  },
  "status": 400
}
```
### index
index干啥的？
用来限定字段是否索引，如果索引那么可以作为主查询条件查询，如果没索引，则无法查询
index有啥用？
对不希望索引的字段进行限制，比如不需要索引的内容长文本。
index怎么用？
```
#指定age不作为索引
PUT a5
{
  "mappings": {
    "doc": {
      "dynamic": "strict",
      "properties": {
        "name": {
          "type": "text"
        },
        "age": {
          "type": "long",
          "index":"false"
        }
      }
    }
  }
}

POST a5/doc/1
{
  "name":"andy",
  "age":28
}

POST a5/doc/2
{
  "name":"Amy",
  "age":19
}

GET a5/doc/_search
{
  "query": {
    "match": {
      "name": "Amy"
    }
  }
}
#output
{
  "took" : 10,
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
        "_index" : "a5",
        "_type" : "doc",
        "_id" : "2",
        "_score" : 0.2876821,
        "_source" : {
          "name" : "Amy",
          "age" : 19
        }
      }
    ]
  }
}
GET a5/doc/_search
{
  "query": {
    "match": {
      "age": "19"
    }
  }
}
#output
{
  "error": {
    "root_cause": [
      {
        "type": "query_shard_exception",
        "reason": "failed to create query: {\n  \"match\" : {\n    \"age\" : {\n      \"query\" : \"19\",\n      \"operator\" : \"OR\",\n      \"prefix_length\" : 0,\n      \"max_expansions\" : 50,\n      \"fuzzy_transpositions\" : true,\n      \"lenient\" : false,\n      \"zero_terms_query\" : \"NONE\",\n      \"auto_generate_synonyms_phrase_query\" : true,\n      \"boost\" : 1.0\n    }\n  }\n}",
        "index_uuid": "X5pVZfMYREqstpaipj5JIQ",
        "index": "a5"
      }
    ],
    "type": "search_phase_execution_exception",
    "reason": "all shards failed",
    "phase": "query",
    "grouped": true,
    "failed_shards": [
      {
        "shard": 0,
        "index": "a5",
        "node": "vS6Xs5U6S9C50QpbNRZLkw",
        "reason": {
          "type": "query_shard_exception",
          "reason": "failed to create query: {\n  \"match\" : {\n    \"age\" : {\n      \"query\" : \"19\",\n      \"operator\" : \"OR\",\n      \"prefix_length\" : 0,\n      \"max_expansions\" : 50,\n      \"fuzzy_transpositions\" : true,\n      \"lenient\" : false,\n      \"zero_terms_query\" : \"NONE\",\n      \"auto_generate_synonyms_phrase_query\" : true,\n      \"boost\" : 1.0\n    }\n  }\n}",
          "index_uuid": "X5pVZfMYREqstpaipj5JIQ",
          "index": "a5",
          "caused_by": {
            "type": "illegal_argument_exception",
            "reason": "Cannot search on field [age] since it is not indexed."
          }
        }
      }
    ]
  },
  "status": 400
}
```

### copy_to
干啥的？
从一个字段向另一个字段赋值，copy后面可以通过`copy_to:[f1,f2]`复制到多个字段，在聚合中使用时，要将filddata设置为true
有啥用？
当字段之间有一定关系时可以通过复制完成，不知道是否可以进行运算
怎么用？
```
PUT a6
{
  "mappings": {
    "doc": {
      "properties": {
        "name": {
          "type": "text",
          "copy_to":"full_name"
        },
        "age": {
          "type": "long",
          "index":"false"
        },
        "full_name":{
          "type":"text"
        }
      }
    }
  }
}
#output
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "a6"
}

POST a6/doc/1
{
  "name":"Amy",
  "age":19
}

GET a6/doc/_search
{
  "query": {
    "match": {
      "name": "Amy"
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
        "_index" : "a6",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 0.2876821,
        "_source" : {
          "name" : "Amy",
          "age" : 19
        }
      }
    ]
  }
}

GET a6/doc/_search
{
  "query": {
    "match": {
      "full_name": "Amy"
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
        "_index" : "a6",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 0.2876821,
        "_source" : {
          "name" : "Amy",
          "age" : 19
        }
      }
    ]
  }
}

```
### 对象的属性
对象的属性是什么？
在这里可以理解嵌套的数据结构
有什么用？
多层嵌套数据结果时，获取子属性。
怎么用？
对过点访问它的子属性
```
PUT a8
{
  "mappings": {
    "doc":{
      "properties":{
        "name":{"type":"text"},
        "info":{
          "properties":{
            "city":{"type":"text"},
            "county":{"type":"text"}
          }
        }
      }
  
    }
  }
}
POST a8/doc/1
{
  "name":"wanggang",
  "info":{
    "city":"shanxi",
    "county":"xishan"
  }
}

GET a8/doc/_search
{
  "query": {
    "match": {
      "info.city": "shanxi"
    }
  }
}
#output
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
    "max_score" : 0.2876821,
    "hits" : [
      {
        "_index" : "a8",
        "_type" : "doc",
        "_id" : "1",
        "_score" : 0.2876821,
        "_source" : {
          "name" : "wanggang",
          "info" : {
            "city" : "shanxi",
            "county" : "xishan"
          }
        }
      }
    ]
  }
}
```

### 指定分片信息
```
PUT s1
{
  "mappings": {
    "doc": {
      "properties": {
        "name": {
          "type": "text"
        }
      }
    }
  }, 
  "settings": {
    "number_of_replicas": 1,
    "number_of_shards": 5
  }
}
```
number_of_shards是主分片数量（每个索引默认5个主分片），而number_of_replicas是复制分片，默认一个主分片搭配一个复制分片。

### ignore_above
长度超过ignore_above设置的字符串将不会被索引或存储（个人认为会存储，但不会为该字段建立索引，也就是该字段不能被检索）。 对于字符串数组，ignore_above将分别应用于每个数组元素，并且不会索引或存储比ignore_above更长的字符串元素。