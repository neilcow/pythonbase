# # 通用的装饰器，可以装饰任意类型的函数
#
# # 装饰带有参数的函数
# def decorator(func):
#     def inner(a, b):
#         # 在内部函数对已有函数进行装饰
#         print("正在努力执行加法计算")
#         func(a, b)
#     return inner
#
#
# # add_num = decorator(add_num)
# @decorator
# def add_num(num1, num2):
#     result = num1 + num2
#     print("结果为：", result)
#
#
# add_num(2, 4)


# 通用的装饰器，可以装饰任意类型的函数

# # 装饰带有参数的函数,有返回值
# def decorator(func):
#     def inner(a, b):
#         # 在内部函数对已有函数进行装饰
#         print("正在努力执行加法计算")
#         num = func(a, b)
#         return num
#     return inner
#
#
# # add_num = decorator(add_num)
# @decorator
# def add_num(num1, num2):
#     result = num1 + num2
#     return result
#
#
# result1 = add_num(2, 4)
# print("结果为：", result1)


# 装饰带有不定长的参数和返回值的函数
def decorator(func):
    def inner(*args, **kwargs):
        print("正在努力执行加法计算")
        num = func(*args, **kwargs)
        return num
    return inner


@decorator
def add_num(*args, **kwargs):
    result = 0
    # *args 把元组里面的每一个元素，按照位置参数的方式进行传参
    # **kwargs 把字典里的每一个键值对，按照关键字的方式进行传参
    # 这里对元组和字段进行闭包，仅限于结合不定长参数的函数使用
    for value in args:
        result += value

    for value in kwargs.values():
        result += value

    return result


result1 = add_num(1, 2)
print("结果为：", result1)