from functools import wraps

def timer(func):
    import time
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_started = time.time()
        result = func(*args, **kwargs)
        time_ended = time.time()
        print(f"Function {func.__name__} executed in {time_started - time_ended}s")
        return result
    
    return wrapper


class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @timer
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value


if __name__ == "__main__":
    x = Celsius(100)
    print(x.to_fahrenheit())