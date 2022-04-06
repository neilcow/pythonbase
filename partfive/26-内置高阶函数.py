# 1、map()
list1 = [1, 2, 3, 4, 5]


def fun(i):
    return i ** 2


res = map(fun, list1)
print(res)
print(list(res))
# 输出[1, 4, 9, 16, 25]



# 2、reduce
import functools
list2 = [1, 2, 3, 4]


def fun1(a, b):
    return a + b


res = functools.reduce(fun1, list2)
print(res)
# 输出 10

# 3、filter
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def fun2(i):
    return i % 2 == 0


res = filter(fun2, list3)
print(list(res))
