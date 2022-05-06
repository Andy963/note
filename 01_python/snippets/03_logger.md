### logger(stream,time,file)
logger with stream_handler, TimeRotatingHandler, RotatingFileHandler

```python


import logging
import os
from logging import handlers


class Logger:
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self,
                 filename,
                 level='info',
                 when='D',
                 back_count=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):

        f_dir, f_name = os.path.split(filename)
        os.makedirs(f_dir, exist_ok=True)  # 当前目录新建log文件夹

        format_str = logging.Formatter(fmt)  # 设置日志格式

        self.logger = logging.getLogger(filename)
        self.logger.setLevel(self.level_relations.get(level,logging.INFO))  # 设置日志级别

        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式

        # 按时间分割的日志记录
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=back_count,
                                               encoding='utf-8')  # 往文件里写入指定间隔时间自动生成文件的Handler
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时
        # D 天
        # 'W0'-'W6' 每星期（interval=0时代表星期一：W0）
        # midnight 每天凌晨
        th.setFormatter(format_str)  # 设置文件里写入的格式

        # 按文件大小分割的日志记录
        fs = handlers.RotatingFileHandler(filename=filename,maxBytes=10*1024*1024,backupCount=back_count,encoding='utf-8')
        fs.setFormatter(format_str)

        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)
        self.logger.addHandler(fs)


# 测试
if __name__ == '__main__':
    logger = Logger('./logs/2020/app.log', 'debug', 'S', 5).logger

    logger.debug('debug')
    logger.info('info')
    logger.warning('警告')
    logger.error('报错')
    logger.critical('严重')

    # 单独记录error
    err_logger = Logger('./logs/2020/error.log', 'error', 'S', 3).logger
    err_logger.error('错误 error')
```

### TimeSplitLogger

```python
import logging
import os
from logging import handlers


class TimeSplitLogger:
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self,
                 filename,
                 level='info',
                 when='D',
                 back_count=5,
                 to_stream=False,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        f_dir, f_name = os.path.split(filename)
        os.makedirs(f_dir, exist_ok=True)  # 当前目录新建log文件夹

        format_str = logging.Formatter(fmt)  # 设置日志格式

        self.logger = logging.getLogger(filename)
        self.logger.setLevel(self.level_relations.get(level, logging.INFO))  # 设置日志级别

        # 按时间分割的日志记录
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=back_count,
                                               encoding='utf-8')  # 往文件里写入指定间隔时间自动生成文件的Handler
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时
        # D 天
        # 'W0'-'W6' 每星期（interval=0时代表星期一：W0）
        # midnight 每天凌晨
        th.setFormatter(format_str)  # 设置文件里写入的格式

        if to_stream:
            sh = logging.StreamHandler()  # 往屏幕上输出
            sh.setFormatter(format_str)  # 设置屏幕上显示的格式
            self.logger.addHandler(sh)  # 把对象加到logger里
        if not self.logger.handlers:
            self.logger.addHandler(th)

    def __call__(self):
        return self.logger


if __name__ == '__main__':
    logger = TimeSplitLogger('./logs/test.log')()
    logger.info('hello')

```

### FileSplitLogger
```python
import logging
import os
from logging import handlers


class FileSplitLogger:
    """
    按文件大小分割的logger
    logger 默认是单例模式，只要传入的日志文件名一样，得到的都是同一个对象，即使其它参数改变，也不影响
    """
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self,
                 filename,
                 level='info',
                 back_count=5,
                 max_bytes=10 * 1024 * 1024,
                 encoding='utf-8',
                 to_stream=False,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        f_dir, f_name = os.path.split(filename)
        os.makedirs(f_dir, exist_ok=True)  # 当前目录新建log文件夹

        format_str = logging.Formatter(fmt)  # 设置日志格式

        self.logger = logging.getLogger(filename)
        self.logger.setLevel(self.level_relations.get(level, logging.INFO))  # 设置日志级别,默认为INFO

        # 按文件大小分割的日志记录
        fs = handlers.RotatingFileHandler(filename=filename, maxBytes=max_bytes, backupCount=back_count,
                                          encoding=encoding)
        fs.setFormatter(format_str)
        if to_stream:
            sh = logging.StreamHandler()  # 往屏幕上输出
            sh.setFormatter(format_str)  # 设置屏幕上显示的格式
            self.logger.addHandler(sh)  # 把对象加到logger里
        if not self.logger.handlers:# 防止多个handler,导致多次打印相同内容
            self.logger.addHandler(fs)

    def __call__(self):
        return self.logger


if __name__ == '__main__':
    logger = FileSplitLogger('./logs/test.log', 'debug', max_bytes=100, )()
    for i in range(10):
        logger.info('how are you')

```