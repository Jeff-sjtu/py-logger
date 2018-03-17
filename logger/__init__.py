from . import *
import sys
if sys.version_info > (3, 0):
    from .pylogger import CCLogger
else:
    from .py2logger import CCLogger
