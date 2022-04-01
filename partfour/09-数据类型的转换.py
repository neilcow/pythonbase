tuple1 = (1, 2, 3, 4, 5)
list1 = ['a', 'b', 'c', 'd']
set1 = {100, 200, 300, 400}

# tuple
print(tuple(list1))
print(tuple(set1))
# 输出
# ('a', 'b', 'c', 'd')
# (200, 100, 400, 300)

# list1
print(list(tuple1))
print(list(set1))
# 输出
# [1, 2, 3, 4, 5]
# [200, 100, 400, 300]

# set 集合会自动去重
print(set(tuple1))
print(set(list1))
# 输出
# {1, 2, 3, 4, 5}
# {'a', 'c', 'd', 'b'}
