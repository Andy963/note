### 安装
```
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
使用get时，`index,doc_type,id`都得指定，否则 出错
```python
print(es.get(index='a2', doc_type='doc', id=1))
```
### indices
关于索引的操作，如open,close, get_mapping,get_setting等。

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