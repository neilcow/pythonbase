print(abs(-10))
print(round(2.7))


# 方法一
def sum_num(a, b):
    return abs(a) + abs(b)


res = sum_num(-12, 23)
print(res)


# 方法二
def sum(a, b, f):
    return f(a) + f(b)


res = sum(18.23, 23.23, round)
print(res)
