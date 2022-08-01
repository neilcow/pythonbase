import time


def decorator(func):
    def inner():
        begin = time.time()
        func()
        end = time.time()
        result = end - begin
        print("函数执行完成耗时:", result)
    return inner


@decorator
def work():
    for i in range(1000):
        print(i)


work()
