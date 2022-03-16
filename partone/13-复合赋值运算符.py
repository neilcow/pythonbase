a = 10
a += 1 # a = a + 1
print(a)

b = 10
b -= 1  # b = b - 1
print(b)

# 先算复合运算符有右边的表达式，再算复合运算符
d = 10
d *= 1 + 2  # d = d * (1 + 2)
print(d)
