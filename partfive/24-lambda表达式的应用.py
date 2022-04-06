# 1、带判断的lambda
fn1 = lambda a, b: a if a > b else b
print(fn1(50, 20))

# 2、列表数据按字典key的值排序
list1 = [
    {'name': 'test1', 'age': 12},
    {'name': 'test2', 'age': 13},
    {'name': 'test3', 'age': 14}
]
# list1.sort(key=lambda x: x['name'], reverse=True)
# print(list1)
# 输出 [{'name': 'test3', 'age': 14}, {'name': 'test2', 'age': 13}, {'name': 'test1', 'age': 12}]
list1.sort(key=lambda x: x['age'])
print(list1)
# 输出 [{'name': 'test1', 'age': 12}, {'name': 'test2', 'age': 13}, {'name': 'test3', 'age': 14}]