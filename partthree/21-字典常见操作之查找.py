# key值查找
dict1 = {'name': 'test1', 'age': 23, 'sex': '男'}
# print(dict1['name'])
# 函数方式查找
#  get()
# print(dict1.get('age'))
# 输出 23
# print(dict1.get('adsd'))
# 输出None
# keys()
# print(dict1.keys())
# 输出 dict_keys(['name', 'age', 'sex'])
# values()
# print(dict1.values())
# 输出 dict_values(['test1', 23, '男'])
# items()
print(dict1.items())
# 输出dict_items([('name', 'test1'), ('age', 23), ('sex', '男')])