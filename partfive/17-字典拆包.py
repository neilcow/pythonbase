dict1 = {'name': 'test', 'age': 23, 'gender': '男'}


# 用字典拆包，拆后得到的都是key的值，然后通过key的值，获取value
a, b, c = dict1
print(a)
print(b)
print(c)

print(dict1[a])
print(dict1[b])
print(dict1[c])
