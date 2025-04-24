import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"\n{func.__name__} took {(end - start)*1000:.3f} milliseconds")
        return result
    return wrapper