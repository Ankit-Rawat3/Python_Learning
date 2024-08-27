import time


def time_decorator(func):
    def wrapper():
        start_time=time.time()
        print(start_time)
        func()
        end_time=time.time()
        print(end_time)
        print(f" time take by func {end_time-start_time}")
    return wrapper()

@time_decorator
def test_ui1():
    print("Add a func, time taken to finish this function")
    time.sleep(2)

@time_decorator
def test_ui2():
    print("Add a func, time taken to finish this function")
    time.sleep(5)

