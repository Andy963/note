### py select in 
```pyhton
maintainer_list = ['name1','name2']
sql = "select user_id from users where name in (%s)" % (",".join(['%s']*len(maintainer_list)))
db.fetchall(sql, maintainer_list)
```