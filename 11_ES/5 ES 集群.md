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