from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time() - startTime
        print(f"[Function '{func.__name__}' took {endTime} seconds to run]")
    return wrapper

@timer
def measureMe():
    time.sleep(2.0)

def main():
    measureMe()

if __name__ == "__main__":
    main()