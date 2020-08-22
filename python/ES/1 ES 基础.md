
## 基本操作：

### index type
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

**dynamic/static/strict**
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
PUT my_index1
{
  "mappings": {
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
```

#### static
```
# 设置为false,此时如果新增字段，它不会对该字段进行分词，导致如果对该新增的字段进行查询，会查不出结果
PUT my_index2
{
  "mappings": {
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

POST /my_index2/_doc/1
{
  "name":"andy",
  "age":28
}


POST /my_index2/_doc/2
{
  "name":"andy",
  "age":28,
  "grade":10
}

# 此时根据后面添加的`grade`字段进行查询，查不出结果，因为Es不会对它进行分词,但可以对其它之前定义好的字段进行查询 
GET /my_index2/_search
{
  "query": {
    "match": {
      "grade": 10
    }
  }
}
#output
{
  "took" : 713,
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
#### strict
```如果设置为strict，将导致无法新增字段
PUT /my_index3
{
  "mappings": {
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
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "my_index3"
}

# 字段对应，添加数据没问题
POST /my_index3/_doc/1
{
  "name":"andy",
  "age":28
}
{
  "_index" : "my_index3",
  "_type" : "_doc",
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
POST /my_index3/_doc/2
{
  "name":"andy",
  "age":28,
  "grade":10
}
{
  "error" : {
    "root_cause" : [
      {
        "type" : "strict_dynamic_mapping_exception",
        "reason" : "mapping set to strict, dynamic introduction of [grade] within [_doc] is not allowed"
      }
    ],
    "type" : "strict_dynamic_mapping_exception",
    "reason" : "mapping set to strict, dynamic introduction of [grade] within [_doc] is not allowed"
  },
  "status" : 400
}
```

### properties
对象的属性是什么？
在这里可以理解嵌套的数据结构
有什么用？
多层嵌套数据结果时，获取子属性。
怎么用？
对过点访问它的子属性
```
PUT /my_index/
{
  "mappings": {
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
POST /my_index/_doc/1
{
  "name":"wanggang",
  "info":{
    "city":"shanxi",
    "county":"xishan"
  }
}

GET /my_index/_search
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

### index or not
index干啥的？
用来限定字段是否索引，如果索引那么可以作为主查询条件查询，如果没索引，则无法查询
index有啥用？
对不希望索引的字段进行限制，比如不需要索引的内容长文本。
index怎么用？
```
#指定age不作为索引
PUT my_index
{
  "mappings": {
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

POST /my_index/_doc/1
{
  "name":"andy",
  "age":28
}

POST /my_index/_doc/2
{
  "name":"Amy",
  "age":19
}

GET /my_index/_search
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

GET /my_index/_search
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
PUT /my_index
{
  "mappings": {
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
#output
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "a6"
}

POST /my_index/_doc/1
{
  "name":"Amy",
  "age":19
}

GET /my_index/_search
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

GET /my_index/_search
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

### PUT/GET/DELETE
```
PUT /my_index

GET /my_index
{
  "my_index" : {
    "aliases" : { },
    "mappings" : {
      "properties" : {
        "email" : {
          "type" : "keyword"
        }
      }
    },
    "settings" : {
      "index" : {
        "creation_date" : "1598067052855",
        "number_of_shards" : "1",
        "number_of_replicas" : "1",
        "uuid" : "zND6rQGKSh-CwcLQTyn9ew",
        "version" : {
          "created" : "7090099"
        },
        "provided_name" : "my_index"
      }
    }
  }
}

DELETE /my_index
```

### setting
修改index setting,当要创建的index不存在时，下面代码才能成功
```
PUT /my_index
{
  "settings": {
    "index": {
      "number_of_shards": 2,  
      "number_of_replicas": 2 
    }
  }
}
# 可以不指定index
PUT /my-index-000001
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 2
  }
}
```
create index with setting and mapping
```
PUT /test
{
  "settings": {
    "number_of_shards": 1
  },
  "mappings": {
    "properties": {
      "field1": { "type": "text" }
    }
  }
}
```
create index with alias
```
PUT /test
{
  "aliases": {
    "alias_1": {},
    "alias_2": {
      "filter": {
        "term": { "user.id": "kimchy" }
      },
      "routing": "shard-1"
    }
  }
}
```
**ignore_above**
长度超过ignore_above设置的字符串将不会被索引或存储（个人认为会存储，但不会为该字段建立索引，也就是该字段不能被检索）。 对于字符串数组，ignore_above将分别应用于每个数组元素，并且不会索引或存储比ignore_above更长的字符串元素。

### mapping

#### PUT/GET/DELETE
```
PUT /publications # 这样创建的索引不带mapping

PUT /publications/_mapping  # 必须先有索引才能这样操作
{
  "properties": {
    "title":  { "type": "text"}
  }
}

# 作用在多个index上
PUT /my-index-000001
PUT /my-index-000002
PUT /my-index-000001,my-index-000002/_mapping
{
  "properties": {
    "user": {
      "properties": {
        "name": {
          "type": "keyword"
        }
      }
    }
  }
}
# 在创建索引时指定mappings, 此情况下，index不能是已经存在的
PUT /my-index-000001
{
  "mappings": {
    "properties": {
      "name": {
        "properties": {
          "first": {
            "type": "text"
          }
        }
      }
    }
  }
}
```
#### add new filed
为已经存在的mapping添加字段
```
PUT /my-index-000001/_mapping
{
  "properties": {
    "name": {
      "properties": {
        "last": {
          "type": "text"
        }
      }
    }
  }
}

PUT /my-index-000001
{
  "mappings": {
    "properties": {
      "city": {
        "type": "text"
      }
    }
  }
}

# 这同一字段指定两种不同类型 用raw
PUT /my-index-000001/_mapping
{
  "properties": {
    "city": {
      "type": "text",
      "fields": {
        "raw": {
          "type": "keyword"
        }
      }
    }
  }
}
```
#### update mapping filed
```
PUT /my-index-000001
{
  "mappings": {
    "properties": {
      "user_id": {
        "type": "keyword",
        "ignore_above": 20
      }
    }
  }
}
# 将ignore_above 从20改成100
PUT /my-index-000001/_mapping
{
  "properties": {
    "user_id": {
      "type": "keyword",
      "ignore_above": 100
    }
  }
}

GET /my-index-000001
{
  "my-index-000001" : {
    "aliases" : { },
    "mappings" : {
      "properties" : {
        "user_id" : {
          "type" : "keyword",
          "ignore_above" : 100
        }
      }
    },
    "settings" : {
      "index" : {
        "creation_date" : "1598075230100",
        "number_of_shards" : "1",
        "number_of_replicas" : "1",
        "uuid" : "tV2LZYU5R0qJf9RR7gOzWw",
        "version" : {
          "created" : "7090099"
        },
        "provided_name" : "my-index-000001"
      }
    }
  }
}
```
#### change the mapping of exist field
```
# create index
PUT /my-index-000001
{
  "mappings" : {
    "properties": {
      "user_id": {
        "type": "long"
      }
    }
  }
}

# post data
POST /my-index-000001/_doc?refresh=wait_for
{
  "user_id" : 12345
}

POST /my-index-000001/_doc?refresh=wait_for
{
  "user_id" : 12346
}

# create new index with correct type: keyword
PUT /my-new-index-000001
{
  "mappings" : {
    "properties": {
      "user_id": {
        "type": "keyword"
      }
    }
  }
}

# reindex data from old source: my-index-000001 to my-new-index-000001
POST /_reindex
{
  "source": {
    "index": "my-index-000001"
  },
  "dest": {
    "index": "my-new-index-000001"
  }
}
#此时两个 索引数据一样：
GET /my-index-000001/_search

GET /my-new-index-000001/_search
{
  "took" : 77,
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
        "_index" : "my-new-index-000001",
        "_type" : "_doc",
        "_id" : "dt24FHQBjhulFRhnlbug",
        "_score" : 1.0,
        "_source" : {
          "user_id" : 12345
        }
      },
      {
        "_index" : "my-new-index-000001",
        "_type" : "_doc",
        "_id" : "et24FHQBjhulFRhns7sz",
        "_score" : 1.0,
        "_source" : {
          "user_id" : 12346
        }
      }
    ]
  }
}

```
#### rename field
```
PUT /my-index-000001
{
  "mappings": {
    "properties": {
      "user_identifier": {
        "type": "keyword"
      }
    }
  }
}
#output
{
  "my-index-000001" : {
    "aliases" : { },
    "mappings" : {
      "properties" : {
        "user_identifier" : {
          "type" : "keyword"
        }
      }
    },
    "settings" : {
      "index" : {
        "creation_date" : "1598076038653",
        "number_of_shards" : "1",
        "number_of_replicas" : "1",
        "uuid" : "K-vITcAcQ5uSsNuVmzYB0g",
        "version" : {
          "created" : "7090099"
        },
        "provided_name" : "my-index-000001"
      }
    }
  }
}

#rename
PUT /my-index-000001/_mapping
{
  "properties": {
    "user_id": {
      "type": "alias",
      "path": "user_identifier"
    }
  }
}
GET /my-index-000001
{
  "my-index-000001" : {
    "aliases" : { },
    "mappings" : {
      "properties" : {
        "user_id" : {
          "type" : "alias",
          "path" : "user_identifier"
        },
        "user_identifier" : {
          "type" : "keyword"
        }
      }
    },
    "settings" : {
      "index" : {
        "creation_date" : "1598076038653",
        "number_of_shards" : "1",
        "number_of_replicas" : "1",
        "uuid" : "K-vITcAcQ5uSsNuVmzYB0g",
        "version" : {
          "created" : "7090099"
        },
        "provided_name" : "my-index-000001"
      }
    }
  }
}

```


注意，在新版本中去年了type字段，所以查询时添加时应该写成：PUT a1/_doc/1, 而查询是应该是：GET a1/_search,如果仍然加了doc，可能导致结果不是我们想要的。
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

在之前的示例中，都没有关注mapping,因为当我们插入数据时，Es会去猜测字段的类型。但如果要自定义，应该怎么做呢？

