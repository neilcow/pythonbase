# 遍历字典的key
# dict1 = {'name': 'test1', 'aga': 12, 'sex': '男'}
# for key in dict1.keys():
#     print(key)

# 遍历字典的value
# dict1 = {'name': 'test1', 'aga': 12, 'sex': '男'}
# for value in dict1.values():
#     print(value)

# 遍历字典的元素
# dict1 = {'name': 'test1', 'aga': 12, 'sex': '男'}
# for item in dict1.items():
#     print(item)
# 输出('name', 'test1')
# ('aga', 12)
# ('sex', '男')

# 遍历字典的键值对(拆包)
dict1 = {'name': 'test1', 'aga': 12, 'sex': '男'}
for key, value in dict1.items():
    print(f'key的值是：{key}，value的值是：{value}')
# 输出
# key的值是：name，value的值是：test1
# key的值是：aga，value的值是：12
# key的值是：sex，value的值是：男