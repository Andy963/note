## SQLAlchemy

### 连接数据库

Sqlite

```python
# sqlite://<nohostname>/<path>
# where <path> is relative:
engine = create_engine("sqlite:///foo.db")
# for sqlite memory database, just keep it empty.
engine = create_engine("sqlite://")
# absolute path
# Unix/Mac - 4 initial slashes in total
engine = create_engine("sqlite:////absolute/path/to/foo.db")

# Windows
engine = create_engine("sqlite:///C:\\path\\to\\foo.db")

# Windows alternative using raw string
engine = create_engine(r"sqlite:///C:\path\to\foo.db")
```

 PostgreSQL

```python
# default
engine = create_engine("postgresql://scott:tiger@localhost/mydatabase")

# psycopg2
engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/mydatabase")

# pg8000
engine = create_engine("postgresql+pg8000://scott:tiger@localhost/mydatabase")
```

MySQL

```python
# default
engine = create_engine("mysql://scott:tiger@localhost/foo")

# mysqlclient (a maintained fork of MySQL-Python)
engine = create_engine("mysql+mysqldb://scott:tiger@localhost/foo")

# PyMySQL
engine = create_engine("mysql+pymysql://scott:tiger@localhost/foo")
```


### 执行SQL

execute with connect:

```python
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
    )
    conn.commit()

# with paramters 
with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table WHERE y > :y"), {"y": 2})
    for row in result:
        print(f"x: {row.x}  y: {row.y}")
```

execute with Session:

```python
from sqlalchemy import text
from sqlalchemy.orm import Session

stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
with Session(engine) as session:
    result = session.execute(stmt, {"y": 6})
    for row in result:
        print(f"x: {row.x}  y: {row.y}")

# commit update
with Session(engine) as session:
    result = session.execute(
        text("UPDATE some_table SET y=:y WHERE x=:x"),
        [{"x": 9, "y": 11}, {"x": 13, "y": 15}],
    )
    session.commit()
```



`pip install flask-sqlalchemy`

### 使用SQLAlchemy去连接数据库：
这里连接数据库与flask没有任何关系

使用SQLALchemy去连接数据库，需要使用一些配置信息，然后将他们组合成满足条件的字符串：

```python
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)
```

然后使用`create_engine`创建一个引擎`engine`，然后再调用这个引擎的`connect`方法，就可以得到这个对象，然后就可以通过这个对象对数据库进行操作了：

```python
engine = create_engine(DB_URI)
#创建engine时可以指定echo=True查看语句：create_engine(DB_URI,echo=True)
# 判断是否连接成功
conn = engine.connect()
result = conn.execute('select 1')
print(result.fetchone())

#输出：
(1,)
```

```python

conn = pymysql.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)
cur = conn.cursor()
lock.acquire()
cur.execute('select 1;')
lock.release()
print(cur.fetchone())
cur.close()
conn.close()
```

在win 下如果对应的app.py 没有叫“app.py" 直接执行 `flask shell` 是没有效果的，此时需要指定 ”app.py" 可通过：`set FLASK_APP=main.py`  Linux下是 `export`

### ORM：
1. ORM：Object Relationship Mapping
2. 大白话：对象模型与数据库表的映射

#### 将ORM模型映射到数据库中：
1. 用`declarative_base`根据`engine`创建一个ORM基类。

    ```python
    from sqlalchemy.ext.declarative import declarative_base
    engine = create_engine(DB_URI)
    Base = declarative_base(engine)
    ```

2. 用这个`Base`类作为基类来写自己的ORM类。要定义`__tablename__`类属性，来指定这个模型映射到数据库中的表名。

    ```python
    class Person(Base):
        __tablename__ = 'person'
    ```

3. 创建属性来映射到表中的字段，所有需要映射到表中的属性都应该为Column类型：

    ```python
    #2. 在这个ORM模型中创建一些属性，来跟表中的字段进行一一映射。这些属性必须是sqlalchemy给我们提供好的数据类型。
    from sqlalchemy import Integer, String
    class Person(Base):
        __tablename__ = 'person'
        id = Column(Integer,primary_key=True,autoincrement=True)
        name = Column(String(50))
        age = Column(Integer)
    ```
	
4. 使用`Base.metadata.create_all()`来将模型映射到数据库中。
5. 一旦使用`Base.metadata.create_all()`将模型映射到数据库中后，即使改变了模型的字段，也不会重新映射了。

#### 用session做数据的增删改查操作：
1. 构建session对象：所有和数据库的ORM操作都必须通过一个叫做`session`的会话对象来实现，通过以下代码来获取会话对象：

    ```python
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(DB_URI)
    session = sessionmaker(engine)()
    ```
2. 添加对象：
    * 创建对象，也即创建一条数据：
        ```python
        p = Person(name='zhiliao',age=18,country='china')
        ```
    * 将这个对象添加到`session`会话对象中：
        ```python
        session.add(p)
        ```
    * 将session中的对象做commit操作（提交）：
        ```python
        session.commit()
        ```
    * 一次性添加多条数据：
        ```python
        p1 = Person(name='zhiliao1',age=19,country='china')
        p2 = Person(name='zhiliao2',age=20,country='china')
        session.add_all([p1,p2])
        session.commit()
        ```
3. 查找对象：
    ```python
    # 查找某个模型对应的那个表中所有的数据：
    all_person = session.query(Person).all()
    # 使用filter_by来做条件查询
    all_person = session.query(Person).filter_by(name='zhiliao').all()
    # 使用filter来做条件查询
    all_person = session.query(Person).filter(Person.name=='zhiliao').all()
    # 使用get方法查找数据，get方法是根据id来查找的，只会返回一条数据或者None
    person = session.query(Person).get(primary_key)
    # 使用first方法获取结果集中的第一条数据
    person = session.query(Person).first()
    ```
4. 修改对象：首先从数据库中查找对象，然后将这条数据修改为你想要的数据，最后做commit操作就可以修改数据了。
    ```python
    person = session.query(Person).first()
    person.name = 'ketang'
    session.commit()
    ```
5. 删除对象：将需要删除的数据从数据库中查找出来，然后使用`session.delete`方法将这条数据从session中删除，最后做commit操作就可以了。
    ```python
    person = session.query(Person).first()
    session.delete(person)
    session.commit()
    ```
	
#### SQLAlchemy常用数据类型：
1. Integer：整形，映射到数据库中是int类型。
2. Float：浮点类型，映射到数据库中是float类型。他占据的32位。
3. Double：双精度浮点类型，映射到数据库中是double类型，占据64位。
4. String：可变字符类型，映射到数据库中是varchar类型.
5. Boolean：布尔类型，映射到数据库中的是tinyint类型。
6. DECIMAL：定点类型。是专门为了解决浮点类型精度丢失的问题的。在存储钱相关的字段的时候建议大家都使用这个数据类型。并且这个类型使用的时候需要传递两个参数，第一个参数是用来标记这个字段总能能存储多少个数字，第二个参数表示小数点后有多少位。
7. Enum：枚举类型。指定某个字段只能是枚举中指定的几个值，不能为其他值。在ORM模型中，使用Enum来作为枚举，示例代码如下：

    ```python
    class Article(Base):
        __tablename__ = 'article'
        id = Column(Integer,primary_key=True,autoincrement=True)
        tag = Column(Enum("python",'flask','django'))
    ```
    
    在Python3中，已经内置了enum这个枚举的模块，我们也可以使用这个模块去定义相关的字段。示例代码如下：
    
    ```python
    import enum
    class TagEnum(enum.Enum):
        python = "python"
        flask = "flask"
        django = "django"

    class Article(Base):
        __tablename__ = 'article'
        id = Column(Integer,primary_key=True,autoincrement=True)
        tag = Column(Enum(TagEnum))

    article = Article(tag=TagEnum.flask)
    ```
8. Date：存储时间，只能存储年月日。映射到数据库中是date类型。在Python代码中，可以使用`datetime.date`来指定。示例代码如下：
    ```python
    class Article(Base):
        __tablename__ = 'article'
        id = Column(Integer,primary_key=True,autoincrement=True)
        create_time = Column(Date)

    article = Article(create_time=date(2017,10,10))
    ```
9. DateTime：存储时间，可以存储年月日时分秒毫秒等。映射到数据库中也是datetime类型。在Python代码中，可以使用`datetime.datetime`来指定。示例代码如下：
    ```python
    class Article(Base):
        __tablename__ = 'article'
        id = Column(Integer,primary_key=True,autoincrement=True)
        create_time = Column(DateTime)

    article = Article(create_time=datetime(2011,11,11,11,11,11))
    ```
10. Time：存储时间，可以存储时分秒。映射到数据库中也是time类型。在Python代码中，可以使用`datetime.time`来至此那个。示例代码如下：
    ```python
    class Article(Base):
        __tablename__ = 'article'
        id = Column(Integer,primary_key=True,autoincrement=True)
        create_time = Column(Time)

    article = Article(create_time=time(hour=11,minute=11,second=11))
    ```
11. Text：存储长字符串。一般可以存储6W多个字符。如果超出了这个范围，可以使用LONGTEXT类型。映射到数据库中就是text类型。
12. LONGTEXT：长文本类型，映射到数据库中是longtext类型。



#### Column常用参数：
1. primary_key：设置某个字段为主键。
2. autoincrement：设置这个字段为自动增长的。
3. default：设置某个字段的默认值。在发表时间这些字段上面经常用。
4. nullable：指定某个字段是否为空。默认值是True，就是可以为空。
5. unique：指定某个字段的值是否唯一。默认是False。
6. onupdate：在数据更新的时候会调用这个参数指定的值或者函数。在第一次插入这条数据的时候，不会用onupdate的值，只会使用default的值。常用的就是`update_time`（每次更新数据的时候都要更新的值）。
7. name：指定ORM模型中某个属性映射到表中的字段名。如果不指定，那么会使用这个属性的名字来作为字段名。如果指定了，就会使用指定的这个值作为参数。这个参数也可以当作位置参数，在第1个参数来指定。

    ```python
    title = Column(String(50),name='title',nullable=False)
    title = Column('my_title',String(50),nullable=False)
    ```

8. Index 创建索引

单独某个列创建索引直接在column中指定 `index=True` 即可，下面是创建联合索引

```python

from sqlalchemy import Column, Integer, String, Index

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120))
    
# 创建一个联合索引
Index('idx_name_email', User.name, User.email)

```

## Query
### query可用参数：
1. 模型对象。指定查找这个模型中所有的对象。
2. 模型中的属性。可以指定只查找某个模型的其中几个属性。

```python
from sqlalchemy import func

articles = session.query(Article.title,Article.price).all()
res = session.query(func.max(Article.price)).first()
print(res)
```

3. 聚合函数。
    * func.count：统计行的数量。
    * func.avg：求平均值。
    * func.max：求最大值。
    * func.min：求最小值。
    * func.sum：求和。
    `func`上，其实没有任何聚合函数。但是因为他底层做了一些魔术，只要mysql中有的聚合函数，都可以通过func调用。


### filter过滤条件：
过滤是数据提取的一个很重要的功能，以下对一些常用的过滤条件进行解释，并且这些过滤条件都是只能通过filter方法实现的：

*注意*filter_by,filter之后还要接上first,all等限定，否则返回的数据会有问题

```python

res = session.query(Article).filter(Article.id==5).all() 支持>,<
res = session.query(Article).filter_by(id=5).all() 不支持>,<
print(res)

```

1. equals：

    ```python
    article = session.query(Article).filter(Article.title == "title0").first()
    print(article)
    ```
2. not equals:
    ```python
    query.filter(User.name != 'ed')
    ```
2. like：
    ```python
    query.filter(User.name.like('%ed%'))
    ```

3. in：
    ```python
    query.filter(User.name.in_(['ed','wendy','jack']))
    # 同时，in也可以作用于一个Query
    query.filter(User.name.in_(session.query(User.name).filter(User.name.like('%ed%'))))
    ```

4. not in：前面加波浪线取反
    ```python
    query.filter(~User.name.in_(['ed','wendy','jack']))
    ```
5.  is null：
    ```python
    query.filter(User.name==None)
    # 或者是
    query.filter(User.name.is_(None))
    ```

6. is not null:
    ```python
    query.filter(User.name != None)
    # 或者是
    query.filter(User.name.isnot(None))
    # 上面是v1.1之后的isnot
    # https://docs.sqlalchemy.org/en/13/core/metadata.html?highlight=isnot
    # 在v2.0中为is_not 具体哪个版本开始改的不清楚
    ```

7. and：
    ```python
    from sqlalchemy import and_
    query.filter(and_(User.name=='ed',User.fullname=='Ed Jones'))
    # 或者是传递多个参数
    query.filter(User.name=='ed',User.fullname=='Ed Jones')
    # 或者是通过多次filter操作
    query.filter(User.name=='ed').filter(User.fullname=='Ed Jones')
    ```

8. or：
    ```python
    from sqlalchemy import or_  
    query.filter(or_(User.name=='ed',User.name=='wendy'))
    ```

如果想要查看orm底层转换的sql语句，可以在filter方法后面不要再执行任何方法直接打印就可以看到了。比如：
```python
        # 查找title或者content为abc的文章，or_
        articles = session.query(Article).filter(or_(Article.title=='abc',Article.content=='abc'))
        print(articles)
```


### 排序：
1. order_by：可以指定根据这个表中的某个字段进行排序，如果在前面加了一个-，代表的是降序排序。
2. 在模型定义的时候指定默认排序：有些时候，不想每次在查询的时候都指定排序的方式，可以在定义模型的时候就指定排序的方式。有以下两种方式：
    * relationship的order_by参数：在指定relationship的时候，传递order_by参数到（backref中，因为如果不指定多的一方指定order_by没有意义）来指定排序的字段。
    * 在模型定义中，添加以下代码：类似于django中的class meta

     __mapper_args__ = {
         "order_by": title
       }
    即可让文章使用标题来进行排序。
3. 正序排序与倒序排序：默认是使用正序排序。如果需要使用倒序排序，那么可以使用这个字段的`desc()`方法，或者是在排序的时候使用这个字段的字符串名字，然后在前面加一个负号。

### limit、offset和切片操作：
1. limit：可以限制每次查询的时候只查询几条数据。
2. offset：可以限制查找数据的时候过滤掉前面多少条。
3. 切片：可以对Query对象使用切片操作，来获取想要的数据。可以使用`slice(start,stop)`方法来做切片操作。也可以使用`[start:stop]`的方式来进行切片操作。一般在实际开发中，中括号的形式是用得比较多的。希望大家一定要掌握。示例代码如下：
```python
articles = session.query(Article).order_by(Article.id.desc())[0:10]
```


### 懒加载：
在一对多，或者多对多的时候，如果想要获取多的这一部分的数据的时候，往往能通过一个属性就可以全部获取了。比如有一个作者，想要或者这个作者的所有文章，那么可以通过user.articles就可以获取所有的。但有时候我们不想获取所有的数据，比如只想获取这个作者今天发表的文章，那么这时候我们可以给relationship传递一个lazy='dynamic'，以后通过user.articles获取到的就不是一个列表，而是一个AppenderQuery对象了。这样就可以对这个对象再进行一层过滤和排序等操作。
通过`lazy='dynamic'`，获取出来的多的那一部分的数据，就是一个`AppenderQuery`对象了。这种对象既可以添加新数据，也可以跟`Query`一样，可以再进行一层过滤。
总而言之一句话：如果你在获取数据的时候，想要对多的那一边的数据再进行一层过滤，那么这时候就可以考虑使用`lazy='dynamic'`。
lazy可用的选项：
1. `select`：这个是默认选项。还是拿`user.articles`的例子来讲。如果你没有访问`user.articles`这个属性，那么sqlalchemy就不会从数据库中查找文章。一旦你访问了这个属性，那么sqlalchemy就会立马从数据库中查找所有的文章，并把查找出来的数据组装成一个列表返回。这也是懒加载。
2. `dynamic`：这个就是我们刚刚讲的。就是在访问`user.articles`的时候返回回来的不是一个列表，而是`AppenderQuery`对象。

### group_by：
根据某个字段进行分组。比如想要根据性别进行分组，来统计每个分组分别有多少人，那么可以使用以下代码来完成：
```python
session.query(User.gender,func.count(User.id)).group_by(User.gender).all()
```

### having：
having是对查找结果进一步过滤。比如只想要看未成年人的数量，那么可以首先对年龄进行分组统计人数，然后再对分组进行having过滤。示例代码如下：
```python
result = session.query(User.age,func.count(User.id)).group_by(User.age).having(User.age >= 18).all()
```

### join：
1. join分为left join（左外连接）和right join（右外连接）以及内连接（等值连接）。
2. 参考的网页：http://www.jb51.net/article/15386.htm
3. 在sqlalchemy中，使用join来完成内连接。在写join的时候，如果不写join的条件，那么默认将使用外键来作为条件连接。
4. query查找出来什么值，不会取决于join后面的东西，而是取决于query方法中传了什么参数。就跟原生sql中的select 后面那一个一样。
比如现在要实现一个功能，要查找所有用户，按照发表文章的数量来进行排序。示例代码如下：
```python
result = session.query(User,func.count(Article.id)).join(Article).group_by(User.id).order_by(func.count(Article.id).desc()).all()
```

### subquery：
子查询可以让多个查询变成一个查询，只要查找一次数据库，性能相对来讲更加高效一点。不用写多个sql语句就可以实现一些复杂的查询。那么在sqlalchemy中，要实现一个子查询，应该使用以下几个步骤：
1. 将子查询按照传统的方式写好查询代码，然后在`query`对象后面执行`subquery`方法，将这个查询变成一个子查询。
2. 在子查询中，将以后需要用到的字段通过`label`方法，取个别名。
3. 在父查询中，如果想要使用子查询的字段，那么可以通过子查询的返回值上的`c`属性拿到。
整体的示例代码如下：
```python
stmt = session.query(User.city.label("city"),User.age.label("age")).filter(User.username=='李A').subquery()
result = session.query(User).filter(User.city==stmt.c.city,User.age==stmt.c.age).all()
```



### 外键：
使用SQLAlchemy创建外键非常简单。在从表中增加一个字段，指定这个字段外键的是哪个表的哪个字段就可以了。从表中外键的字段，必须和父表的主键字段类型保持一致。(一对多中，一是父表，多是子表) 下面的你表是User, id字段为Integer,所以外键的数据类型也必须是Integer
示例代码如下：
```python
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    content = Column(Text,nullable=False)

    uid = Column(Integer,ForeignKey("user.id", on_delete="RESTRICT"))
```

外键约束有以下几项： 
1. RESTRICT：父表数据被删除，会阻止删除。默认就是这一项。 
2. NO ACTION：在MySQL中，同RESTRICT。 
3. CASCADE：级联删除。 User删除了，他所写的文章也会被删除
4. SET NULL：父表数据被删除，子表数据会设置为NULL。

#### 一对一：

在sqlalchemy中，如果想要将两个模型映射成一对一的关系，那么应该在父模型中，指定引用的时候，要传递一个`uselist=False`这个参数进去。就是告诉父模型，以后引用这个从模型的时候，不再是一个列表了，而是一个对象了，即一对一。示例代码如下：
relation可以在两个存在外键的model中都定义，但这样比较麻烦，推荐使用relationship中的backref

```python
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)

    extend = relationship("UserExtend",uselist=False)

    def __repr__(self):
        return "<User(username:%s)>" % self.username

class UserExtend(Base):
    __tablename__ = 'user_extend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50))
    uid = Column(Integer,ForeignKey("user.id"))

    user = relationship("User",backref="extend")
```

当然，也可以借助`sqlalchemy.orm.backref`来简化代码：
下面的代码中backref()函数与上面User类中注释的代码的作用相同，但如果User类中定义了extend则UserExtend不能写backref因为重复了，uselist=False限制了添加数据，达到一对一的目的

```python
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)

    # extend = relationship("UserExtend",uselist=False)

    def __repr__(self):
        return "<User(username:%s)>" % self.username

class UserExtend(Base):
    __tablename__ = 'user_extend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50))
    uid = Column(Integer,ForeignKey("user.id"))

    user = relationship("User",backref=backref("extend",uselist=False))
```

#### 一对多：
mysql级别的外键，还不够ORM，必须拿到一个表的外键，然后通过这个外键再去另外一张表中查找，这样太麻烦了。SQLAlchemy提供了一个`relationship`，这个类可以定义属性，以后在访问相关联的表的时候就直接可以通过属性访问的方式就可以访问得到了。示例代码：

```python
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(50),nullable=False)

    # articles = relationship("Article")

    def __repr__(self):
        return "<User(username:%s)>" % self.username

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)
    content = Column(Text,nullable=False)
    uid = Column(Integer,ForeignKey("user.id"))

    author = relationship("User",backref="articles")

user = User(username='andy')

article = Article(title='this is article one', uid=1)
article2 = Article(title='this is article t2o' )
user.articles.append(article)
user.articles.append(article2)
#article.user = user 这种方式更常见
#session.add(article)
session.add(user)
session.commit()
```

另外，可以通过`backref`来指定反向访问的属性名称。articles是有多个。他们之间的关系是一个一对多的关系。
总结为：正向查找是relationship, 反向查找为relations中的backref指定。


#### 多对多：
1. 多对多的关系需要通过一张中间表来绑定他们之间的关系。
2. 先把两个需要做多对多的模型定义出来
3. 使用Table定义一个中间表，中间表一般就是包含两个模型的外键字段就可以了，并且让他们两个来作为一个“复合主键”。
4. 在两个需要做多对多的模型中随便选择一个模型，定义一个relationship属性，来绑定三者之间的关系，在使用relationship的时候，需要传入一个secondary=中间表。


```python
#encoding: utf-8
from sqlalchemy import create_engine,Column,Integer,Float,Boolean,DECIMAL,Enum,Date,DateTime,Time,String,Text,func,and_,or_,ForeignKey,Table
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
# 在Python3中才有这个enum模块，在python2中没有
import enum
from datetime import datetime
import random

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

engine = create_engine(DB_URI)

Base = declarative_base(engine)

session = sessionmaker(engine)()

#第三张表
article_tag = Table(
    "article_tag",
    Base.metadata,
    Column("article_id",Integer,ForeignKey("article.id"),primary_key=True),
    Column("tag_id",Integer,ForeignKey("tag.id"),primary_key=True)
)

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(50),nullable=False)

    # tags = relationship("Tag",backref="articles",secondary=article_tag)

    def __repr__(self):
        return "<Article(title:%s)>" % self.title

class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    articles = relationship("Article",backref="tags",secondary=article_tag)

    def __repr__(self):
        return "<Tag(name:%s)>" % self.name

# 1. 先把两个需要做多对多的模型定义出来
# 2. 使用Table定义一个中间表，中间表一般就是包含两个模型的外键字段就可以了，并且让他们两个来作为一个“复合主键（联合唯一，都为primary_key）”。
# 3. 在两个需要做多对多的模型中随便选择一个模型，定义一个relationship属性，来绑定三者之间的关系，在使用relationship的时候，需要传入一个secondary=中间表。

# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# article1 = Article(title="article1")
# article2 = Article(title="article2")
#
# tag1 = Tag(name='tag1')
# tag2 = Tag(name='tag2')
#
# article1.tags.append(tag1)
# article1.tags.append(tag2)
#
# article2.tags.append(tag1)
# article2.tags.append(tag2)
#
# session.add(article1)
# session.add(article2)
#
# session.commit()

# article = session.query(Article).first()
# print(article.tags)

tag = session.query(Tag).first()
print(tag.articles)
```

### ORM层面的删除数据：
ORM层面删除数据，会无视mysql级别的外键约束。直接会将对应的数据删除，然后将从表中的那个外键设置为NULL。如果想要避免这种行为，应该将从表中的外键的`nullable=False`。
在SQLAlchemy，只要将一个数据添加到session中，和他相关联的数据都可以一起存入到数据库中了。这些是怎么设置的呢？其实是通过relationship的时候，有一个关键字参数cascade可以设置这些属性： 
当外键中的casecade被设置为空（非Null)时，外键关系不会添加
1. save-update：默认选项。在添加一条数据的时候，会把其他和他相关联的数据都添加到数据库中。这种行为就是save-update属性影响的。 
2. delete：表示当删除某一个模型中的数据的时候，是否也删掉使用relationship和他关联的数据。
3. delete-orphan：表示当对一个ORM对象解除了父表中的关联对象的时候，自己便会被删除掉。当然如果父表中的数据被删除，自己也会被删除。这个选项只能用在一对多上，不能用在多对多以及多对一上。并且还需要在子模型中的relationship中，增加一个single_parent=True的参数。 
4. merge：默认选项。当在使用session.merge，合并一个对象的时候，会将使用了relationship相关联的对象也进行merge操作。 
5. expunge：移除操作的时候，会将相关联的对象也进行移除。这个操作只是从session中移除，并不会真正的从数据库中删除。 
6. all：是对save-update, merge, refresh-expire, expunge, delete几种的缩写。




### 重写flask_sqlalchemy中的filter_by,filter

```python
class Query(BaseQuery):
    def filtery_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] =1
        return super(Query,self).filtery_by(**kwargs)

db = SQLAlchemy(query_class=Query)

# from gpt 
from sqlalchemy.orm import Query

class CustomQuery(Query):
    def filter_by(self, **kwargs):
        # 自定义的查询逻辑
        pass

    def filter(self, *args):
        # 自定义的查询逻辑
        pass

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app, query_class=CustomQuery)

# ...

users = db.session.query(User).filter_by(name='Alice').all()


```

### sqlalchemy 对JSON 字段操作
项目中的字段无法确定，动态变化或者考虑后续扩展时使用。
也可以使用text、varchar来代替，但是text、varchar是不支持搜索的，并且不支持局部更新，只能更改全部字段，增加了i/o操作，不利于性能。

```python

class User(db.Model):
    name= db.Column(db.String(32), comment='姓名')
    extra = db.Column(db.JSON, comment='扩展字段')
```

#### 增加数据：

```python
User(name = '张三', extra = dict(age=18, gender = 1, weght = 70kg))) 
user = User.query.filter(User.name == '张三').first()

```

#### 更新数据：

```python
from sqlalchemy.orm.attributes import flag_modified 
user.extra.update(dict(birthday=1998-12-12))) 
flag_modified(user, 'extra') 
db.session.add(user) 
db.session.commit()
```

#### 删除：

```python
user.extra.pop('birthday') 
flag_modified(user, 'extra') 
db.session.add(user) 
db.session.commit()
```

####查询：

```python

from sqlalchemy import cast, type_coerce
from sqlalchemy import String, JSON
import json
# 首先是针对单一数字、字符串时
User.query.filter(User.extra['age'] == 18, User.extra['weight'] == '70kg').first()
# 另一种特殊情况时,查询条件是一个对象时： 
# 先增加一组数据： 
user.extra.update(dict(info=dict(address='北京市'))) 
flag_modified(user, 'extra') 
db.session.commit() 
# 查询整个info时： 
User.query.filter(cast(User.extra['info'], String) == json.dumps({'address':'北京市'})).first() 
# or
User.query.filter(cast(User.extra['info'], String) == type_coerce({"address": "北京市"}, JSON)).first()

```
ref:[sqlalchemy中使用json](https://learnku.com/python/t/36061)

最近确实有这样的需求，但因为需求比较简单，没有做较多尝试，上面例子的操作最后一种查询还没有验证，后续如果使用到再更新


todo 测试get_or_404


## Flask-SQLAlchemy

### 安装：
```shell
pip install flask-sqlalchemy
```

### 数据库连接：
1. 跟sqlalchemy一样，定义好数据库连接字符串DB_URI。
2. 将这个定义好的数据库连接字符串DB_URI，通过`SQLALCHEMY_DATABASE_URI`这个键放到`app.config`中。示例代码：`app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI`.
3. 使用`flask_sqlalchemy.SQLAlchemy`这个类定义一个对象，并将`app`传入进去。示例代码：`db = SQLAlchemy(app)`。

### 创建ORM模型：
1. 还是跟使用sqlalchemy一样，定义模型。现在不再是需要使用`delarative_base`来创建一个基类。而是使用`db.Model`来作为基类。
2. 在模型类中，`Column`、`String`、`Integer`以及`relationship`等，都不需要导入了，直接使用`db`下面相应的属性名就可以了。
3. 在定义模型的时候，可以不写`__tablename__`，那么`flask_sqlalchemy`会默认使用当前的模型的名字转换成小写来作为表的名字，并且如果这个模型的名字使用了多个单词并且使用了驼峰命名法，那么会在多个单词之间使用下划线来进行连接。**虽然flask_sqlalchemy给我们提供了这个特性，但是不推荐使用。因为明言胜于暗喻**

### 将ORM模型映射到数据库：
1. db.drop_all()
2. db.create_all()

### 使用session：
以后session也不需要使用`sessionmaker`来创建了。直接使用`db.session`就可以了。操作这个session的时候就跟之前的`sqlalchemy`的`session`是iyimoyiyang的。

### 查询数据：
如果查找数据只是查找一个模型上的数据，那么可以通过`模型.query`的方式进行查找。`query`就跟之前的sqlalchemy中的query方法是一样用的。示例代码如下：
```python
users = User.query.order_by(User.id.desc()).all()
print(users)
```

### 对choice序列化
```python
from flask.json import JSONEncoder
from sqlalchemy_utils import Choice

class CustomJSONEncoder(JSONEncoder):
     def default(self, obj):
        if isinstance(obj, Choice):
            return obj.code

        return JSONEncoder.default(self, obj)  # aka super()

app.json_encoder = CustomJSONEncoder
```


### postgresql Enum update/add value

Enum 类型直接在model中添加了新的状态，然后再migrate是没有效果的。

```sql
CREATE TYPE "public"."visitstatus" AS ENUM ('pending_review', 'pending_visit', 'visiting','has_revisited','unnecessary_visit','visit_failed');

ALTER TYPE "public"."visitstatus" ADD VALUE 'visit_failed'

DROP TYPE "public"."visitstatus"
```



Ref:
[6. 枚举类型-postgresql教程 (cntofu.com)](https://www.cntofu.com/book/194/chapters/6.md)
[PostgreSQL删除或修改枚举 - 简书 (jianshu.com)](https://www.jianshu.com/p/de4f16953020)


### view model

```python from gpt

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)

class UserView(db.Model):
    __tablename__ = 'users_view'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(120))

    user = db.relationship(User, uselist=False, backref=db.backref('view', uselist=False))

    @hybrid_property
    def full_name(self):
        return self.username + ' (' + self.email + ')'

```


## alembic笔记：

alembic 与sqlalchemy 一样可以独立存在
使用alembic的步骤：
1. 定义好自己的模型。
2. 使用alembic创建一个仓库：`alembic init [仓库的名字，推荐使用alembic]`。
3. 修改配置文件：
    * 在`alembic.ini`中，给`sqlalchemy.url`设置数据库的连接方式。这个连接方式跟sqlalchemy的方式一样的。
    * 在`alembic/env.py`中的`target_metadata`设置模型的`Base.metadata`。但是要导入`models`，需要将models所在的路径添加到这个文件中。示例代码如下：
        ```python
        import sys,os
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))
		# this works fine
		from myapp.models import Base
		target_metadata = Base.metadata
        ```
4. 将ORM模型生成迁移脚本：`alembic revision --autogenerate -m 'message'`。
5. 将生成的脚本映射到数据库中：`alembic upgrade head`。
6. 以后如果修改了模型，重复4、5步骤。
7. 注意事项：在终端中，如果想要使用alembic，则需要首先进入到安装了alembic的虚拟环境中，不然就找不到这个命令。

### 常用命令：
1. init：创建一个alembic仓库。
2. revision：创建一个新的版本文件。
3. --autogenerate：自动将当前模型的修改，生成迁移脚本。
4. -m：本次迁移做了哪些修改，用户可以指定这个参数，方便回顾。
5. upgrade：将指定版本的迁移文件映射到数据库中，会执行版本文件中的upgrade函数。如果有多个迁移脚本没有被映射到数据库中，那么会执行多个迁移脚本。
6. [head]：代表最新的迁移脚本的版本号。
7. downgrade：会执行指定版本的迁移文件中的downgrade函数。
8. heads：展示head指向的脚本文件版本号。
9. history：列出所有的迁移版本及其信息。
10. current：展示当前数据库中的版本号。

### 经典错误：
1. FAILED: Target database is not up to date.
    * 原因：主要是heads和current不相同。current落后于heads的版本。
    * 解决办法：将current移动到head上。alembic upgrade head
2. FAILED: Can't locate revision identified by '77525ee61b5b'
    * 原因：数据库中存的版本号不在迁移脚本文件中
    * 解决办法：删除数据库的alembic_version表中的数据，重新执行alembic upgrade head
3. 执行`upgrade head`时报某个表已经存在的错误：
    * 原因：执行这个命令的时候，会执行所有的迁移脚本，因为数据库中已经存在了这个表。然后迁移脚本中又包含了创建表的代码。
    * 解决办法：（1）删除versions中所有的迁移文件。（2）修改迁移脚本中创建表的代码。
4. with session and commit but no data in database: 
	1.  this should in a session scope, even the object is returned by sqlalchemy



