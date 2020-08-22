

## suggest
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
