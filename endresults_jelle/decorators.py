from functools import wraps
import time

def time_function(func):
    @wraps(func)
    def wrapper(*args, **kwds):
        start = time.perf_counter()
        func(*args, **kwds)
        end = time.perf_counter()

        print(f"Function {func.__name__} took: {'%.4f' % (end - start)} seconds.")
    return wrapper