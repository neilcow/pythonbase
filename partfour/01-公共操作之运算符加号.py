str1 = ('aa', 'bb', 'cc')
str2 = ('cc', 'dd', 'ee')

tuple1 = (1, 3, 4, 5)
tuple2 = (4, 5, 6, 8)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

dict1 = {'name': 'test', 'sex': '男'}
dict2 = {'age': 23}

# + 合并的含义
print(str1 + str2)
# 输出 ('aa', 'bb', 'cc', 'cc', 'dd', 'ee')
print(tuple1 + tuple2)
# 输出 (1, 3, 4, 5, 4, 5, 6, 8)
print(list1 + list2)
# 输出[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
