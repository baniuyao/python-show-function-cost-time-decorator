import time
import multiprocessing
import os
import sys


def print_cost_time(func):
    def __d(*args, **kwargs):
        st_time = time.time()
        func(*args, **kwargs)
        if sys.version_info.major == 2:
            func_name = func.func_name
        elif sys.version_info.major == 3:
            func_name = func.__name__
        t = round((time.time() - st_time) * 1000, 4)
        print '[function %s] [args %s] [kwargs %s] cost %s s' % (func_name, args, kwargs, t)

    return __d


@print_cost_time
def foo(name, age):
    return 'abc'


if __name__ == '__main__':
    foo('frank', 10)
