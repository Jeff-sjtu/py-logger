A simple and convenient logger wrapper.
一个简单的logger实现

# Usage
``` python
from logger import CCLogger


def test_function():
    StreamLogger.warning('This is warning test.', a='this is a')
    StreamLogger.info('This is info.')


if __name__ == "__main__":
    StreamLogger = CCLogger(name='DebugLog', loglevel='DEBUG')
    test_function()
```

logger的输出可以精确定位到进程号、文件、函数，以及行号。
``` 
2018-03-17 15:44:39,593 WARNING: MainProcess[11240] test_logger.py:[DebugLog]:test_function [line 5] - This is warning test. -- {'a': 'this is a'}

2018-03-17 15:44:39,597 INFO: MainProcess[11240] test_logger.py:[DebugLog]:test_function [line 6] - This is info. -- {}
```