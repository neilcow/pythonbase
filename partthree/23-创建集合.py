# 1、有数据集合
s1 = {10, 20, 30, 40, 50}
print(s1)
# 输出 {40, 10, 50, 20, 30}
s2 = {10, 10, 30, 40, 50, 40}
print(s2)
# 输出 {40, 10, 50, 30}
s3 = set()
print(type(s3))
# 输出 <class 'set'>
s4 = {}
print(type(s4))
# 输出 <class 'dict'>
s5 = set('abcedf')
print(s5)
# 输出 {'c', 'f', 'a', 'b', 'e', 'd'}
