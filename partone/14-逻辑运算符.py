a = 0
b = 1
c = 2
# 1. and 与： 都真才是真
print((a < b) and (c > b))
print((a > b) and (c > b))
# 2. or  或，一个真就是真，两个都是假 才是假
print((a < b) or (c > b))
print((a > b) or (c > b))
print((a > b) or (b > c))

# 3. not, 非，取反
print(not False)
print(not (c > b))