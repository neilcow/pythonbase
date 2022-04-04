# 方法一
def num():
    a = 10
    b = 20
    c = 0
    c = a
    a = b
    b = c
    print(a)
    print(b)


num()
# 方法二
a, b = 1, 2
a, b = b, a
print(a)
print(b)