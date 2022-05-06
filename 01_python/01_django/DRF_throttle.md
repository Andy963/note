# DRF_throttle

## custom throttle 

```py
VISIT_RECORD = {} #定义全局变量，用于存放访问记录
class VisitThrottle(object):

    def __init__(self):　　　　 #用于await计算剩余访问时间
        self.history = None
        self.throttle_time = 60
        self.throttle_rate = 10

    def allow_request(self,request,view):
        #获取用户ip作为唯一的标示
        remote_addr = request.META.get('REMOTE_ADDR')

        # 获取当前访问的时刻
        ctime = time.time()
        # 这是用户第一次访问,将其进行记录，并且返回True，允许继续访问
         if remote_addr not in VISIT_RECORD:
             VISIT_RECORD[remote_addr] = [ctime,]
             return True

        # 如果不是第一次访问，获取所有的记录
        history = VISIT_RECORD.get(remote_addr)

        self.history = history
        # 判断最开始的时刻与现在的时刻的差值是否在规定的时间范围内，比如在60s内，如果不在，
        # 可以去除最开始的时刻记录
        while history and history[-1] < ctime - self.throttle_time:
            history.pop()
        # 此时列表中的时刻记录都是在规定的时间范围内，判断时刻的个数也就是访问的次数

        if len(history) < self.throttle_rate:
            history.insert(0,ctime)
            return True

    def wait(self):
        # 还需要等多少秒才能访问
        ctime = time.time()
        return self.throttle_time - (ctime - self.history[-1])
```

上面的全局变量Visit_record 可以通过threading.local来实现，做到线程，协程安全等

```py
# 兼容线程协程
try:
    from greenlet import getcurrent as get_ident
except Exception as e:
    from threading import get_ident
from threading import Thread

class Local(object):
    storage = {}

    def set(self, k, v):
        ident = get_ident()
        if ident in Local.storage:
            Local.storage[ident][k] = v
        else:
            Local.storage[ident] = {k: v}

    def get(self, k):
        ident = get_ident()
        return Local.storage[ident][k]

# 通过setattr,getattr实现
class Local(object):
    def __init__(self):
        object.__setattr__(self,'storage',{})
    def __setattr__(self, k, v):
        ident = get_ident()
        if ident in self.storage:
            self.storage[ident][k] = v
        else:
            self.storage[ident] = {k: v}
    def __getattr__(self, k):
        ident = get_ident()
        if ident in self.storage:
            return self.storage[ident][k]
            
obj = Local()
def task(arg):
    obj.val = arg
    obj.xxx = arg
    print(obj.val)
for i in range(10):
    t = Thread(target=task,args=(i,))
    t.start()
```