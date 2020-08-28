

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
### completion suggester
### context suggester