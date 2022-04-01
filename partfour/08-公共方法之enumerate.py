# enumerate(可遍历对象，start=0)
list1 = {'a', 'b', 'c', 'd', 'e', 'f'}
for i in enumerate(list1, 3):
    print(i)

# 输出
# (3, 'f')
# (4, 'a')
# (5, 'c')
# (6, 'd')
# (7, 'e')
# (8, 'b')
