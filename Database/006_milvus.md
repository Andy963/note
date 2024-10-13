
## collections
### connect

```python
from pymilvus import (  
connections,  
utility,  
FieldSchema, CollectionSchema, DataType, Collection,  
)  
  
# get a connection  
conn = connections.connect(host='localhost', port=19530)
```

### create, has, release collections

```python
paper_milvus = Collection("paper")

has = utility.has_collection("paper")  
print(f"Does collection paper exist in Milvus: {has}")

# release
paper_milvus.release()
```


### rename, drop collections

```python
has_paper = utility.has_collection('paper')  
if has_paper:  
	# rename collections  
	has_paper_milvus = utility.has_collection('paper_milvus')  
	if has_paper_milvus:  
	utility.drop_collection('paper_milvus')  
	  
	utility.rename_collection('paper', 'paper_milvus')  
	# check if collections exist  
	has_paper_milvus = utility.has_collection('paper_milvus')  
	if has_paper_milvus:  
	utility.rename_collection('paper_milvus', 'paper')  
	print(f"has paper_milvus {utility.has_collection('paper_milvus')}")
```

### create, alter, drop alias 

```python
# create alias  
utility.create_alias(  
collection_name="paper",  
alias="default" # collection alias can only contain numbers, letters and underscores  
)  
  
# alter alias  
utility.alter_alias(  
collection_name="paper",  
alias="new_default"  
)  
  
# drop alias  
utility.drop_alias(alias="new_default")  
utility.create_alias(  
collection_name="paper",  
alias="paper_alias"  
)
```

### load collections

```python
collection = Collection("paper")  
collection.load(replica_number=2)  
  
# Check the loading progress and loading status  
utility.load_state("paper")  
# Output: <LoadState: Loaded>  
  
utility.loading_progress("paper")  
# Output: {'loading_progress': 100%}
```

collection with different replica number 1 existed, release this collection first before

## partition

### creat, check, list partition 

```python
collection = Collection("book") # Get an existing collection.
collection.create_partition("novel") # max to 4096 

# hceck if exist
collection.has_partition("novel")

# list
collection.partitions

collection.drop_partition("novel") # need to release first
```

### load, release  partition

```python
collection = Collection("book") # Get an existing collection. 
collection.load(["novel"], replica_number=2) # Or you can load a partition with the partition as an object 
from pymilvus import Partition 
partition = Partition("novel") # Get an existing partition. 
partition.load(replica_number=2)

# get partition info
result = partition.get_replicas() 
print(result)

# release
partition.release()
```


## Data

### insert,

```python
import random  
  
from pymilvus import (  
connections,  
FieldSchema, DataType, Collection, CollectionSchema,  
)  
from pymilvus.orm import utility

conn = connections.connect(host='localhost', port=19530)  
  
data = [  
[i for i in range(2000)],  
[str(i) for i in range(2000)],  
[[random.random() for _ in range(2)] for _ in range(2000)],  
]  
if utility.has_collection('book'):  
utility.drop_collection('book')  
  
# collection = Collection("book") # Get an existing collection.  
# collection.create_partition("novel")  
fields = [  
FieldSchema("id", DataType.INT64, is_primary=True),  
FieldSchema("title", DataType.VARCHAR, max_length=10),  
FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=2)  
]  
schema = CollectionSchema(fields=fields)  
collection = Collection("book", schema=schema, using='default')  
mr = collection.insert(data)
mr.flush()

conn = connections.connect(host='localhost', port=19530)
```

有几点需要注意：
- 必须有主键(is_primary), 
- VARCHAR 必须指定max_length, 
- VECTOR dim必须与数据的一致，max :32,768
- insert 调用完后最好调用下flush collections.flush()

### insert entitties

```python
from pymilvus import utility
task_id = utility.do_bulk_insert(
    collection_name="book",
    partition_name="2022",
    files=["test.json"]
)

```

### delete entitties

```python
expr = "id in [0,1]"
from pymilvus import Collection
collection = Collection("book")      # Get an existing collection.
collection.delete(expr)

# expr中如果有不存在的字段名就会：failed to create expr plan, expr = book_id in [0,1]

```

### compact

```python
collection = Collection("book") # Get an existing collection.  
# collection.compact()  
print(collection.get_compaction_state())
```

### index

### build index

```python
index_params = {
  "metric_type":"L2",
  "index_type":"IVF_FLAT",
  "params":{"nlist":1024}
}


from pymilvus import Collection, utility
collection = Collection("book")      
collection.create_index(
  field_name="book_intro", 
  index_params=index_params
)

utility.index_building_progress("book")

```

build index on scalars:

```python
from pymilvus import Collection

collection = Collection("book")   
collection.create_index(
  field_name="book_name", 
  index_name="scalar_index",
)
collection.load()

```

after build index, how to get how many index you have ?

```python
index_infos = collection.indexes  
for index in index_infos:  
	print(index.index_name)
# see the collections source code: line 852, it's a property
```

### search
对于scalar 可以指定一个expr用来过滤

```python
search_param = {
  "data": [[0.1, 0.2]],
  "anns_field": "book_intro",
  "param": {"metric_type": "L2", "params": {"nprobe": 10}},
  "limit": 2,
  "expr": "book_name like \"Hello%\"", 
}
res = collection.search(**search_param)
print(results[0].ids)  
  
print(results[0].distances)  
  
hit = results[0][0]  
print(hit.entity.get('title'))
```

### drop index

```python
from pymilvus import Collection
collection = Collection("book")      # Get an existing collection.
collection.drop_index()

```

## search

```python

from pymilvus import Collection
collection = Collection("book")      # Get an existing collection.
collection.load()

search_params = {"metric_type": "L2", "params": {"nprobe": 10}, "offset": 5}

results = collection.search(
	data=[[0.1, 0.2]], 
	anns_field="book_intro", 
	param=search_params,
	limit=10, 
	expr=None,
	output_fields=['title'] # set the names of the fields you want to retrieve from the search result.
	consistency_level="Strong"
)

results[0].ids

results[0].distances

hit = results[0][0]
hit.entity.get('title')

```