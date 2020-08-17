# DRF serializer


serializer中的类并不多，主要有BaseSerializer， serializer, ListSerializer, ModelSerializer, HyperlinkedModelSerializer,它们之间的继承关系如下：没错，它们的父类是Field.

![serializer继承关系](vimages/20200223150508167_17792.png =650x)

在前面的view中我们知道，除了list之外有对数据库操作的就是create, update, destory等。而destory只需要对实例执行delete即可。剩下的create,update我们查看一下它的源代码：

## CreateModelMixin & UpdateModelMixin

```python
class CreateModelMixin:
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

class UpdateModelMixin:
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
```

我们可以看到，不管是create,update最后都是执行serializer.注意，view中的create,update并不执行数据库操作，真正执行操作的是serializer的save方法。这个方法继承自BaseSerializer中，我们看源码（源码太多，去掉了其它部分）：
其中的update,create对子类做了限制，是必须实现的方法，也是save方法最终要执行的动作，即我们在子类中实现的update, create方法。

## BaseSerializer

```python
class BaseSerializer(Field):

    def update(self, instance, validated_data):
        raise NotImplementedError('`update()` must be implemented.')

    def create(self, validated_data):
        raise NotImplementedError('`create()` must be implemented.')

    def save(self, **kwargs):
        assert not hasattr(self, 'save_object'), (
            'Serializer `%s.%s` has old-style version 2 `.save_object()` '
            'that is no longer compatible with REST framework 3. '
            'Use the new-style `.create()` and `.update()` methods instead.' %
            (self.__class__.__module__, self.__class__.__name__)
        )

        assert hasattr(self, '_errors'), (
            'You must call `.is_valid()` before calling `.save()`.'
        )

        assert not self.errors, (
            'You cannot call `.save()` on a serializer with invalid data.'
        )

        # Guard against incorrect use of `serializer.save(commit=False)`
        assert 'commit' not in kwargs, (
            "'commit' is not a valid keyword argument to the 'save()' method. "
            "If you need to access data before committing to the database then "
            "inspect 'serializer.validated_data' instead. "
            "You can also pass additional keyword arguments to 'save()' if you "
            "need to set extra attributes on the saved model instance. "
            "For example: 'serializer.save(owner=request.user)'.'"
        )

        assert not hasattr(self, '_data'), (
            "You cannot call `.save()` after accessing `serializer.data`."
            "If you need to access data before committing to the database then "
            "inspect 'serializer.validated_data' instead. "
        )

        validated_data = dict(
            list(self.validated_data.items()) +
            list(kwargs.items())
        )

        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
            assert self.instance is not None, (
                '`update()` did not return an object instance.'
            )
        else:
            self.instance = self.create(validated_data)
            assert self.instance is not None, (
                '`create()` did not return an object instance.'
            )

        return self.instance

    def is_valid(self, raise_exception=False):
        assert not hasattr(self, 'restore_object'), (
            'Serializer `%s.%s` has old-style version 2 `.restore_object()` '
            'that is no longer compatible with REST framework 3. '
            'Use the new-style `.create()` and `.update()` methods instead.' %
            (self.__class__.__module__, self.__class__.__name__)
        )

        assert hasattr(self, 'initial_data'), (
            'Cannot call `.is_valid()` as no `data=` keyword argument was '
            'passed when instantiating the serializer instance.'
        )

        if not hasattr(self, '_validated_data'):
            try:
                self._validated_data = self.run_validation(self.initial_data)
            except ValidationError as exc:
                self._validated_data = {}
                self._errors = exc.detail
            else:
                self._errors = {}

        if self._errors and raise_exception:
            raise ValidationError(self.errors)

        return not bool(self._errors)

```

我们看看serializer

## serializer

可以看到serializer中并没有实现create, update方法，所以如果我们直接使用Serializer,必须自己实现create, update方法。否则是会报错的。

```python
class Serializer(BaseSerializer, metaclass=SerializerMetaclass):
    default_error_messages = {
        'invalid': _('Invalid data. Expected a dictionary, but got {datatype}.')
    }

    @cached_property
    def fields(self):
        pass

    @property
    def _writable_fields(self):
        pass

    @property
    def _readable_fields(self):
        pass

    def get_fields(self):
        pass

    def get_validators(self):
        pass

    def get_initial(self):
        pass

    def get_value(self, dictionary):
        pass

    def run_validation(self, data=empty):
        pass

    def _read_only_defaults(self):
        pass

    def run_validators(self, value):
        pass

    def to_internal_value(self, data):
        pass

    def to_representation(self, instance):
        pass

    def validate(self, attrs):
        return attrs

    def __repr__(self):
        return representation.serializer_repr(self, indent=1)

    def __iter__(self):
        for field in self.fields.values():
            yield self[field.field_name]

    def __getitem__(self, key):
        pass

    @property
    def data(self):
        ret = super().data
        return ReturnDict(ret, serializer=self)

    @property
    def errors(self):
        pass
```

再看看我们比较常用的ModelSerializer

## ModelSerializer

```python
class ModelSerializer(Serializer):
    def create(self, validated_data):
        """
        We have a bit of extra checking around this in order to provide
        descriptive messages when something goes wrong, but this method is
        essentially just:

            return ExampleModel.objects.create(**validated_data)

        If there are many to many fields present on the instance then they
        cannot be set until the model is instantiated, in which case the
        implementation is like so:

            example_relationship = validated_data.pop('example_relationship')
            instance = ExampleModel.objects.create(**validated_data)
            instance.example_relationship = example_relationship
            return instance

        The default implementation also does not handle nested relationships.
        If you want to support writable nested relationships you'll need
        to write an explicit `.create()` method.
        """
        raise_errors_on_nested_writes('create', self, validated_data)

        ModelClass = self.Meta.model

        # Remove many-to-many relationships from validated_data.
        # They are not valid arguments to the default `.create()` method,
        # as they require that the instance has already been saved.
        info = model_meta.get_field_info(ModelClass)
        many_to_many = {}
        for field_name, relation_info in info.relations.items():
            if relation_info.to_many and (field_name in validated_data):
                many_to_many[field_name] = validated_data.pop(field_name)

        try:
            instance = ModelClass._default_manager.create(**validated_data)
        except TypeError:
            tb = traceback.format_exc()
            msg = (
                'Got a `TypeError` when calling `%s.%s.create()`. '
                'This may be because you have a writable field on the '
                'serializer class that is not a valid argument to '
                '`%s.%s.create()`. You may need to make the field '
                'read-only, or override the %s.create() method to handle '
                'this correctly.\nOriginal exception was:\n %s' %
                (
                    ModelClass.__name__,
                    ModelClass._default_manager.name,
                    ModelClass.__name__,
                    ModelClass._default_manager.name,
                    self.__class__.__name__,
                    tb
                )
            )
            raise TypeError(msg)

        # Save many-to-many relationships after the instance is created.
        if many_to_many:
            for field_name, value in many_to_many.items():
                field = getattr(instance, field_name)
                field.set(value)

        return instance

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        # Simply set each attribute on the instance, and then save it.
        # Note that unlike `.create()` we don't need to treat many-to-many
        # relationships as being a special case. During updates we already
        # have an instance pk for the relationships to be associated with.
        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        instance.save()

        # Note that many-to-many fields are set after updating instance.
        # Setting m2m fields triggers signals which could potentially change
        # updated instance and we do not want it to collide with .update()
        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.set(value)

        return instance

    # Determine the fields to apply...

    def get_fields(self):
        pass

    def get_field_names(self, declared_fields, info):
        pass

    def get_default_field_names(self, declared_fields, model_info):
        pass

    def build_field(self, field_name, info, model_class, nested_depth):
        pass

    def build_standard_field(self, field_name, model_field):
        pass

    def build_relational_field(self, field_name, relation_info):
        pass

    def build_nested_field(self, field_name, relation_info, nested_depth):
        pass

    def build_property_field(self, field_name, model_class):
        pass

    def build_url_field(self, field_name, model_class):
        pass

    def build_unknown_field(self, field_name, model_class):
        pass

    def include_extra_kwargs(self, kwargs, extra_kwargs):
        pass

    def get_extra_kwargs(self):
        pass

    def get_uniqueness_extra_kwargs(self, field_names, declared_fields, extra_kwargs):
        pass

    def _get_model_fields(self, field_names, declared_fields, extra_kwargs):
        pass

    def get_validators(self):
        """
        Determine the set of validators to use when instantiating serializer.
        """
        # If the validators have been declared explicitly then use that.
        validators = getattr(getattr(self, 'Meta', None), 'validators', None)
        if validators is not None:
            return list(validators)

        # Otherwise use the default set of validators.
        return (
            self.get_unique_together_validators() +
            self.get_unique_for_date_validators()
        )

    def get_unique_together_validators(self):
        """
        Determine a default set of validators for any unique_together constraints.
        """
        model_class_inheritance_tree = (
            [self.Meta.model] +
            list(self.Meta.model._meta.parents)
        )

        # The field names we're passing though here only include fields
        # which may map onto a model field. Any dotted field name lookups
        # cannot map to a field, and must be a traversal, so we're not
        # including those.
        field_names = {
            field.source for field in self._writable_fields
            if (field.source != '*') and ('.' not in field.source)
        }

        # Special Case: Add read_only fields with defaults.
        field_names |= {
            field.source for field in self.fields.values()
            if (field.read_only) and (field.default != empty) and (field.source != '*') and ('.' not in field.source)
        }

        # Note that we make sure to check `unique_together` both on the
        # base model class, but also on any parent classes.
        validators = []
        for parent_class in model_class_inheritance_tree:
            for unique_together in parent_class._meta.unique_together:
                if field_names.issuperset(set(unique_together)):
                    validator = UniqueTogetherValidator(
                        queryset=parent_class._default_manager,
                        fields=unique_together
                    )
                    validators.append(validator)
        return validators

    def get_unique_for_date_validators(self):
        """
        Determine a default set of validators for the following constraints:

        * unique_for_date
        * unique_for_month
        * unique_for_year
        """
        info = model_meta.get_field_info(self.Meta.model)
        default_manager = self.Meta.model._default_manager
        field_names = [field.source for field in self.fields.values()]

        validators = []

        for field_name, field in info.fields_and_pk.items():
            if field.unique_for_date and field_name in field_names:
                validator = UniqueForDateValidator(
                    queryset=default_manager,
                    field=field_name,
                    date_field=field.unique_for_date
                )
                validators.append(validator)

            if field.unique_for_month and field_name in field_names:
                validator = UniqueForMonthValidator(
                    queryset=default_manager,
                    field=field_name,
                    date_field=field.unique_for_month
                )
                validators.append(validator)

            if field.unique_for_year and field_name in field_names:
                validator = UniqueForYearValidator(
                    queryset=default_manager,
                    field=field_name,
                    date_field=field.unique_for_year
                )
                validators.append(validator)

        return validators
```

ModelSerializer都实现了create, update方法，所以当使用ModelSerializer时，就不需要自己实现这些方法了。除非需要对它做额外的操作。

至于另外的ListSerializer,HyperlinkedModelSerializer因为使用得少，暂时不分析。

## serializer使用

看了这么多源码，还不知道怎么用，显然我们的目的并不仅仅是看看源码，而是要应用它。

### serializer

### 常用的field
CharField、BooleanField、IntegerField、DateTimeField，HiddenField.
除了HiddenField，其它字段都很常见，而HiddenField值不依靠输入，但需要设置默认的值，不需要用户自己post数据过来。比如用户，我们可以通过context上下文获取当前登陆的用户：

```python
class CurrentUser(object):
    def set_context(self, serializer_field):
        self.user_obj = serializer_field.context['request'].user

    def __call__(self):
        return self.user_obj

class ArticleSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=CurrentUser())
    title = serializers.CharField(max_length=64)
    content = serializers.CharField()

    def create(self, validated_data):
        user = self.context['request'].user
        title = validated_data['title']
        content = validated_data['content ']
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.content = validated_data.get('content')
        instance.save()
        return instance
```
因为使用serializer,所以我们要实现create,update方法。而create中的参数都可以通过validated_data中获取 ，类似于form中的cleaned_data,而user则是通过上下文获取 。

至于update的前提则是已经获取到instance.。而create, update方法最后都可以返回instance,而这一点在view中调用了
serializer.is_valid()方法，此时就得到了instance对象。基于这一点，在使用ModelSerializer时，我们可以通过重写create, update, 或者perform_update,perform_create等方法，在判断is_valid()方法后获取到instance，在save之前可以对它进行操作，比如ser.save(user=user_obj).


### 核心参数
我们先看看serializer中的核心参数：

> read_only：True表示不允许用户自己上传，只能用于api的输出。如果某个字段设置了read_only=True，那么就不需要进行数据验证，只会在返回时，将这个字段序列化后返回
write_only: 与read_only对应
required: 顾名思义，就是这个字段是否必填。
allow_null/allow_blank：是否允许为NULL/空 。
error_messages：出错时，信息提示,与form表单一样。
label: 字段显示设置，如 label=’验证码’
help_text: 在指定字段增加一些提示文字，这两个字段作用于api页面比较有用
style: 说明字段的类型，这样看可能比较抽象，如：
> `password = serializers.CharField(style={'input_type': 'password'})`
> validators:指定验证器。

### validators
如果对django的form表单比较了解，可以很容易理解这些字段的意思。比如这里的validators,在form中也是存在的。
```python
class UserSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, min_length=11)
```
这里的serializer虽然能提供简单的长度验证，但远远不够，此时我们就需要指定Validators:
```python
def phone_validator(value):
    pattern = r"^1[3|4|5|6|7|8|9]\d{9}$"
    if not re.match(pattern, value):
        raise ValidationError('手机号格式错误')
    return value

class UserSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, min_length=11, validators=[phone_validator, ])
```

### UniqueValidator

指定某一个对象是唯一的，如，电话号只能存在且唯一

```python
phone = serializers.CharField(
    max_length=11,
    min_length=11,
    validators=[UniqueValidator(queryset=UserProfile.objects.all())
    )
```

### UniqueTogetherValidator

queryset：required，用于明确验证唯一性集合，必须设置
fields: required，字段列表或者元组，字段必须是序列化类中存在的字段
message：当验证失败时的提示信息

UniqueTogetherValidator有一个隐性要求就是验证的字段必须要提供值，除非设置了一个默认值,并且它需要在Meta中设置：

比如要求用户昵称与邮箱联合唯一：

```python
class UserSerializer(serializers.Serializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=UserProfile.objects.all(),
                fields=('username', 'email')
            )
        ]

```


### 局部钩子validate_phone

这里以短信验证码登陆时的验证为例，我们在给用户发送短信验证码后会将它存入redis，当我们验证时，就需要与redis中进行对比，在form中我们获取初始数据是通过self.cleaned_data, 这里是通过self.initial_data,获取到phone然后去redis根据电话号取验证码，与用户传过来的进行对比。
```python
def message_code_validator(value):
    if not value.isdecimal() or len(value) != 4:
        raise ValidationError('短信验证码格式错误')

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(label='手机号', validators=[phone_validator, ])
    code = serializers.CharField(label="验证码", validators=[message_code_validator, ])

    def validate_code(self, value):
        phone = self.initial_data.get('phone')
        conn = get_redis_connection()
        code = conn.get(phone)
        if not code:
            raise ValidationError('短信验证码已失效')
        if value != code.decode('utf-8'):
            raise ValidationError('短信验证码错误')
        return value
```

### 全局钩子validate

```python
class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(label='密码', validators=[password_validator, ])
    password2 = serializers.CharField(label="验证密码", validators=[password_validator, ])

    def validate(self, value):
        password = self.initial_data.get('password')
        password2 = self.initial_data.get('password2')

        if password != password2:
            raise ValidationError('两次密码不一致')
        return value
```

### serializer中的外键 

外键关系在日常使用中非常常见的那么我们要怎么获取外键呢？

#### 指定source

```python
class ArticleSerializer(serializers.ModelSerializer):
    # 指定外键显示的字段来源,其中category是Article的一个字段
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Article
        fields = "__all__" 
```


#### serializer嵌套

tag我们使用另一个serializer, TagSerializer. 这里因为是多对多，所以指定many=True
```python
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    # 指定外键显示的字段来源
    category = serializers.CharField(source='category.name')
    tag = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = "__all__" 
```

#### 指定depth

指定嵌套尝试是不推荐的方式。

```python
class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"
        depth = 1
```

默认情况下depth=0, 即不会跨表取值 ，这里指定depth=1,它就会跨到category表中，把category表中的所有数据拿到（注意是所有，包括你并不需要的）。因为它会拿到你不需要的数据，如果尝试较深，就又比较影响效率，所以不推荐这种用法。

### serializer中的choice

选择型字段也是非常常见的字段，为了方便存数据，我们一般不会存choice对应的文字，而是存一个数字，或者字符
那取值时要怎么取呢？


```python
class Article(models.Model):
    """
    文章表
    """
    status_choices = (
        (1, '发表'),
        (2, '删除'),
    )
    status = models.IntegerField(verbose_name='状态', choices=status_choices, default=1)

```

#### source

```python

class ArticleSerializer(seriliazers.Serializer):
    status_text = serializers.CharField(source='get_status_display')
```

#### serializers.MethodField

```python
class ArticleSerializer(seriliazers.Serializer):
    status_text = serializers.SerializerMethodField()

    def get_status_text(self, obj):
        return obj.get_status_display()
```

可以看到这两种方法与form表单也保持了一致，都是通过get_status_display来实现的。其中第二种obj指的是当前article对象。

### to_internal_value
to_internal_value是在外部数据传进来时进行处理的函数，通常情况下，状态码在数据库中只保存一个数字即可，在查看时我们要看后面对应的文字。对于传入的数据，我们可以 在此验证。如果是数字类型，那么它必须只能是0,1,如果是文字，那么对它进行转换，最后存入数据库的仍为数字。最后返回 data，它的处理在validate之前。
```python
STATES_CODE = (
	(0,'失败'),
	(1,'成功'),
	)

def to_internal_value(self,data):
	"""
	传入的data是个字典类型
	最后一定要返回data
	"""

	states = data.get('states')
	if states not in [i[1] for i in STATES_CODE]:
		raise ValueError('states的选项不正确')
		
	if not isinstance(states,int):
		for item in STATES_CODE:
			if item[1] == states:
				data['states'] = item[0]
	return data

```
### to_representation
to_presentation控制数据的输出时的形式，比如，字段如果设置为blank=True,null=True,最后数据可能为Null,这样就会导致输出的数据为Null,此时我们可以对它进行处理。
指定这种情况下显示的值。

```python
def to_presentation(self,instance):
	if not data['ver']:
		data['ver'] = ''

	if not data['status']:
		data['status'] = '状态未知'

	return data
```

### 日期序列化

```py
import json
from datetime import datetime
from datetime import date

#对含有日期格式数据的json数据进行转换
class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):
        if isinstance(field,datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field,date):
            return field.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self,field)


d1 = datetime.now()

dd = json.dumps(d1,cls=JsonCustomEncoder)
print(dd)
```

