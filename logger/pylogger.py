__version__ = "0.0.1"

import logging
import os
import sys
import types
import io
import traceback


if hasattr(sys, 'frozen'):  # support for py2exe
    _srcfile = "logging%s__init__%s" % (os.sep, __file__[-4:])
elif str.lower(__file__[-4:]) in ['.pyc', '.pyo']:
    _srcfile = __file__[:-4] + '.py'
else:
    _srcfile = __file__
_srcfile = os.path.normcase(_srcfile)


class CCLogger(logging.Logger):
    def __init__(self, name='root', loglevel='DEBUG', handler=logging.StreamHandler()):
        if isinstance(name, str):
            pass
        elif isinstance(name, types.TypeType) or isinstance(name, types.ClassType):
            name = name.__name__
        elif isinstance(name, types.ObjectType):
            name = name.__class__.__name__

        super(CCLogger, self).__init__(name)
        if not self.handlers:
            self.setLevel(getattr(logging, loglevel.upper()))
            ch = handler
            ch.setLevel(getattr(logging, loglevel.upper()))
            formatter = logging.Formatter(
                '%(asctime)s %(levelname)s: %(processName)s[%(process)d] %(filename)s:[%(name)s]:%(funcName)s [line %(lineno)d] - %(message)s -- %(varinfo)s')
            ch.setFormatter(formatter)
            self.addHandler(ch)

    def findCaller(self, stack_info=False):
        """
        Have to do this otherwise it will only show this frame
        """
        f = logging.currentframe()
        if f is not None:
            f = f.f_back
        rv = "(unknown file)", 0, "(unknown function)", None
        while hasattr(f, "f_code"):
            co = f.f_code
            filename = os.path.normcase(co.co_filename)
            if filename in (_srcfile, logging._srcfile):
                f = f.f_back
                continue
            sinfo = None
            if stack_info:
                sio = io.StringIO()
                sio.write('Stack (most recent call last):\n')
                traceback.print_stack(f, file=sio)
                sinfo = sio.getvalue()
                if sinfo[-1] == '\n':
                    sinfo = sinfo[:-1]
                sio.close()
            rv = (filename, f.f_lineno, co.co_name, sinfo)
            break
        return rv

    def debug(self, message, *args, **kwargs):
        exc_info = kwargs.pop('exc_info', False)
        extra = kwargs.pop('extra', {})
        if 'varinfo' not in extra:
            extra['varinfo'] = {}
        extra['varinfo'].update(kwargs)
        super(CCLogger, self).debug(
            message, *args, exc_info=exc_info, extra=extra)

    def warning(self, message, *args, **kwargs):
        exc_info = kwargs.pop('exc_info', False)
        extra = kwargs.pop('extra', {})
        if 'varinfo' not in extra:
            extra['varinfo'] = {}
        extra['varinfo'].update(kwargs)
        super(CCLogger, self).warning(
            message, *args, exc_info=exc_info, extra=extra)

    def info(self, message, *args, **kwargs):
        exc_info = kwargs.pop('exc_info', False)
        extra = kwargs.pop('extra', {})
        if 'varinfo' not in extra:
            extra['varinfo'] = {}
        extra['varinfo'].update(kwargs)
        super(CCLogger, self).info(
            message, *args, exc_info=exc_info, extra=extra)

    def error(self, message, *args, **kwargs):
        exc_info = kwargs.pop('exc_info', False)
        extra = kwargs.pop('extra', {})
        if 'varinfo' not in extra:
            extra['varinfo'] = {}
        extra['varinfo'].update(kwargs)
        super(CCLogger, self).error(
            message, *args, exc_info=exc_info, extra=extra)

    def critical(self, message, *args, **kwargs):
        exc_info = kwargs.pop('exc_info', False)
        extra = kwargs.pop('extra', {})
        if 'varinfo' not in extra:
            extra['varinfo'] = {}
        extra['varinfo'].update(kwargs)
        super(CCLogger, self).critical(
            message, *args, exc_info=exc_info, extra=extra)

    def exception(self, message, *args, **kwargs):
        exc_info = kwargs.pop('exc_info', True)
        extra = kwargs.pop('extra', {})
        if 'varinfo' not in extra:
            extra['varinfo'] = {}
        extra['varinfo'].update(kwargs)
        super(CCLogger, self).exception(
            message, *args, exc_info=exc_info, extra=extra)

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.debug(line.rstrip())
