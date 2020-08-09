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