
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
dynamic用来限制在定义好映射好后，添加新的字段的行为。
默认为dynamic,添加新的字段时，会主动添加新的映射关系
dynamic:false, 添加新的字段时，可以添加，但不会对它进行分词，无法通过新添加的字段查询
dynamic:strict, 无法添加新的字段，但添加数据时可以忽略某些字段。
有啥用？
比如标签 img,本身有src属性，你可以添加id,class等属性。
怎么用？
#### dynamic

```json
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

```json

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

```json

如果设置为strict，将导致无法新增字段
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

### 属性（properties）
对象的属性是什么？
在这里可以理解嵌套的数据结构
有什么用？
多层嵌套数据结果时，获取子属性。
怎么用？
对过点访问它的子属性

```json
// 创建一个有两个字段的索引， 包括name, info,其中info 是嵌套结构，又包含city, county 字段
// 而字段属性是text,文本类型，可能会被索引
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

```json
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
用来定义索引中数据的类型，结构

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

## 增删改查
Create,Update,Retrieve,Delete
### Create

`POST /my_index/_doc/1`
```json
{
  "name":"Amy",
  "age":19
}

```

` POST /my_index/_doc/2 `
```json
{
  "name":"jack",
  "age":18
}
```

### Update
先查一下：
` GET /my_index/_search `
```json
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

`POST /my_index/_update/1`
```json
{
  "doc":{
      "name":"amy",
      "age":19
  }
}
```
### Retrieve
` GET /my_index/_search `
```json
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
` DELETE /my_index/_doc/1 `

删除后再查询：` GET /my_index/_search `
```json
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
## 查询URL(Retrieve url)

### 查询参数（url params）

` GET /my_index/_search/?q=age:19 `

```json
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

### match

查询 ` GET /my_index/_search `
```json
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
```

添加数据 ` PUT /my_index/_doc/3 `

```json
{
  "name":"Mary",
  "desc":["可爱","漂亮"]
}

{
  "name":"Amy",
  "desc":["可爱","乖巧","阳光"]
}
```


查询 ` GET /my_index/_search `
```json
{
  "query": {
    "match": {
        "desc":"可 漂"
    }
  }
}
```

这种情况下Es会对"可 漂" 做分词

```json
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

### match_all
` GET /my_index/_doc/_search `
```json
{
  "query": {
    "match_all": {}
  }
}
# match_all后面的条件为空，相当于select * from table;
```
### 分词查询 （match_phrase）

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

### 最左前缀查询（match_phrase_prefix）

` GET /my_index/_search `

```json
{
  "query": {
    "match_phrase_prefix": {
      "name": "M"
    }
  }
}
```

```json
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
```json
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
### 多字段（multi_match）
多字段查询：
我们可以通过must来限定多个字段,但如果字段太多，这样就比较麻烦
```json
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

### 词条（term /terms）
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
### 布尔（bool）
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
### 排序（sort）
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

### 分页（paginate）
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

### 高亮（highlight）
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

### 指定字段 （_source）
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

### 分组（group）
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

## 建议器（suggester）
准备数据
```
PUT s1
{
  "mappings": {
      "properties": {
        "title": {
          "type": "text",
          "analyzer": "standard"
        }
      }
    }
}

PUT /s1/_doc/1
{
  "title": "Lucene is cool"
}

PUT s1/_doc/2
{
  "title":"Elasticsearch builds on top of lucene"
}

GET s1/_doc/_search
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

### term suggester
词条建议器接收输入的文本，对其进行分析并且分为词条，然后为每个词条提供一系列的建议
```
PUT s2
{
  "mappings": {
      "properties": {
        "title": {
          "type": "text",
          "analyzer": "standard"
        }
      }
    }
}

PUT /s2/_doc/1
{
  "title": "Lucene is cool"
}

PUT /s2/_doc/2
{
  "title": "Elasticsearch builds on top of lucene"
}

PUT /s2/_doc/3
{
  "title": "Elasticsearch rocks"
}

PUT /s2/_doc/4
{
  "title": "Elastic is the company behind ELK stack"
}

PUT /s2/_doc/5
{
  "title": "elk rocks"
}
PUT /s2/_doc/6
{
  "title": "elasticsearch is rock solid"
}
```

查询

```
GET /s2/_search
{
  "suggest": {
    "my_suggest": {
      "text": "luenc",
      "term": {
        "field": "title"
      }
    }
  }
}
{
  "took" : 951,
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
  },
  "suggest" : {
    "my_suggest" : [
      {
        "text" : "luenc",
        "offset" : 0,
        "length" : 5,
        "options" : [
          {
            "text" : "lucene",
            "score" : 0.6,
            "freq" : 2
          }
        ]
      }
    ]
  }
}
```

在options字段中，建议结果是lucene

#### suggester fields
- text 建议文本，建议文本是必需的选项，可以通过全局（多个建议器中查询相同的内容）或者按照单个建议器的格式来
- field 从field字段中获取候选建议的字段。这是一个必需的选项，需要全局设置或根据建议器设置
- analyzer：用于分析建议文本的分析器。默认为建议字段的搜索分析器
- size：个建议文本标记返回的最大条目
- sort：定义如何根据建议文本术语对建议进行排序。它有两个可能的值
    - score，先按分数排序，然后按文档频率排序，再按术语本身排序
    - frequency，首先按文档频率排序，然后按相似性分数排序，然后按术语本身排序。也可以理解为按照流行度排序
- suggest_mode：控制建议的模式，有3个模式可选择
    - missing，仅为不在索引中的建议文本术语提供建议。这是默认值
    - popular，仅建议在比原始建议文本术语更多的文档中出现的建议。也就是说提供比原有输入词频更高的词条
    - always，根据建议文本中的条款建议任何匹配的建议。说白了就是无论如何都会提供建议。
- lowercase_terms：在文本分析之后降低建议文本术语的大小写
- min_word_length：建议文本术语必须具有的最小长度才能包含在内。默认为4.（旧名称min_word_len已弃用）
- shard_size：设置从每个单独分片中检索的最大建议数。在减少阶段，仅根据size选项返回前N个建议。默认为该 size选项。将此值设置为高于该值的值size可能非常有用，以便以性能为代价获得更准确的拼写更正文档频率。由于术语在分片之间被划分，因此拼写校正频率的分片级文档可能不准确。增加这些将使这些文档频率更精确
- max_inspections：用于乘以的因子， shards_size以便在碎片级别上检查更多候选拼写更正。可以以性能为代价提高准确性。默认为5
- string_distance：用于比较类似建议术语的字符串距离实现
    - internal，默认值基于damerau_levenshtein，但高度优化用于比较索引中术语的字符串距离
    - damerau_levenshtein，基于Damerau-Levenshtein算法的字符串距离算法
    - levenshtein，基于Levenshtein编辑距离算法的字符串距离算法
    - jaro_winkler，基于Jaro-Winkler算法的字符串距离算法
    - ngram，基于字符n-gram的字符串距离算法

#### how 
词条建议器使用了Lucene的错拼检查器模块，该模块会根据给定词条的编辑距离（es使用了叫做Levenstein edit distance的算法，其核心思想就是一个词改动多少字符就可以和另外一个词一致），从索引中返回最大编辑距离不超过某个值的那些词条。比如说为了从mik得到mick，需要加入一个字母（也就是说需要至少要改动一次），所以这两个词的编辑距离就是1。我们可以通过配置一系列的选项，来均衡灵活和性能

- max_edits：最大编辑距离候选建议可以具有以便被视为建议。只能是介于1和2之间的值。任何其他值都会导致抛出错误的请求错误。默认为2。
- prefix_length：必须匹配的最小前缀字符的数量才是候选建议。默认为1.增加此数字可提高拼写检查性能。通常拼写错误不会出现在术语的开头。（旧名prefix_len已弃用）。
- min_doc_freq：建议应出现的文档数量的最小阈值。可以指定为绝对数字或文档数量的相对百分比。这可以仅通过建议高频项来提高质量。默认为0f且未启用。如果指定的值大于1，则该数字不能是小数。分片级文档频率用于此选项。
- max_term_freq：建议文本令牌可以存在的文档数量的最大阈值，以便包括在内。可以是表示文档频率的相对百分比数（例如0.4）或绝对数。如果指定的值大于1，则不能指定小数。默认为0.01f。这可用于排除高频术语的拼写检查。高频术语通常拼写正确，这也提高了拼写检查的性能。分片级文档频率用于此选项。
#### conclusion
term suggester首先将输入文本经过分析器（所以，分析结果由于采用的分析器不同而有所不同）分析，处理为单个词条，然后根据单个词条去提供建议，并不会考虑多个词条之间的关系。然后将每个词条的建议结果（有或没有）封装到options列表中。最后由建议器统一返回
### phrase suggester
词组建议器和词条建议器一样，不过它不再为单个词条提供建议，而是为整个文本提供建议。

```
PUT s3
{
  "mappings": {
      "properties": {
        "title": {
          "type": "text",
          "analyzer": "standard"
        }
      }
    }
}

PUT /s3/_doc/1
{
  "title": "Lucene is cool"
}

PUT /s3/_doc/2
{
  "title": "Elasticsearch builds on top of lucene"
}

PUT /s3/_doc/3
{
  "title": "Elasticsearch rocks"
}

PUT /s3/_doc/4
{
  "title": "Elastic is the company behind ELK stack"
}

PUT /s3/_doc/5
{
  "title": "elk rocks"
}

PUT /s3/_doc/6
{
  "title": "elasticsearch is rock solid"
}
```

查询

```
GET /s3/_search
{
  "suggest": {
    "my_s3": {
      "text": "lucne and elasticsear rock",
      "phrase": {
        "field": "title"
      }
    }
  }
}
{
  "took" : 318,
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
  },
  "suggest" : {
    "my_s3" : [
      {
        "text" : "lucne and elasticsear rock",
        "offset" : 0,
        "length" : 26,
        "options" : [
          {
            "text" : "lucene and elasticsearch rock",
            "score" : 0.004993905
          },
          {
            "text" : "lucne and elasticsearch rock",
            "score" : 0.0033391973
          },
          {
            "text" : "lucene and elasticsear rock",
            "score" : 0.0029183894
          }
        ]
      }
    ]
  }
}
```
可以看到options直接返回了相关短语列表。虽然lucene建议的并不好。但elasticserch和rock很不错。除此之外，我们还可以使用高亮来向用户展示哪些原有的词条被纠正了。
```
GET /s3/_search
{
  "suggest": {
    "my_s3": {
      "text": "lucne and elasticsear rock",
      "phrase": {
        "field": "title",
        "highlight":{
          "pre_tag":"<em>",
          "post_tag":"</em>"
        }
      }
    }
  }
}
{
  "took" : 9,
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
  },
  "suggest" : {
    "my_s3" : [
      {
        "text" : "lucne and elasticsear rock",
        "offset" : 0,
        "length" : 26,
        "options" : [
          {
            "text" : "lucene and elasticsearch rock",
            "highlighted" : "<em>lucene</em> and <em>elasticsearch</em> rock",
            "score" : 0.004993905
          },
          {
            "text" : "lucne and elasticsearch rock",
            "highlighted" : "lucne and <em>elasticsearch</em> rock",
            "score" : 0.0033391973
          },
          {
            "text" : "lucene and elasticsear rock",
            "highlighted" : "<em>lucene</em> and elasticsear rock",
            "score" : 0.0029183894
          }
        ]
      }
    ]
  }
}
#除了默认的，还可以自定义高亮显示：
GET s4/doc/_search
{
  "suggest": {
    "my_s4": {
      "text": "lucne and elasticsear rock",
      "phrase": {
        "field": "title",
        "highlight":{
          "pre_tag":"<b id='d1' class='t1' style='color:red;font-size:18px;'>",
          "post_tag":"</b>"
        }
      }
    }
  }
}
#需要注意的是，建议器结果的高亮显示和查询结果高亮显示有些许区别，比如说，这里的自定义标签是pre_tag和post_tag而不是之前如这样的
GET /s3/_search
{
  "query": {
    "match": {
      "title": "rock"
    }
  },
  "highlight": {
    "pre_tags": "<b style='color:red'>",
    "post_tags": "</b>",
    "fields": {
      "title": {}
    }
  }
}
{
  "took" : 57,
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
    "max_score" : 1.540445,
    "hits" : [
      {
        "_index" : "s3",
        "_type" : "_doc",
        "_id" : "6",
        "_score" : 1.540445,
        "_source" : {
          "title" : "elasticsearch is rock solid"
        },
        "highlight" : {
          "title" : [
            "elasticsearch is <b style='color:red'>rock</b> solid"
          ]
        }
      }
    ]
  }
}
```

phrase suggester在term suggester的基础上，会考虑多个term之间的关系，比如是否同时出现索引的原文中，临近程度，词频等。

### completion suggester
为了告诉elasticsearch我们准备将建议存储在自动完成的FST中，需要在映射中定义一个字段并将其type类型设置为completion

```
PUT s4
{
  "mappings":{
      "properties": {
        "title": {
          "type": "completion",
          "analyzer": "standard"
        }
      }
    }
}

PUT /s4/_doc/1
{
  "title":"Lucene is cool"
}

PUT /s4/_doc/2
{
  "title":"Elasticsearch builds on top of lucene"
}

PUT /s4/_doc/3
{
  "title":"Elasticsearch rocks"
}

PUT /s4/_doc/4
{
  "title":"Elastic is the company behind ELK stack"
}

PUT /s4/_doc/5
{
  "title":"the elk stack rocks"
}

PUT /s4/_doc/6
{
  "title":"elasticsearch is rock solid"
}

GET /s4/_search
{
  "suggest": {
    "my_s4": {
      "text": "elas",
      "completion": {
        "field": "title"
      }
    }
  }
}
#output
{
  "took" : 865,
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
  },
  "suggest" : {
    "my_s4" : [
      {
        "text" : "elas",
        "offset" : 0,
        "length" : 4,
        "options" : [
          {
            "text" : "Elastic is the company behind ELK stack",
            "_index" : "s4",
            "_type" : "_doc",
            "_id" : "4",
            "_score" : 1.0,
            "_source" : {
              "title" : "Elastic is the company behind ELK stack"
            }
          },
          {
            "text" : "Elasticsearch builds on top of lucene",
            "_index" : "s4",
            "_type" : "_doc",
            "_id" : "2",
            "_score" : 1.0,
            "_source" : {
              "title" : "Elasticsearch builds on top of lucene"
            }
          },
          {
            "text" : "Elasticsearch rocks",
            "_index" : "s4",
            "_type" : "_doc",
            "_id" : "3",
            "_score" : 1.0,
            "_source" : {
              "title" : "Elasticsearch rocks"
            }
          },
          {
            "text" : "elasticsearch is rock solid",
            "_index" : "s4",
            "_type" : "_doc",
            "_id" : "6",
            "_score" : 1.0,
            "_source" : {
              "title" : "elasticsearch is rock solid"
            }
          }
        ]
      }
    ]
  }
}
```
上例的特殊映射中，支持以下参数：
- analyzer，要使用的索引分析器，默认为simple。
- search_analyzer，要使用的搜索分析器，默认值为analyzer。
- preserve_separators，保留分隔符，默认为true。 如果您禁用，您可以找到以Foo Fighters开头的字段，如果您建议使用foof。
- preserve_position_increments，启用位置增量，默认为true。如果禁用并使用停用词分析器The Beatles，如果您建议，可以从一个字段开始b。注意：您还可以通过索引两个输入来实现此目的，Beatles并且 The Beatles，如果您能够丰富数据，则无需更改简单的分析器。
- max_input_length，限制单个输入的长度，默认为50UTF-16代码点。此限制仅在索引时使用，以减少每个输入字符串的字符总数，以防止大量输入膨胀基础数据结构。大多数用例不受默认值的影响，因为前缀完成很少超过前缀长于少数几个字符。

#### 已存在索引字段的多字段
```
PUT s6
{
  "mappings": {
      "properties": {
        "name": {
          "type": "text",
          "fields": {
            "suggest": {
              "type": "completion"
            }
          }
        }
      }
    }
}

PUT s6/_doc/1
{
  "name":"KFC"
}
PUT s6/_doc/2
{
  "name":"kfc"
}

GET s6/_search
{
  "suggest": {
    "my_s6": {
      "text": "K",
      "completion": {
        "field": "name.suggest"
      }
    }
  }
}
#output
{
  "took" : 20,
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
  },
  "suggest" : {
    "my_s6" : [
      {
        "text" : "K",
        "offset" : 0,
        "length" : 1,
        "options" : [
          {
            "text" : "KFC",
            "_index" : "s6",
            "_type" : "_doc",
            "_id" : "1",
            "_score" : 1.0,
            "_source" : {
              "name" : "KFC"
            }
          },
          {
            "text" : "kfc",
            "_index" : "s6",
            "_type" : "_doc",
            "_id" : "2",
            "_score" : 1.0,
            "_source" : {
              "name" : "kfc"
            }
          }
        ]
      }
    ]
  }
}
```
#### 在索引阶段提升相关性
在进行普通的索引时，输入的文本在索引和搜索阶段都会被分析，这就是为什么上面的示例会将KFC和kfc都返回了。我们也可以通过analyzer和search_analyzer选项来进一步控制分析过程。如上例我们可以只匹配KFC而不匹配kfc.

通过指定　analyzer:keyword
```
PUT s7
{
  "mappings": {
      "properties": {
        "name": {
          "type": "text",
          "fields": {
            "suggest": {
              "type": "completion",
              "analyzer":"keyword",
              "search_analyzer":"keyword"
            }
          }
        }
      }
    }
}

PUT /s7/_doc/1
{
  "name":"KFC"
}
PUT /s7/_doc/2
{
  "name":"kfc"
}
GET /s7/_search
{
  "suggest": {
    "my_s7": {
      "text": "K",
      "completion": {
        "field": "name.suggest"
      }
    }
  }
}
#output
{
  "took" : 1,
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
  },
  "suggest" : {
    "my_s7" : [
      {
        "text" : "K",
        "offset" : 0,
        "length" : 1,
        "options" : [
          {
            "text" : "KFC",
            "_index" : "s7",
            "_type" : "_doc",
            "_id" : "1",
            "_score" : 1.0,
            "_source" : {
              "name" : "KFC"
            }
          }
        ]
      }
    ]
  }
}
```
##### input/weight
使用input和可选的weight属性，input是建议查询匹配的预期文本，weight是建议评分方式（也就是权重）。例如
```
PUT s8
{
  "mappings": {
      "properties":{
        "title":{
          "type": "completion"
        }
      }
    }
}
```
添加数据:分别添加两个建议并设置各自的权重值
```
PUT s8/_doc/1
{
  "title":{
    "input":"blow",
    "weight": 2
  }
}
PUT s8/_doc/2
{
  "title":{
    "input":"block",
    "weight": 3
  }
}
```
以列表的形式添加建议，设置不同的权重
```
PUT s8/_doc/3
{
  "title": [  
    {
      "input":"appel",
      "weight": 2
    },
    {
      "input":"apple",
      "weight": 3
    }
  ]
}
```
为多个建议设置相同的权重
```
PUT s8/_doc/4
{
  "title": ["apple", "appel", "block", "blow"],
  "weght": 32
}
```
查询的结果由权重决定
```
GET /s8/_search
{
  "suggest": {
    "my_s8": {
      "text": "app",
      "completion": {
        "field": "title"
      }
    }
  }
}
#output
{
  "took" : 49,
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
  },
  "suggest" : {
    "my_s8" : [
      {
        "text" : "app",
        "offset" : 0,
        "length" : 3,
        "options" : [
          {
            "text" : "apple",
            "_index" : "s8",
            "_type" : "_doc",
            "_id" : "3",
            "_score" : 3.0,
            "_source" : {
              "title" : [
                {
                  "input" : "appel",
                  "weight" : 2
                },
                {
                  "input" : "apple",
                  "weight" : 3
                }
              ]
            }
          },
          {
            "text" : "appel",
            "_index" : "s8",
            "_type" : "_doc",
            "_id" : "4",
            "_score" : 1.0,
            "_source" : {
              "title" : [
                "apple",
                "appel",
                "block",
                "blow"
              ],
              "weght" : 32
            }
          }
        ]
      }
    ]
  }
}
```
#### 在搜索阶段提升相关性
当在运行建议的请求时，可以决定出现哪些建议，就像其他建议器一样，size参数控制返回多少项建议（默认为5项）；还可以通过fuzzy参数设置模糊建议，以对拼写进行容错。当开启模糊建议之后，可以设置下列参数来完成建议

－　fuzziness，可以指定所允许的最大编辑距离。
－　min_length，指定什么长度的输入文本可以开启模糊查询。
－　prefix_length，假设若干开始的字符是正确的（比如block，如果输入blaw，该字段也认为之前输入的是对的），这样可以通过牺牲灵活性提升性能
这些参数都是在建议的completion对象的下面
```
GET /s8/_search
{
  "suggest": {
    "my_s9": {
      "text": "blaw",
      "completion": {
        "field": "title",
        "size": 2,
        "fuzzy": {
          "fuzziness": 2,
          "min_length": 3,
          "prefix_length": 2
        }
      }
    }
  }
}
#output
{
  "took" : 5,
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
  },
  "suggest" : {
    "my_s9" : [
      {
        "text" : "blaw",
        "offset" : 0,
        "length" : 4,
        "options" : [
          {
            "text" : "block",
            "_index" : "s8",
            "_type" : "_doc",
            "_id" : "2",
            "_score" : 6.0,
            "_source" : {
              "title" : {
                "input" : "block",
                "weight" : 3
              }
            }
          },
          {
            "text" : "blow",
            "_index" : "s8",
            "_type" : "_doc",
            "_id" : "1",
            "_score" : 4.0,
            "_source" : {
              "title" : {
                "input" : "blow",
                "weight" : 2
              }
            }
          }
        ]
      }
    ]
  }
}
```
##### _source
为了减少不必要的响应，我们可以对建议结果做一些过滤，比如加上_source
```
GET /s8/_search
{
  "suggest": {
    "completion_suggest": {
      "text": "appl",
      "completion": {
        "field": "title"
      }
    }
  },
  "_source": "title"
}
#output
{
  "took" : 1,
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
  },
  "suggest" : {
    "completion_suggest" : [
      {
        "text" : "appl",
        "offset" : 0,
        "length" : 4,
        "options" : [
          {
            "text" : "apple",
            "_index" : "s8",
            "_type" : "_doc",
            "_id" : "3",
            "_score" : 3.0,
            "_source" : {
              "title" : [
                {
                  "input" : "appel",
                  "weight" : 2
                },
                {
                  "input" : "apple",
                  "weight" : 3
                }
              ]
            }
          },
          {
            "text" : "apple",
            "_index" : "s8",
            "_type" : "_doc",
            "_id" : "4",
            "_score" : 1.0,
            "_source" : {
              "title" : [
                "apple",
                "appel",
                "block",
                "blow"
              ]
            }
          }
        ]
      }
    ]
  }
}
```
##### size
size默认为5
```
GET /s8/_search
{
  "suggest": {
    "completion_suggest": {
      "prefix": "app",
      "completion": {
        "field": "title",
        "size": 1
      }
    }
  },
  "_source": "title"
}
#output
{
  "took" : 2,
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
  },
  "suggest" : {
    "completion_suggest" : [
      {
        "text" : "app",
        "offset" : 0,
        "length" : 3,
        "options" : [
          {
            "text" : "apple",
            "_index" : "s8",
            "_type" : "_doc",
            "_id" : "3",
            "_score" : 3.0,
            "_source" : {
              "title" : [
                {
                  "input" : "appel",
                  "weight" : 2
                },
                {
                  "input" : "apple",
                  "weight" : 3
                }
              ]
            }
          }
        ]
      }
    ]
  }
}
```
##### skip_duplicates
我们的建议可能是来自不同的文档，这其中就会有一些重复建议项，我们可以通过设置skip_duplicates:true来修改此行为，如果为true则会过滤掉结果中的重复建议文档
```
GET /s8/_search
{
  "suggest": {
    "completion_suggest": {
      "prefix": "app",
      "completion": {
        "field": "title",
        "size": 5,
        "skip_duplicates":true
      }
    }
  },
  "_source": "title"
}
```
但需要注意的是，该参数设置为true的话，可能会降低搜索速度，因为需要访问更多的建议结果项，才能过滤出来前N个。
最后，完成建议器还支持正则表达式查询，这意味着我们可以将前缀表示为正则表达式
```
GET /s8/_search
{
  "suggest": {
    "completion_suggest": {
      "regex": "e[l|e]a",
      "completion": {
        "field": "title"
      }
    }
  }
}
```
### context suggester
虽然完成建议器已经能返回所有和输入文本相匹配的结果，但有些使用案例需要过滤。这就要用到了上下文过滤器，它在完成建议器的基础上加入了过滤功能。
上下文建议器允许用户使用context上下文来进行过滤，上下文可以是分类（词条）或者地理位置，为了开启上下文，同样在映射中指定，然后在文档和建议中提供上下文。
完成建议器考虑索引中的所有文档，但通常我们希望提供某些标准过滤或者提升的建议。例如，我们想要推荐某些歌手过滤的歌曲标题，或者我们希望根据其类型推广歌曲标题。
要实现建议过滤或者提升，我们可以在配置完成字段时添加上下文映射，我们也可以为完成字段定义多个上下文映射，每个上下文映射都有唯一的名称和类型，有两种类型category和geo。上下文映射contexts在字段映射中的参数下配置。
注意：在索引查询启用上下文的完成字段时，必须提供上下文
```
PUT place
{
  "mappings": {
      "properties":{
        "title":{
          "type":"completion",
          "contexts":[
            {#定义category名为place_type的上下文，其中必须与建议一起发送类别。
              "name":"place_type", 
              "type": "category"
            },
            {# 定义一个geo名为location的上下文，其中必须使用建议发送类别
              "name":"location",
              "type":"geo",
              "precision": 4
            }
          ]
        }
      }
  }
}

PUT place_path_category
{
  "mappings": {
      "properties":{
        "title":{
          "type":"completion",
          "contexts":[
            {#定义category名为place_type的上下文，其中必须从cat字段字段中读取类别。
              "name":"place_type",
              "type":"category",
              "path":"cat"
            },
            {#定义geo名为location的上下文，其中从loc字段中读取类别。
              "name":"location",
              "type":"geo",
              "precision": 4,
              "path":"loc"
            }
          ]
        },
        "loc":{
          "type":"geo_point"
        }
      }
  }
}
```
添加上下文映射会增加完成字段的索引大小，完成索引完全是堆驻留的，我们可以使用Indices Stats监视完成字段索引的大小
#### 类别上下文
在category上下文允许我们将一个或多个类别与索引时间的建议关联，在查询时，建议可以通过其关联的类别进行过滤和提升。
映射的设置与place_type上面的字段类似，如果path已定义，则从文档中的该路径读取类别，否则必须在建议字段中发送它们，如下示例所示
```
PUT /place/_doc/1
{
  "title":{
    "input":["timmy's", "starbucks", "dunkin donuts"],
    "contexts":{
       "place_type":["cafe", "food"] # 这些建议将与咖啡馆和食品类别相关联
    }
  }
}
```
如果映射有path， 那么以下索引请求就可以添加类别
```
PUT /place_path_category/_doc/1
{
  "title":["timmy's", "sstarbucks", "dunkin donuts"],
  "cat":["cafe", "food"] 
}
```
如果上下文映射引用另一个字段并且类别被明确索引，则使用两组类别对建议进行索引

##### 类别查询

```
POST /place/_search
{
  "suggest":{
    "place_suggestion":{
      "prefix":"tim",
      "completion":{
        "field":"title",
        "size": 10,
        "contexts":{
          "place_type":["cafe", "restaurants"]
        }
      }
    }
  }
}
```
注意，如果在查询上设置了多个类别或者类别上下文，则将它们合并为分离。这意味着如果建议包含至少一个提供的上下文值，则建议匹配
某些类别的建议可能会比其他类别高，以下按类别过滤建议，并额外提升与某些类别相关的建议
```
POST /place/_search
{
  "suggest": {
    "place_suggestion": {
      "prefix": "tim",
      "completion": {
        "field": "title",
        "size": 10,
        "contexts":{
          "place_type":[ #上下文查询过滤建议与类别咖啡馆和餐馆相关联，并且通过因子增强与餐馆相关联的建议
            {
              "context":"cafe"
            },
            {
              "context":"restaurants", "boost":2
            }
          ]
        }
      }
    }
  }
}
```
除了接受类别值之外，上下文查询还可以由多个类别上下文子句组成，category上下文支持以下参数：
- context，要过滤/提升的类别的值，这是强制性的。
- boost，应该提高建议分数的因素，通过将boost乘以建议权重来计算分数，默认为1。
- prefix，是否应该将类别实为前缀，例如，如果设置为true，则可以通过指定类型的类别前缀来过滤type1，type2等类别，默认为false。

注意：如果建议条目与多个上下文匹配，则最终分数被计算为由任何匹配上下文产生的最大分数
#### 地理位置上下文
一个geo上下文允许我们将一个或多个地理位置或geohash与在索引时间的建议关联，在查询时，如果建议位于地理位置特定的距离内，则可以过滤和提升建议。
在内部，地位置被编码为具有指定精度的地理位置
##### 地理映射
除了path设置，geo上下文映射还接受以下设置：

- precision，它定义了地理散列的精度要被索引并且可以指定为一个距离值（5km，10km等），或作为原料地理散列精度（1 … 12）。默认为原始geohash精度值6
索引时间precision设置可以在查询时使用的最大geohash精度

**索引地理上下文**
geo上下文可以通过参数显式设置或通过path参数从文档中的地理点地段建立索引，类似于category上下文，将多个地理位置上下文与建立相关联，将为每个地理位置索引建议，以下索引具有两个地理位置上下文的建议：
```
PUT /place/_doc/2
{
  "title":{
    "input":"timmy's",
    "contexts":{
      "location":[
        {
          "lat":43.6624803,
          "lon":-79.3863353
        },
        {
          "lat":43.6624718,
          "lon":-79.3873327
        }
      ]
    }
  }
}
```

#### 地理位置查询
```
POST /place/_search
{
  "suggest": {
    "place_suggestion": {
      "prefix": "tim",
      "completion": {
        "field": "title",
        "size": 4,
        "contexts":{
          "location":{
            "lat": 43.662,
            "lon": -79.380
          }
        }
      }
    }
  }
}
#output
{
  "took" : 244,
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
  },
  "suggest" : {
    "place_suggestion" : [
      {
        "text" : "tim",
        "offset" : 0,
        "length" : 3,
        "options" : [
          {
            "text" : "timmy's",
            "_index" : "place",
            "_type" : "_doc",
            "_id" : "2",
            "_score" : 1.0,
            "_source" : {
              "title" : {
                "input" : "timmy's",
                "contexts" : {
                  "location" : [
                    {
                      "lat" : 43.6624803,
                      "lon" : -79.3863353
                    },
                    {
                      "lat" : 43.6624718,
                      "lon" : -79.3873327
                    }
                  ]
                }
              }
            },
            "contexts" : {
              "location" : [
                "dpz8"
              ]
            }
          }
        ]
      }
    ]
  }
}

```
注意：当指定查询精度较低的位置时，将考虑属于该区域内的所有建议。如果在查询上设置了多个类别或类别上下文，则将它们合并为分离，这意味着如果建议包含至少一个提供的上下文值，则建议才匹配
在geohash所代表的区域内的建议也可以比其他建议更高，如下所示
```
POST /place/_search
{
  "suggest": {
    "place_suggestion": {
      "prefix": "tim",
      "completion": {
        "field": "title",
        "size":10,
        "contexts":{
          "location":[ 
            {
              "lat": 43.6624803,
              "lon": -79.3863353,
              "precision": 2
            },
            {
              "context":{
                "lat": 43.6624803,
                "lon":-79.3863353
              },
              "boost": 2
            }
          ]
        }
      }
    }
  }
}
#上下文查询过滤属于geohash（43.662，-79.380）表示的地理位置的建议，精度为2，并提升属于（43.6624803，-79.3863353）geohash表示的建议，默认精度为6，因数为2
```
注意：如果建议条目与多个上下文匹配，则最终分数被计算为由任何匹配上下文产生的最大分数。
除了接受上下文值之外，上下文查询还可以由多个上下文子句组成，category上下文子句支持一下参数：
- context，地理点对象或地理哈希字符串，用于过滤提升建议，这是强制性的。
- boost，应该提高建议分数的因素，通过将boost乘以建议权重来计算分数，默认为1。
- precision，geohash对查询地理点进行编码的精度，这可以被指定为一个距离值（5m，10km等），或作为原料地理散列精度（1 … 12）。默认为索引时间精度级别。
- neighbours，接受应该考虑相邻地理位置的精度值数组，精度值可以是距离值（5m， 10km等）或一个原始地理散列精度（1 … 12）。默认为索引时间精度级别生成的临近值。


### 过程
当数据被发送到elasticsearch后并加入到倒排索引之前，elasticsearch会对该文档的进行一系列的处理步骤：
- 字符过滤：使用字符过滤器转变字符。
- 文本切分为分词：将文本（档）分为单个或多个分词。
- 分词过滤：使用分词过滤器转变每个分词。
- 分词索引：最终将分词存储在Lucene倒排索引中。

### 分析器
一个分析器可以包含：
- 字符过滤器 （可选）
- 一个分词器
- 0个或者多个分词过滤器 

#### standard analyzer
标准分析器（standard analyzer）：是elasticsearch的默认分析器，该分析器综合了大多数欧洲语言来说合理的默认模块，包括标准分词器、标准分词过滤器、小写转换分词过滤器和停用词分词过滤器
```
POST _analyze
{
  "analyzer": "standard",
  "text":"To be or not to be,  That is a question ———— 莎士比亚"
}

#output
{
  "tokens" : [
    {
      "token" : "to",
      "start_offset" : 0,
      "end_offset" : 2,
      "type" : "<ALPHANUM>",
      "position" : 0
    },
    {
      "token" : "be",
      "start_offset" : 3,
      "end_offset" : 5,
      "type" : "<ALPHANUM>",
      "position" : 1
    },
    {
      "token" : "or",
      "start_offset" : 6,
      "end_offset" : 8,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "not",
      "start_offset" : 9,
      "end_offset" : 12,
      "type" : "<ALPHANUM>",
      "position" : 3
    },
    {
      "token" : "to",
      "start_offset" : 13,
      "end_offset" : 15,
      "type" : "<ALPHANUM>",
      "position" : 4
    },
    {
      "token" : "be",
      "start_offset" : 16,
      "end_offset" : 18,
      "type" : "<ALPHANUM>",
      "position" : 5
    },
    {
      "token" : "that",
      "start_offset" : 21,
      "end_offset" : 25,
      "type" : "<ALPHANUM>",
      "position" : 6
    },
    {
      "token" : "is",
      "start_offset" : 26,
      "end_offset" : 28,
      "type" : "<ALPHANUM>",
      "position" : 7
    },
    {
      "token" : "a",
      "start_offset" : 29,
      "end_offset" : 30,
      "type" : "<ALPHANUM>",
      "position" : 8
    },
    {
      "token" : "question",
      "start_offset" : 31,
      "end_offset" : 39,
      "type" : "<ALPHANUM>",
      "position" : 9
    },
    {
      "token" : "莎",
      "start_offset" : 45,
      "end_offset" : 46,
      "type" : "<IDEOGRAPHIC>",
      "position" : 10
    },
    {
      "token" : "士",
      "start_offset" : 46,
      "end_offset" : 47,
      "type" : "<IDEOGRAPHIC>",
      "position" : 11
    },
    {
      "token" : "比",
      "start_offset" : 47,
      "end_offset" : 48,
      "type" : "<IDEOGRAPHIC>",
      "position" : 12
    },
    {
      "token" : "亚",
      "start_offset" : 48,
      "end_offset" : 49,
      "type" : "<IDEOGRAPHIC>",
      "position" : 13
    }
  ]
}

```

#### simple analyzer
简单分析器（simple analyzer）：简单分析器仅使用了小写转换分词，这意味着在非字母处进行分词，并将分词自动转换为小写。这个分词器对于亚种语言来说效果不佳，因为亚洲语言不是根据空白来分词的，所以一般用于欧洲言中

```
POST _analyze
{
  "analyzer": "simple",
  "text":"To be or not to be,  That is a question ———— 莎士比亚"
}
#output
{
  "tokens" : [
    {
      "token" : "to",
      "start_offset" : 0,
      "end_offset" : 2,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "be",
      "start_offset" : 3,
      "end_offset" : 5,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "or",
      "start_offset" : 6,
      "end_offset" : 8,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "not",
      "start_offset" : 9,
      "end_offset" : 12,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "to",
      "start_offset" : 13,
      "end_offset" : 15,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "be",
      "start_offset" : 16,
      "end_offset" : 18,
      "type" : "word",
      "position" : 5
    },
    {
      "token" : "that",
      "start_offset" : 21,
      "end_offset" : 25,
      "type" : "word",
      "position" : 6
    },
    {
      "token" : "is",
      "start_offset" : 26,
      "end_offset" : 28,
      "type" : "word",
      "position" : 7
    },
    {
      "token" : "a",
      "start_offset" : 29,
      "end_offset" : 30,
      "type" : "word",
      "position" : 8
    },
    {
      "token" : "question",
      "start_offset" : 31,
      "end_offset" : 39,
      "type" : "word",
      "position" : 9
    },
    {
      "token" : "莎士比亚",
      "start_offset" : 45,
      "end_offset" : 49,
      "type" : "word",
      "position" : 10
    }
  ]
}

```
#### whitespace analyzer
空白（格）分析器（whitespace analyzer）：这玩意儿只是根据空白将文本切分为若干分词，真是有够偷懒！
```
POST _analyze
{
  "analyzer": "whitespace",
  "text":"To be or not to be,  That is a question ———— 莎士比亚"
}
#output
{
  "tokens" : [
    {
      "token" : "To",
      "start_offset" : 0,
      "end_offset" : 2,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "be",
      "start_offset" : 3,
      "end_offset" : 5,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "or",
      "start_offset" : 6,
      "end_offset" : 8,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "not",
      "start_offset" : 9,
      "end_offset" : 12,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "to",
      "start_offset" : 13,
      "end_offset" : 15,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "be,",
      "start_offset" : 16,
      "end_offset" : 19,
      "type" : "word",
      "position" : 5
    },
    {
      "token" : "That",
      "start_offset" : 21,
      "end_offset" : 25,
      "type" : "word",
      "position" : 6
    },
    {
      "token" : "is",
      "start_offset" : 26,
      "end_offset" : 28,
      "type" : "word",
      "position" : 7
    },
    {
      "token" : "a",
      "start_offset" : 29,
      "end_offset" : 30,
      "type" : "word",
      "position" : 8
    },
    {
      "token" : "question",
      "start_offset" : 31,
      "end_offset" : 39,
      "type" : "word",
      "position" : 9
    },
    {
      "token" : "————",
      "start_offset" : 40,
      "end_offset" : 44,
      "type" : "word",
      "position" : 10
    },
    {
      "token" : "莎士比亚",
      "start_offset" : 45,
      "end_offset" : 49,
      "type" : "word",
      "position" : 11
    }
  ]
}

```

#### stop analyzer
停用词分析（stop analyzer）和简单分析器的行为很像，只是在分词流中额外的过滤了停用词。
```
POST _analyze
{
  "analyzer": "stop",
  "text":"To be or not to be,  That is a question ———— 莎士比亚"
}
{
  "tokens" : [
    {
      "token" : "question",
      "start_offset" : 31,
      "end_offset" : 39,
      "type" : "word",
      "position" : 9
    },
    {
      "token" : "莎士比亚",
      "start_offset" : 45,
      "end_offset" : 49,
      "type" : "word",
      "position" : 10
    }
  ]
}

```
#### keyword analyzer
关键词分析器（keyword analyzer）将整个字段当做单独的分词，如无必要，我们不在映射中使用关键词分析器
```
POST _analyze
{
  "analyzer": "keyword",
  "text":"To be or not to be,  That is a question ———— 莎士比亚"
}
#output
{
  "tokens" : [
    {
      "token" : "To be or not to be,  That is a question ———— 莎士比亚",
      "start_offset" : 0,
      "end_offset" : 49,
      "type" : "word",
      "position" : 0
    }
  ]
}

```

#### pattern analyzer
模式分析器（pattern analyzer）允许我们指定一个分词切分模式。但是通常更佳的方案是使用定制的分析器，组合现有的模式分词器和所需要的分词过滤器更加合适。
```
POST _analyze
{
  "analyzer": "pattern",
  "explain": false, 
  "text":"To be or not to be,  That is a question ———— 莎士比亚"
}
#output
{
  "tokens" : [
    {
      "token" : "to",
      "start_offset" : 0,
      "end_offset" : 2,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "be",
      "start_offset" : 3,
      "end_offset" : 5,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "or",
      "start_offset" : 6,
      "end_offset" : 8,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "not",
      "start_offset" : 9,
      "end_offset" : 12,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "to",
      "start_offset" : 13,
      "end_offset" : 15,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "be",
      "start_offset" : 16,
      "end_offset" : 18,
      "type" : "word",
      "position" : 5
    },
    {
      "token" : "that",
      "start_offset" : 21,
      "end_offset" : 25,
      "type" : "word",
      "position" : 6
    },
    {
      "token" : "is",
      "start_offset" : 26,
      "end_offset" : 28,
      "type" : "word",
      "position" : 7
    },
    {
      "token" : "a",
      "start_offset" : 29,
      "end_offset" : 30,
      "type" : "word",
      "position" : 8
    },
    {
      "token" : "question",
      "start_offset" : 31,
      "end_offset" : 39,
      "type" : "word",
      "position" : 9
    }
  ]
}
```
##### 自定义模式分析器，比如我们写匹配邮箱的正则。

```
PUT pattern_test
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_email_analyzer":{
          "type":"pattern",
          "pattern":"\\W|_",
          "lowercase":true
        }
      }
    }
  }
}

POST pattern_test/_analyze
{
  "analyzer": "my_email_analyzer",
  "text": "John_Smith@foo-bar.com"
}
#output
{
  "tokens" : [
    {
      "token" : "john",
      "start_offset" : 0,
      "end_offset" : 4,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "smith",
      "start_offset" : 5,
      "end_offset" : 10,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "foo",
      "start_offset" : 11,
      "end_offset" : 14,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "bar",
      "start_offset" : 15,
      "end_offset" : 18,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "com",
      "start_offset" : 19,
      "end_offset" : 22,
      "type" : "word",
      "position" : 4
    }
  ]
}

```
#### chinese
语言和多语言分析器
```
POST _analyze
{
  "analyzer": "chinese",
  "text":"To be or not to be,  That is a question ———— 莎士比亚"
}
#output
{
  "tokens" : [
    {
      "token" : "question",
      "start_offset" : 31,
      "end_offset" : 39,
      "type" : "<ALPHANUM>",
      "position" : 9
    },
    {
      "token" : "莎",
      "start_offset" : 45,
      "end_offset" : 46,
      "type" : "<IDEOGRAPHIC>",
      "position" : 10
    },
    {
      "token" : "士",
      "start_offset" : 46,
      "end_offset" : 47,
      "type" : "<IDEOGRAPHIC>",
      "position" : 11
    },
    {
      "token" : "比",
      "start_offset" : 47,
      "end_offset" : 48,
      "type" : "<IDEOGRAPHIC>",
      "position" : 12
    },
    {
      "token" : "亚",
      "start_offset" : 48,
      "end_offset" : 49,
      "type" : "<IDEOGRAPHIC>",
      "position" : 13
    }
  ]
}

```
#### snowball analyzer
雪球分析器（snowball analyzer）除了使用标准的分词和分词过滤器（和标准分析器一样）也是用了小写分词过滤器和停用词过滤器，除此之外，它还是用了雪球词干器对文本进行词干提取
```
POST _analyze
{
  "analyzer": "snowball",
  "text":"To be or not to be,  That is a question ———— 莎士比亚"
}
#output
{
  "tokens" : [
    {
      "token" : "question",
      "start_offset" : 31,
      "end_offset" : 39,
      "type" : "<ALPHANUM>",
      "position" : 9
    },
    {
      "token" : "莎",
      "start_offset" : 45,
      "end_offset" : 46,
      "type" : "<IDEOGRAPHIC>",
      "position" : 10
    },
    {
      "token" : "士",
      "start_offset" : 46,
      "end_offset" : 47,
      "type" : "<IDEOGRAPHIC>",
      "position" : 11
    },
    {
      "token" : "比",
      "start_offset" : 47,
      "end_offset" : 48,
      "type" : "<IDEOGRAPHIC>",
      "position" : 12
    },
    {
      "token" : "亚",
      "start_offset" : 48,
      "end_offset" : 49,
      "type" : "<IDEOGRAPHIC>",
      "position" : 13
    }
  ]
}

```

### 字符过滤器
字符过滤器在 `<charFilter>`属性中定义，它是对字符流进行处理。字符过滤器种类不多。elasticearch只提供了三种字符过滤器：
- HTML字符过滤器（HTML Strip Char Filter）
- 映射字符过滤器（Mapping Char Filter）
- 模式替换过滤器（Pattern Replace Char Filter）

#### HTML
```
POST _analyze
{
  "tokenizer": "keyword",
  "char_filter": ["html_strip"],
  "text":"<p>I&apos;m so <b>happy</b>!</p>"
}

{
  "tokens" : [
    {
      "token" : """
I'm so happy!
""",
      "start_offset" : 0,
      "end_offset" : 32,
      "type" : "word",
      "position" : 0
    }
  ]
}
```
#### mapping
映射字符过滤器（Mapping Char Filter）接收键值的映射，每当遇到与键相同的字符串时，它就用该键关联的值替换它们
```
PUT pattern_test1
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer":{
          "tokenizer":"keyword",
          "char_filter":["my_char_filter"]
        }
      },
      "char_filter":{
          "my_char_filter":{
            "type":"mapping",
            "mappings":["小明 => 666","小红 => 888"]
          }
        }
    }
  }
}
POST pattern_test1/_analyze
{
  "analyzer": "my_analyzer",
  "text": "小明爱小红，可惜后来小红结婚了"
}
{
  "tokens" : [
    {
      "token" : "666爱888，可惜后来888结婚了",
      "start_offset" : 0,
      "end_offset" : 15,
      "type" : "word",
      "position" : 0
    }
  ]
}
```
#### pattern
模式替换过滤器（Pattern Replace Char Filter）使用正则表达式匹配并替换字符串中的字符。但要小心你写的抠脚的正则表达式。因为这可能导致性能变慢
```
PUT pattern_test2
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "tokenizer": "standard",
          "char_filter": [
            "my_char_filter"
          ]
        }
      },
      "char_filter": {
        "my_char_filter": {
          "type": "pattern_replace",
          "pattern": "(\\d+)-(?=\\d)",
          "replacement": "$1_"
        }
      }
    }
  }
}

POST pattern_test2/_analyze
{
  "analyzer": "my_analyzer",
  "text": "My credit card is 123-456-789"
}
{
  "tokens" : [
    {
      "token" : "My",
      "start_offset" : 0,
      "end_offset" : 2,
      "type" : "<ALPHANUM>",
      "position" : 0
    },
    {
      "token" : "credit",
      "start_offset" : 3,
      "end_offset" : 9,
      "type" : "<ALPHANUM>",
      "position" : 1
    },
    {
      "token" : "card",
      "start_offset" : 10,
      "end_offset" : 14,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "is",
      "start_offset" : 15,
      "end_offset" : 17,
      "type" : "<ALPHANUM>",
      "position" : 3
    },
    {
      "token" : "123_456_789",
      "start_offset" : 18,
      "end_offset" : 29,
      "type" : "<NUM>",
      "position" : 4
    }
  ]
}

```

### 分词器
由于elasticsearch内置了分析器，它同样也包含了分词器。分词器，顾名思义，主要的操作是将文本字符串分解为小块，而这些小块这被称为分词token

#### standard tokenizer
标准分词器（standard tokenizer）是一个基于语法的分词器，对于大多数欧洲语言来说还是不错的，它同时还处理了Unicode文本的分词，但分词默认的最大长度是255字节，它也移除了逗号和句号这样的标点符号
```
POST _analyze
{
  "tokenizer": "standard",
  "text":"To be or not to be,  That is a question ———— 莎士比亚"
}

{
  "tokens" : [
    {
      "token" : "To",
      "start_offset" : 0,
      "end_offset" : 2,
      "type" : "<ALPHANUM>",
      "position" : 0
    },
    {
      "token" : "be",
      "start_offset" : 3,
      "end_offset" : 5,
      "type" : "<ALPHANUM>",
      "position" : 1
    },
    {
      "token" : "or",
      "start_offset" : 6,
      "end_offset" : 8,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "not",
      "start_offset" : 9,
      "end_offset" : 12,
      "type" : "<ALPHANUM>",
      "position" : 3
    },
    {
      "token" : "to",
      "start_offset" : 13,
      "end_offset" : 15,
      "type" : "<ALPHANUM>",
      "position" : 4
    },
    {
      "token" : "be",
      "start_offset" : 16,
      "end_offset" : 18,
      "type" : "<ALPHANUM>",
      "position" : 5
    },
    {
      "token" : "That",
      "start_offset" : 21,
      "end_offset" : 25,
      "type" : "<ALPHANUM>",
      "position" : 6
    },
    {
      "token" : "is",
      "start_offset" : 26,
      "end_offset" : 28,
      "type" : "<ALPHANUM>",
      "position" : 7
    },
    {
      "token" : "a",
      "start_offset" : 29,
      "end_offset" : 30,
      "type" : "<ALPHANUM>",
      "position" : 8
    },
    {
      "token" : "question",
      "start_offset" : 31,
      "end_offset" : 39,
      "type" : "<ALPHANUM>",
      "position" : 9
    },
    {
      "token" : "莎",
      "start_offset" : 45,
      "end_offset" : 46,
      "type" : "<IDEOGRAPHIC>",
      "position" : 10
    },
    {
      "token" : "士",
      "start_offset" : 46,
      "end_offset" : 47,
      "type" : "<IDEOGRAPHIC>",
      "position" : 11
    },
    {
      "token" : "比",
      "start_offset" : 47,
      "end_offset" : 48,
      "type" : "<IDEOGRAPHIC>",
      "position" : 12
    },
    {
      "token" : "亚",
      "start_offset" : 48,
      "end_offset" : 49,
      "type" : "<IDEOGRAPHIC>",
      "position" : 13
    }
  ]
}

```

#### keyword tokenizer
关键词分词器（keyword tokenizer）是一种简单的分词器，将整个文本作为单个的分词，提供给分词过滤器，当你只想用分词过滤器，而不做分词操作时，它是不错的选择
```
POST _analyze
{
  "tokenizer": "keyword",
  "text":"To be or not to be,  That is a question ———— 莎士比亚"
}
{
  "tokens" : [
    {
      "token" : "To be or not to be,  That is a question ———— 莎士比亚",
      "start_offset" : 0,
      "end_offset" : 49,
      "type" : "word",
      "position" : 0
    }
  ]
}

```
#### letter tokenizer
字母分词器（letter tokenizer）根据非字母的符号，将文本切分成分词

```
POST _analyze
{
  "tokenizer": "letter",
  "text":"To be or not to be,  That is a question ———— 莎士比亚"
}
{
  "tokens" : [
    {
      "token" : "To",
      "start_offset" : 0,
      "end_offset" : 2,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "be",
      "start_offset" : 3,
      "end_offset" : 5,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "or",
      "start_offset" : 6,
      "end_offset" : 8,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "not",
      "start_offset" : 9,
      "end_offset" : 12,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "to",
      "start_offset" : 13,
      "end_offset" : 15,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "be",
      "start_offset" : 16,
      "end_offset" : 18,
      "type" : "word",
      "position" : 5
    },
    {
      "token" : "That",
      "start_offset" : 21,
      "end_offset" : 25,
      "type" : "word",
      "position" : 6
    },
    {
      "token" : "is",
      "start_offset" : 26,
      "end_offset" : 28,
      "type" : "word",
      "position" : 7
    },
    {
      "token" : "a",
      "start_offset" : 29,
      "end_offset" : 30,
      "type" : "word",
      "position" : 8
    },
    {
      "token" : "question",
      "start_offset" : 31,
      "end_offset" : 39,
      "type" : "word",
      "position" : 9
    },
    {
      "token" : "莎士比亚",
      "start_offset" : 45,
      "end_offset" : 49,
      "type" : "word",
      "position" : 10
    }
  ]
}

```

#### lowercase tokenizer
小写分词器（lowercase tokenizer）结合了常规的字母分词器和小写分词过滤器（跟你想的一样，就是将所有的分词转化为小写）的行为。通过一个单独的分词器来实现的主要原因是，一次进行两项操作会获得更好的性能

```
POST _analyze
{
  "tokenizer": "lowercase",
  "text":"To be or not to be,  That is a question ———— 莎士比亚"
}

{
  "tokens" : [
    {
      "token" : "to",
      "start_offset" : 0,
      "end_offset" : 2,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "be",
      "start_offset" : 3,
      "end_offset" : 5,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "or",
      "start_offset" : 6,
      "end_offset" : 8,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "not",
      "start_offset" : 9,
      "end_offset" : 12,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "to",
      "start_offset" : 13,
      "end_offset" : 15,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "be",
      "start_offset" : 16,
      "end_offset" : 18,
      "type" : "word",
      "position" : 5
    },
    {
      "token" : "that",
      "start_offset" : 21,
      "end_offset" : 25,
      "type" : "word",
      "position" : 6
    },
    {
      "token" : "is",
      "start_offset" : 26,
      "end_offset" : 28,
      "type" : "word",
      "position" : 7
    },
    {
      "token" : "a",
      "start_offset" : 29,
      "end_offset" : 30,
      "type" : "word",
      "position" : 8
    },
    {
      "token" : "question",
      "start_offset" : 31,
      "end_offset" : 39,
      "type" : "word",
      "position" : 9
    },
    {
      "token" : "莎士比亚",
      "start_offset" : 45,
      "end_offset" : 49,
      "type" : "word",
      "position" : 10
    }
  ]
}

```

#### whitespace tokenizer
空白分词器（whitespace tokenizer）通过空白来分隔不同的分词，空白包括空格、制表符、换行等。但是，我们需要注意的是，空白分词器不会删除任何标点符号

```
POST _analyze
{
  "tokenizer": "whitespace",
  "text":"To be or not to be,  That is a question ———— 莎士比亚"
}
{
  "tokens" : [
    {
      "token" : "To",
      "start_offset" : 0,
      "end_offset" : 2,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "be",
      "start_offset" : 3,
      "end_offset" : 5,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "or",
      "start_offset" : 6,
      "end_offset" : 8,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "not",
      "start_offset" : 9,
      "end_offset" : 12,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "to",
      "start_offset" : 13,
      "end_offset" : 15,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "be,",
      "start_offset" : 16,
      "end_offset" : 19,
      "type" : "word",
      "position" : 5
    },
    {
      "token" : "That",
      "start_offset" : 21,
      "end_offset" : 25,
      "type" : "word",
      "position" : 6
    },
    {
      "token" : "is",
      "start_offset" : 26,
      "end_offset" : 28,
      "type" : "word",
      "position" : 7
    },
    {
      "token" : "a",
      "start_offset" : 29,
      "end_offset" : 30,
      "type" : "word",
      "position" : 8
    },
    {
      "token" : "question",
      "start_offset" : 31,
      "end_offset" : 39,
      "type" : "word",
      "position" : 9
    },
    {
      "token" : "————",
      "start_offset" : 40,
      "end_offset" : 44,
      "type" : "word",
      "position" : 10
    },
    {
      "token" : "莎士比亚",
      "start_offset" : 45,
      "end_offset" : 49,
      "type" : "word",
      "position" : 11
    }
  ]
}

```
#### pattern tokenizer
模式分词器（pattern tokenizer）允许指定一个任意的模式，将文本切分为分词
```
POST _analyze
{
  "tokenizer": "pattern",
  "text":"To be or not to be,  That is a question ———— 莎士比亚"
}

{
  "tokens" : [
    {
      "token" : "To",
      "start_offset" : 0,
      "end_offset" : 2,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "be",
      "start_offset" : 3,
      "end_offset" : 5,
      "type" : "word",
      "position" : 1
    },
    {
      "token" : "or",
      "start_offset" : 6,
      "end_offset" : 8,
      "type" : "word",
      "position" : 2
    },
    {
      "token" : "not",
      "start_offset" : 9,
      "end_offset" : 12,
      "type" : "word",
      "position" : 3
    },
    {
      "token" : "to",
      "start_offset" : 13,
      "end_offset" : 15,
      "type" : "word",
      "position" : 4
    },
    {
      "token" : "be",
      "start_offset" : 16,
      "end_offset" : 18,
      "type" : "word",
      "position" : 5
    },
    {
      "token" : "That",
      "start_offset" : 21,
      "end_offset" : 25,
      "type" : "word",
      "position" : 6
    },
    {
      "token" : "is",
      "start_offset" : 26,
      "end_offset" : 28,
      "type" : "word",
      "position" : 7
    },
    {
      "token" : "a",
      "start_offset" : 29,
      "end_offset" : 30,
      "type" : "word",
      "position" : 8
    },
    {
      "token" : "question",
      "start_offset" : 31,
      "end_offset" : 39,
      "type" : "word",
      "position" : 9
    }
  ]
}

```
现在让我们手动定制一个以逗号分隔的分词器
```
PUT pattern_test3
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_analyzer":{
          "tokenizer":"my_tokenizer"
        }
      },
      "tokenizer": {
        "my_tokenizer":{
          "type":"pattern",
          "pattern":","
        }
      }
    }
  }
}
```
上例中，在settings下的自定义分析器my_analyzer中，自定义的模式分词器名叫my_tokenizer；在与自定义分析器同级，为新建的自定义模式分词器设置一些属性，比如以逗号分隔。
```
POST pattern_test3/_analyze
{
  "tokenizer": "my_tokenizer",
  "text":"To be or not to be,  That is a question ———— 莎士比亚"
}
{
  "tokens" : [
    {
      "token" : "To be or not to be",
      "start_offset" : 0,
      "end_offset" : 18,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "  That is a question ———— 莎士比亚",
      "start_offset" : 19,
      "end_offset" : 49,
      "type" : "word",
      "position" : 1
    }
  ]
}

```
#### UAX RUL email tokenizer
在处理单个的英文单词的情况下，标准分词器是个非常好的选择，但是现在很多的网站以网址或电子邮件作为结尾，比如我们现在有这样的一个文本：
```
作者：Andy
来源：未知 
原文：https://www.cnblogs.com/Andy963/
邮箱：xxxxxxx@xx.com
版权声明：本文为博主原创文章，转载请附上博文链接！
```
```
POST _analyze
{
  "tokenizer": "standard",
  "text":"作者：Andy 来源：未知  原文：https://www.cnblogs.com/Andy963/ 邮箱：xxxxxxx@xx.com 版权声明：本文为博主原创文章，转载请附上博文链接！！"
}
{
  "tokens" : [
    {
      "token" : "作",
      "start_offset" : 0,
      "end_offset" : 1,
      "type" : "<IDEOGRAPHIC>",
      "position" : 0
    },
    {
      "token" : "者",
      "start_offset" : 1,
      "end_offset" : 2,
      "type" : "<IDEOGRAPHIC>",
      "position" : 1
    },
    {
      "token" : "Andy",
      "start_offset" : 3,
      "end_offset" : 7,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "来",
      "start_offset" : 8,
      "end_offset" : 9,
      "type" : "<IDEOGRAPHIC>",
      "position" : 3
    },
    {
      "token" : "源",
      "start_offset" : 9,
      "end_offset" : 10,
      "type" : "<IDEOGRAPHIC>",
      "position" : 4
    },
    {
      "token" : "未",
      "start_offset" : 11,
      "end_offset" : 12,
      "type" : "<IDEOGRAPHIC>",
      "position" : 5
    },
    {
      "token" : "知",
      "start_offset" : 12,
      "end_offset" : 13,
      "type" : "<IDEOGRAPHIC>",
      "position" : 6
    },
    {
      "token" : "原",
      "start_offset" : 15,
      "end_offset" : 16,
      "type" : "<IDEOGRAPHIC>",
      "position" : 7
    },
    {
      "token" : "文",
      "start_offset" : 16,
      "end_offset" : 17,
      "type" : "<IDEOGRAPHIC>",
      "position" : 8
    },
    {
      "token" : "https",
      "start_offset" : 18,
      "end_offset" : 23,
      "type" : "<ALPHANUM>",
      "position" : 9
    },
    {
      "token" : "www.cnblogs.com",
      "start_offset" : 26,
      "end_offset" : 41,
      "type" : "<ALPHANUM>",
      "position" : 10
    },
    {
      "token" : "Andy963",
      "start_offset" : 42,
      "end_offset" : 49,
      "type" : "<ALPHANUM>",
      "position" : 11
    },
    {
      "token" : "邮",
      "start_offset" : 51,
      "end_offset" : 52,
      "type" : "<IDEOGRAPHIC>",
      "position" : 12
    },
    {
      "token" : "箱",
      "start_offset" : 52,
      "end_offset" : 53,
      "type" : "<IDEOGRAPHIC>",
      "position" : 13
    },
    {
      "token" : "xxxxxxx",
      "start_offset" : 54,
      "end_offset" : 61,
      "type" : "<ALPHANUM>",
      "position" : 14
    },
    {
      "token" : "xx.com",
      "start_offset" : 62,
      "end_offset" : 68,
      "type" : "<ALPHANUM>",
      "position" : 15
    },
    {
      "token" : "版",
      "start_offset" : 69,
      "end_offset" : 70,
      "type" : "<IDEOGRAPHIC>",
      "position" : 16
    },
    {
      "token" : "权",
      "start_offset" : 70,
      "end_offset" : 71,
      "type" : "<IDEOGRAPHIC>",
      "position" : 17
    },
    {
      "token" : "声",
      "start_offset" : 71,
      "end_offset" : 72,
      "type" : "<IDEOGRAPHIC>",
      "position" : 18
    },
    {
      "token" : "明",
      "start_offset" : 72,
      "end_offset" : 73,
      "type" : "<IDEOGRAPHIC>",
      "position" : 19
    },
    {
      "token" : "本",
      "start_offset" : 74,
      "end_offset" : 75,
      "type" : "<IDEOGRAPHIC>",
      "position" : 20
    },
    {
      "token" : "文",
      "start_offset" : 75,
      "end_offset" : 76,
      "type" : "<IDEOGRAPHIC>",
      "position" : 21
    },
    {
      "token" : "为",
      "start_offset" : 76,
      "end_offset" : 77,
      "type" : "<IDEOGRAPHIC>",
      "position" : 22
    },
    {
      "token" : "博",
      "start_offset" : 77,
      "end_offset" : 78,
      "type" : "<IDEOGRAPHIC>",
      "position" : 23
    },
    {
      "token" : "主",
      "start_offset" : 78,
      "end_offset" : 79,
      "type" : "<IDEOGRAPHIC>",
      "position" : 24
    },
    {
      "token" : "原",
      "start_offset" : 79,
      "end_offset" : 80,
      "type" : "<IDEOGRAPHIC>",
      "position" : 25
    },
    {
      "token" : "创",
      "start_offset" : 80,
      "end_offset" : 81,
      "type" : "<IDEOGRAPHIC>",
      "position" : 26
    },
    {
      "token" : "文",
      "start_offset" : 81,
      "end_offset" : 82,
      "type" : "<IDEOGRAPHIC>",
      "position" : 27
    },
    {
      "token" : "章",
      "start_offset" : 82,
      "end_offset" : 83,
      "type" : "<IDEOGRAPHIC>",
      "position" : 28
    },
    {
      "token" : "转",
      "start_offset" : 84,
      "end_offset" : 85,
      "type" : "<IDEOGRAPHIC>",
      "position" : 29
    },
    {
      "token" : "载",
      "start_offset" : 85,
      "end_offset" : 86,
      "type" : "<IDEOGRAPHIC>",
      "position" : 30
    },
    {
      "token" : "请",
      "start_offset" : 86,
      "end_offset" : 87,
      "type" : "<IDEOGRAPHIC>",
      "position" : 31
    },
    {
      "token" : "附",
      "start_offset" : 87,
      "end_offset" : 88,
      "type" : "<IDEOGRAPHIC>",
      "position" : 32
    },
    {
      "token" : "上",
      "start_offset" : 88,
      "end_offset" : 89,
      "type" : "<IDEOGRAPHIC>",
      "position" : 33
    },
    {
      "token" : "博",
      "start_offset" : 89,
      "end_offset" : 90,
      "type" : "<IDEOGRAPHIC>",
      "position" : 34
    },
    {
      "token" : "文",
      "start_offset" : 90,
      "end_offset" : 91,
      "type" : "<IDEOGRAPHIC>",
      "position" : 35
    },
    {
      "token" : "链",
      "start_offset" : 91,
      "end_offset" : 92,
      "type" : "<IDEOGRAPHIC>",
      "position" : 36
    },
    {
      "token" : "接",
      "start_offset" : 92,
      "end_offset" : 93,
      "type" : "<IDEOGRAPHIC>",
      "position" : 37
    }
  ]
}

```
无论如何，这个结果不符合我们的预期，因为把我们的邮箱和网址分的乱七八糟！那么针对这种情况，我们应该使用UAX URL电子邮件分词器（UAX RUL email tokenizer），该分词器将电子邮件和URL都作为单独的分词进行保留
```
POST _analyze
{
  "tokenizer": "uax_url_email",
  "text":"作者：Andy 来源：未知  原文：https://www.cnblogs.com/Andy963/ 邮箱：xxxxxxx@xx.com 版权声明：本文为博主原创文章，转载请附上博文链接！！"
}
{
  "tokens" : [
    {
      "token" : "作",
      "start_offset" : 0,
      "end_offset" : 1,
      "type" : "<IDEOGRAPHIC>",
      "position" : 0
    },
    {
      "token" : "者",
      "start_offset" : 1,
      "end_offset" : 2,
      "type" : "<IDEOGRAPHIC>",
      "position" : 1
    },
    {
      "token" : "Andy",
      "start_offset" : 3,
      "end_offset" : 7,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "来",
      "start_offset" : 8,
      "end_offset" : 9,
      "type" : "<IDEOGRAPHIC>",
      "position" : 3
    },
    {
      "token" : "源",
      "start_offset" : 9,
      "end_offset" : 10,
      "type" : "<IDEOGRAPHIC>",
      "position" : 4
    },
    {
      "token" : "未",
      "start_offset" : 11,
      "end_offset" : 12,
      "type" : "<IDEOGRAPHIC>",
      "position" : 5
    },
    {
      "token" : "知",
      "start_offset" : 12,
      "end_offset" : 13,
      "type" : "<IDEOGRAPHIC>",
      "position" : 6
    },
    {
      "token" : "原",
      "start_offset" : 15,
      "end_offset" : 16,
      "type" : "<IDEOGRAPHIC>",
      "position" : 7
    },
    {
      "token" : "文",
      "start_offset" : 16,
      "end_offset" : 17,
      "type" : "<IDEOGRAPHIC>",
      "position" : 8
    },
    {
      "token" : "https://www.cnblogs.com/Andy963/",
      "start_offset" : 18,
      "end_offset" : 50,
      "type" : "<URL>",
      "position" : 9
    },
    {
      "token" : "邮",
      "start_offset" : 51,
      "end_offset" : 52,
      "type" : "<IDEOGRAPHIC>",
      "position" : 10
    },
    {
      "token" : "箱",
      "start_offset" : 52,
      "end_offset" : 53,
      "type" : "<IDEOGRAPHIC>",
      "position" : 11
    },
    {
      "token" : "xxxxxxx@xx.com",
      "start_offset" : 54,
      "end_offset" : 68,
      "type" : "<EMAIL>",
      "position" : 12
    },
    {
      "token" : "版",
      "start_offset" : 69,
      "end_offset" : 70,
      "type" : "<IDEOGRAPHIC>",
      "position" : 13
    },
    {
      "token" : "权",
      "start_offset" : 70,
      "end_offset" : 71,
      "type" : "<IDEOGRAPHIC>",
      "position" : 14
    },
    {
      "token" : "声",
      "start_offset" : 71,
      "end_offset" : 72,
      "type" : "<IDEOGRAPHIC>",
      "position" : 15
    },
    {
      "token" : "明",
      "start_offset" : 72,
      "end_offset" : 73,
      "type" : "<IDEOGRAPHIC>",
      "position" : 16
    },
    {
      "token" : "本",
      "start_offset" : 74,
      "end_offset" : 75,
      "type" : "<IDEOGRAPHIC>",
      "position" : 17
    },
    {
      "token" : "文",
      "start_offset" : 75,
      "end_offset" : 76,
      "type" : "<IDEOGRAPHIC>",
      "position" : 18
    },
    {
      "token" : "为",
      "start_offset" : 76,
      "end_offset" : 77,
      "type" : "<IDEOGRAPHIC>",
      "position" : 19
    },
    {
      "token" : "博",
      "start_offset" : 77,
      "end_offset" : 78,
      "type" : "<IDEOGRAPHIC>",
      "position" : 20
    },
    {
      "token" : "主",
      "start_offset" : 78,
      "end_offset" : 79,
      "type" : "<IDEOGRAPHIC>",
      "position" : 21
    },
    {
      "token" : "原",
      "start_offset" : 79,
      "end_offset" : 80,
      "type" : "<IDEOGRAPHIC>",
      "position" : 22
    },
    {
      "token" : "创",
      "start_offset" : 80,
      "end_offset" : 81,
      "type" : "<IDEOGRAPHIC>",
      "position" : 23
    },
    {
      "token" : "文",
      "start_offset" : 81,
      "end_offset" : 82,
      "type" : "<IDEOGRAPHIC>",
      "position" : 24
    },
    {
      "token" : "章",
      "start_offset" : 82,
      "end_offset" : 83,
      "type" : "<IDEOGRAPHIC>",
      "position" : 25
    },
    {
      "token" : "转",
      "start_offset" : 84,
      "end_offset" : 85,
      "type" : "<IDEOGRAPHIC>",
      "position" : 26
    },
    {
      "token" : "载",
      "start_offset" : 85,
      "end_offset" : 86,
      "type" : "<IDEOGRAPHIC>",
      "position" : 27
    },
    {
      "token" : "请",
      "start_offset" : 86,
      "end_offset" : 87,
      "type" : "<IDEOGRAPHIC>",
      "position" : 28
    },
    {
      "token" : "附",
      "start_offset" : 87,
      "end_offset" : 88,
      "type" : "<IDEOGRAPHIC>",
      "position" : 29
    },
    {
      "token" : "上",
      "start_offset" : 88,
      "end_offset" : 89,
      "type" : "<IDEOGRAPHIC>",
      "position" : 30
    },
    {
      "token" : "博",
      "start_offset" : 89,
      "end_offset" : 90,
      "type" : "<IDEOGRAPHIC>",
      "position" : 31
    },
    {
      "token" : "文",
      "start_offset" : 90,
      "end_offset" : 91,
      "type" : "<IDEOGRAPHIC>",
      "position" : 32
    },
    {
      "token" : "链",
      "start_offset" : 91,
      "end_offset" : 92,
      "type" : "<IDEOGRAPHIC>",
      "position" : 33
    },
    {
      "token" : "接",
      "start_offset" : 92,
      "end_offset" : 93,
      "type" : "<IDEOGRAPHIC>",
      "position" : 34
    }
  ]
}

```

#### path hierarchy tokenizer
路径层次分词器（path hierarchy tokenizer）允许以特定的方式索引文件系统的路径，这样在搜索时，共享同样路径的文件将被作为结果返回
```
POST _analyze
{
  "tokenizer": "path_hierarchy",
  "text":"/usr/local/python/python2.7"
}
{
  "tokens" : [
    {
      "token" : "/usr",
      "start_offset" : 0,
      "end_offset" : 4,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "/usr/local",
      "start_offset" : 0,
      "end_offset" : 10,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "/usr/local/python",
      "start_offset" : 0,
      "end_offset" : 17,
      "type" : "word",
      "position" : 0
    },
    {
      "token" : "/usr/local/python/python2.7",
      "start_offset" : 0,
      "end_offset" : 27,
      "type" : "word",
      "position" : 0
    }
  ]
}

```

### 分词过滤器
asticsearch内置很多（真是变态多啊！但一般用不到，美滋滋！！！）的分词过滤器。其中包含分词过滤器和字符过滤器。
常见分词过滤器
这里仅列举几个常见的分词过滤器（token filter）包括：

- 标准分词过滤器（Standard Token Filter）在6.5.0版本弃用。此筛选器已被弃用，将在下一个主要版本中删除。在之前的版本中其实也没干啥，甚至在更老版本的Lucene中，它用于去除单词结尾的s字符，还有不必要的句点字符，但是现在， 连这些小功能都被其他的分词器和分词过滤器顺手干了，真可怜！
- ASCII折叠分词过滤器（ASCII Folding Token Filter）将前127个ASCII字符(基本拉丁语的Unicode块)中不包含的字母、数字和符号Unicode字符转换为对应的ASCII字符(如果存在的话）。
- 扁平图形分词过滤器（Flatten Graph Token Filter）接受任意图形标记流。例如由同义词图形标记过滤器生成的标记流，并将其展平为适合索引的单个线性标记链。这是一个有损的过程，因为单独的侧路径被压扁在彼此之上，但是如果在索引期间使用图形令牌流是必要的，因为Lucene索引当前不能表示图形。 出于这个原因，最好只在搜索时应用图形分析器，因为这样可以保留完整的图形结构，并为邻近查询提供正确的匹配。该功能在Lucene中为实验性功能。
- 长度标记过滤器（Length Token Filter）会移除分词流中太长或者太短的标记，它是可配置的，我们可以在settings中设置。
- 小写分词过滤器（Lowercase Token Filter）将分词规范化为小写，它通过language参数支持希腊语、爱尔兰语和土耳其语小写标记过滤器。
- 大写分词过滤器（Uppercase Token Filter）将分词规范为大写。

#### 自定义分词过滤器
```
PUT pattern_test4
{
  "settings": {
    "analysis": {
      "filter": {
        "my_test_length":{
          "type":"length",
          "max":8,
          "min":2
        }
      }
    }
  }
}

```
上例中，我们自定义了一个长度过滤器，过滤掉长度大于8和小于2的分词。
需要补充的是，max参数表示最大分词长度。默认为Integer.MAX_VALUE，就是2147483647（231−1），而min则表示最小长度，默认为0
```
POST pattern_test4/_analyze
{
  "tokenizer": "standard",
  "filter": ["my_test_length"],
  "text":"a Small word and a longerword"
}
{
  "tokens" : [
    {
      "token" : "Small",
      "start_offset" : 2,
      "end_offset" : 7,
      "type" : "<ALPHANUM>",
      "position" : 1
    },
    {
      "token" : "word",
      "start_offset" : 8,
      "end_offset" : 12,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "and",
      "start_offset" : 13,
      "end_offset" : 16,
      "type" : "<ALPHANUM>",
      "position" : 3
    }
  ]
}

```
#### 自定义小写分词过滤器
自定义一个小写分词过滤器，过滤希腊文
```
PUT lowercase_example
{
  "settings": {
    "analysis": {
      "analyzer": {
        "standard_lowercase_example": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase"]
        },
        "greek_lowercase_example": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["greek_lowercase"]
        }
      },
      "filter": {
        "greek_lowercase": {
          "type": "lowercase",
          "language": "greek"
        }
      }
    }
  }
}

POST lowercase_example/_analyze
{
  "tokenizer": "standard",
  "filter": ["greek_lowercase"],
  "text":"Ένα φίλτρο διακριτικού τύπου πεζά s ομαλοποιεί το κείμενο διακριτικού σε χαμηλότερη θήκη"
}
{
  "tokens" : [
    {
      "token" : "ενα",
      "start_offset" : 0,
      "end_offset" : 3,
      "type" : "<ALPHANUM>",
      "position" : 0
    },
    {
      "token" : "φιλτρο",
      "start_offset" : 4,
      "end_offset" : 10,
      "type" : "<ALPHANUM>",
      "position" : 1
    },
    {
      "token" : "διακριτικου",
      "start_offset" : 11,
      "end_offset" : 22,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "τυπου",
      "start_offset" : 23,
      "end_offset" : 28,
      "type" : "<ALPHANUM>",
      "position" : 3
    },
    {
      "token" : "πεζα",
      "start_offset" : 29,
      "end_offset" : 33,
      "type" : "<ALPHANUM>",
      "position" : 4
    },
    {
      "token" : "s",
      "start_offset" : 34,
      "end_offset" : 35,
      "type" : "<ALPHANUM>",
      "position" : 5
    },
    {
      "token" : "ομαλοποιει",
      "start_offset" : 36,
      "end_offset" : 46,
      "type" : "<ALPHANUM>",
      "position" : 6
    },
    {
      "token" : "το",
      "start_offset" : 47,
      "end_offset" : 49,
      "type" : "<ALPHANUM>",
      "position" : 7
    },
    {
      "token" : "κειμενο",
      "start_offset" : 50,
      "end_offset" : 57,
      "type" : "<ALPHANUM>",
      "position" : 8
    },
    {
      "token" : "διακριτικου",
      "start_offset" : 58,
      "end_offset" : 69,
      "type" : "<ALPHANUM>",
      "position" : 9
    },
    {
      "token" : "σε",
      "start_offset" : 70,
      "end_offset" : 72,
      "type" : "<ALPHANUM>",
      "position" : 10
    },
    {
      "token" : "χαμηλοτερη",
      "start_offset" : 73,
      "end_offset" : 83,
      "type" : "<ALPHANUM>",
      "position" : 11
    },
    {
      "token" : "θηκη",
      "start_offset" : 84,
      "end_offset" : 88,
      "type" : "<ALPHANUM>",
      "position" : 12
    }
  ]
}

```

#### 多个分词过滤器
我们可以使用多个分词过滤器。例如我们在使用长度过滤器时，可以同时使用小写分词过滤器或者更多

```
POST _analyze
{
  "tokenizer": "standard",
  "filter": ["length","lowercase"],
  "text":"a Small word and a longerword"
}
{
  "tokens" : [
    {
      "token" : "a",
      "start_offset" : 0,
      "end_offset" : 1,
      "type" : "<ALPHANUM>",
      "position" : 0
    },
    {
      "token" : "small",
      "start_offset" : 2,
      "end_offset" : 7,
      "type" : "<ALPHANUM>",
      "position" : 1
    },
    {
      "token" : "word",
      "start_offset" : 8,
      "end_offset" : 12,
      "type" : "<ALPHANUM>",
      "position" : 2
    },
    {
      "token" : "and",
      "start_offset" : 13,
      "end_offset" : 16,
      "type" : "<ALPHANUM>",
      "position" : 3
    },
    {
      "token" : "a",
      "start_offset" : 17,
      "end_offset" : 18,
      "type" : "<ALPHANUM>",
      "position" : 4
    },
    {
      "token" : "longerword",
      "start_offset" : 19,
      "end_offset" : 29,
      "type" : "<ALPHANUM>",
      "position" : 5
    }
  ]
}

```

### 向集群中加入节点
- 复制一份elasticsearch 目录
- 分别启动bin目录下的elasticsearch文件

此时访问：http://127.0.0.1:9200/_cluster/health?pretty 就能看到节点数量了
```
{
  "cluster_name" : "elasticsearch",
  "status" : "yellow",
  "timed_out" : false,
  "number_of_nodes" : 1,
  "number_of_data_nodes" : 1,
  "active_primary_shards" : 15,
  "active_shards" : 15,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 9,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 62.5
}
```
一般这个默认的集群名称就是上面的cluster_name对应的elasticsearch
### 发现节点

#### 广播

#### 单播
当节点的ip(想象一下我们的ip地址是不是一直在变)不经常变化的时候，或者es只连接特定的节点。单播发现是个很理想的模式。使用单播时，我们告诉es集群其他节点的ip及（可选的）端口及端口范围。我们在elasticsearch.yml配置文件中设置：
```
discovery.zen.ping.unicast.hosts: ["10.0.0.1", "10.0.0.3:9300", "10.0.0.6[9300-9400]"]
```
一般的，我们没必要关闭单播发现，如果你需要广播发现的话，配置文件中的列表保持空白即可。

#### 选取主节点
无论是广播发现还是到单播发现，一旦集群中的节点发生变化，它们就会协商谁将成为主节点，elasticsearch认为所有节点都有资格成为主节点。如果集群中只有一个节点，那么该节点首先会等一段时间，如果还是没有发现其他节点，就会任命自己为主节点。
对于节点数较少的集群，我们可以设置主节点的最小数量，虽然这么设置看上去集群可以拥有多个主节点。实际上这么设置是告诉集群有多少个节点有资格成为主节点。怎么设置呢？修改配置文件中的：`discovery.zen.minimum_master_nodes: 3`
一般的规则是集群节点数除以2（向下取整）再加一。比如3个节点集群要设置为2。这么着是为了防止脑裂（split brain）问题

## Python ElasticSearch 

### 安装

```shell
pip install elasticsearch
```

### 连接
```
from elasticsearch import Elasticsearch

# es = Elasticsearch()    # 默认连接本地elasticsearch
# es = Elasticsearch(['127.0.0.1:9200'])  # 连接本地9200端口
es = Elasticsearch(
    ["192.168.1.10", "192.168.1.11", "192.168.1.12"],  # 连接集群，以列表的形式存放各节点的IP地址
    sniff_on_start=True,  # 连接前测试
    sniff_on_connection_fail=True,  # 节点无响应时刷新节点
    sniff_timeout=60  # 设置超时时间
)
```

### 简单使用
```python
from elasticsearch import Elasticsearch

es = Elasticsearch()  # 默认连接本地elasticsearch
print(es.index(index='a2', doc_type='doc', id=1, body={'name': "andy", "age": 18}))
print(es.get(index='a2', doc_type='doc', id=1))
#output
{'_index': 'a2', '_type': 'doc', '_id': '1', '_version': 1, 'result': 'created', '_shards': {'total': 2, 'successful': 1, 'failed': 0}, '_seq_no': 0, '_primary_term': 1}
{'_index': 'a2', '_type': 'doc', '_id': '1', '_version': 1, '_seq_no': 0, '_primary_term': 1, 'found': True, '_source': {'name': 'andy', 'age': 18}}

# 只获取数据（source)部分
print(es.get_source(index='a2', doc_type='doc', id=1))
#output
{'name': 'andy', 'age': 18}
```
### get
使用get时，`index,doc_type,id`都得指定，否则 出错, 在版本7中，doc_type字段弃用了
```python
print(es.get(index='a2', doc_type='doc', id=1))
```
### indices
关于索引的操作，如open,close, get_mapping, get_setting等。

es.indices.delete_alias，删除特定别名。
es.indices.exists，返回一个布尔值，指示给定的索引是否存在。
es.indices.exists_type，检查索引/索引中是否存在类型/类型。
es.indices.flus，明确的刷新一个或多个索引。
es.indices.get_field_mapping，检索特定字段的映射。
es.indices.get_template，按名称检索索引模板。
es.indices.open，打开一个封闭的索引以使其可用于搜索。
es.indices.close，关闭索引以从群集中删除它的开销。封闭索引被阻止进行读/写操作。
es.indices.clear_cache，清除与一个或多个索引关联的所有缓存或特定缓存。
es.indices.put_alias，为特定索引/索引创建别名。
es.indices.get_uprade，监控一个或多个索引的升级程度。
es.indices.put_mapping，注册特定类型的特定映射定义。
es.indices.put_settings，实时更改特定索引级别设置。
es.indices.put_template，创建一个索引模板，该模板将自动应用于创建的新索引。
es.indices.rollove，当现有索引被认为太大或太旧时，翻转索引API将别名转移到新索引。API接受单个别名和条件列表。别名必须仅指向单个索引。如果索引满足指定条件，则创建新索引并切换别名以指向新别名。
es.indices.segments，提供构建Lucene索引（分片级别）的低级别段信息。


```
#当索引不存在时，会先创建索引，但要指定doc_type,否则 报错
es.index(index='a2', doc_type='doc', id=1, body={'name': "andy", "age": 18})
#id可以不指定，es会自动处理
print(es.index(index='a2', doc_type='doc',  body={'name': "Amy", "age": 16}))
print(es.search(index='a2', doc_type='doc', filter_path=['hits.hits._source']))
#output
{'hits': {'hits': [{'_source': {'name': 'andy', 'age': 18}}, {'_source': {'name': 'Amy', 'age': 16}}]}}
```

### cluster
关于集群的操作
es.cluster.get_settings，获取集群设置
```
print(es.cluster.get_settings())
```
es.cluster.health，获取有关群集运行状况的非常简单的状态
```
print(es.cluster.get_settings())
```
es.cluster.state，获取整个集群的综合状态信息。
```
print(es.cluster.state())
```
es.cluster.stats，返回群集的当前节点的信息。
```
print(es.cluster.stats())
```
### Nodes
关于节点的相关操作
es.nodes.info，返回集群中节点的信息。
```
print(es.nodes.info())  # 返回所节点
print(es.nodes.info(node_id='node1'))   # 指定一个节点
print(es.nodes.info(node_id=['node1', 'node2']))   # 指定多个节点列表
```
es.nodes.stats，获取集群中节点统计信息。
```
print(es.nodes.stats())
print(es.nodes.stats(node_id='node1'))
print(es.nodes.stats(node_id=['node1', 'node2']))
```
es.nodes.hot_threads，获取指定节点的线程信息。
```
print(es.nodes.hot_threads(node_id='node1'))
print(es.nodes.hot_threads(node_id=['node1', 'node2']))
```
es.nodes.usage，获取集群中节点的功能使用信息。
```
print(es.nodes.usage())
print(es.nodes.usage(node_id='node1'))
print(es.nodes.usage(node_id=['node1', 'node2']))
```
### cat
一种查询方式，一般的返回都是json类型的，cat提供了简洁的返回结果
es.cat.aliases，返回别名信息。
```
#name要返回的以逗号分隔的别名列表。
#formatAccept标头的简短版本，例如json，yaml
print(es.cat.aliases(name='py23_alias'))
print(es.cat.aliases(name='py23_alias', format='json'))
```
es.cat.allocation，返回分片使用情况。
```
print(es.cat.allocation())
print(es.cat.allocation(node_id=['node1']))
print(es.cat.allocation(node_id=['node1', 'node2'], format='json'))
```
es.cat.count，Count提供对整个群集或单个索引的文档计数的快速访问。
```
print(es.cat.count())  # 集群内的文档总数
print(es.cat.count(index='py3'))  # 指定索引文档总数
print(es.cat.count(index=['py3', 'py2'], format='json'))  # 返回两个索引文档和
```
es.cat.fielddata，基于每个节点显示有关当前加载的fielddata的信息。有些数据为了查询效率，会放在内存中，fielddata用来控制哪些数据应该被放在内存中，而这个es.cat.fielddata则查询现在哪些数据在内存中，数据大小等信息。
```
print(es.cat.fielddata())
print(es.cat.fielddata(format='json', bytes='b'))
```
es.cat.health，从集群中health里面过滤出简洁的集群健康信息。
```
print(es.cat.health())
print(es.cat.health(format='json'))
```
es.cat.indices，返回索引的信息；也可以使用此命令进行查询集群中有多少索引。
```
print(es.cat.indices())
print(es.cat.indices(index='py3'))
print(es.cat.indices(index='py3', format='json'))
print(len(es.cat.indices(format='json')))  # 查询集群中有多少索引
```
es.cat.master，返回集群中主节点的IP，绑定IP和节点名称
es.cat.nodeattrs，返回节点的自定义属性。
es.cat.nodes，返回节点的拓扑，这些信息在查看整个集群时通常很有用，特别是大型集群。我有多少符合条件的节点
es.cat.plugins，返回节点的插件信息。
es.cat.segments，返回每个索引的Lucene有关的信息。
es.cat.shards，返回哪个节点包含哪些分片的信息。
es.cat.thread_pool，获取有关线程池的信息。

### snapshot
Snapshot，快照相关，快照是从正在运行的Elasticsearch集群中获取的备份
- repository 存储库名称。
- snapshot快照名称。
- body快照定义。

es.snapshot.delete，从存储库中删除快照。
es.snapshot.create_repository。注册共享文件系统存储库。
es.snapshot.delete_repository，删除共享文件系统存储库。
es.snapshot.get，检索有关快照的信息。
es.snapshot.get_repository，返回有关已注册存储库的信息。
es.snapshot.restore，恢复快照。
es.snapshot.status，返回有关所有当前运行快照的信息。通过指定存储库名称，可以将结果限制为特定存储库。
es.snapshot.verify_repository，返回成功验证存储库的节点列表，如果验证过程失败，则返回错误消息

### search
对index要搜索的以逗号分隔的索引名称列表; 使用_all 或空字符串对所有索引执行操作。
- doc_type 要搜索的以逗号分隔的文档类型列表; 留空以对所有类型执行操作。
- body 使用Query DSL（QueryDomain Specific Language查询表达式）的搜索定义。
- _source 返回_source字段的true或false，或返回的字段列表，返回指定字段。
- _source_exclude要从返回的_source字段中排除的字段列表，返回的所有字段中，排除哪些字段。
- _source_include从_source字段中提取和返回的字段列表，跟_source差不多。

```python
res = es.search(index='a2',doc_type='doc')

#添加过滤条件，过滤条件写在body中
body = {
    "query":{
        "match":{
            "name":"andy"
        }
    }
}
res = es.search(index='a2',doc_type='doc',body=body)

#对拿到的数据结果进行过滤
res = es.search(index='a2',doc_type='doc',body=body,filter_path=['hits.total','hits.hits._source'])
#output
{'hits': {'total': 1, 'hits': [{'_source': {'name': 'andy', 'age': 18}}]}}

#filter_path参数还支持*通配符以匹配字段名称、任何字段或者字段部分
res = es.search(index='a2',doc_type='doc',body=body,filter_path=['hits.hits._*'])
#output
{'hits': {'hits': [{'_index': 'a2', '_type': 'doc', '_id': '1', '_score': 0.2876821, '_source': {'name': 'andy', 'age': 18}}]}}

#_source参数
body = {
    "query": {
        "match": {
            "name": "andy"
        },
    }
}
print(es.search(index='a2', doc_type='doc',body=body,_source=['age'], filter_path=['hits.hits._source']))

# get_source,如果找不到，出错
print(es.get_source(index='a2', doc_type='doc',id=1))
#output
{'name': 'andy', 'age': 18}
```

### count
```python
print(es.count(index='a2'))
#output
{'count': 2, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}}
```
### create
创建索引（索引不存在的话）并新增一条数据，索引存在仅新增（只能新增，重复执行会报错）
```python
print(es.create(index='a2', doc_type='doc', id='2', body={"name": '王五', "age": 20}))
#output
{'_index': 'a2', '_type': 'doc', '_id': '2', '_version': 1, 'result': 'created', '_shards': {'total': 2, 'successful': 1, 'failed': 0}, '_seq_no': 0, '_primary_term': 1}
```
### delete
删除指定的文档。比如删除文章id为4的文档，但不能删除索引，如果想要删除索引，还需要es.indices.delete来处理.删除不存在的数据会出错。
```python
print(es.delete(index='a2', doc_type='doc', id='2'))
```
es.delete_by_query，删除与查询匹配的所有文档,匹配出来的文档都会被删除
```python
print(es.delete_by_query(index='a2', doc_type='doc', body={"query": {"match":{"age": 20}}}))
```
### exists
exists，查询elasticsearch中是否存在指定的文档，返回一个布尔值。
```python
print(es.exists(index='a2', doc_type='doc', id='1'))
#output
True
```
### info
es.info，获取当前集群的基本信息。
```python
print(es.info())
```
### ping
es.ping，如果群集已启动，则返回True，否则返回False。
```python
print(es.ping())
```

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