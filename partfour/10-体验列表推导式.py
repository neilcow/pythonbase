# 需求,将0-10放到列表中
# 思路，先创建一个空列表，然后用while循环加进数据

# while实现---------------------
list1 = []
i = 0
while i < 10:
    list1.append(i)
    i += 1
print(list1)
# 输出 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for实现------------------------
list2 = []
for i in range(10):
    list2.append(i)
print(list2)
# 输出 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 列表推导式实现---------------------
list1 = [i for i in range(10)]
print(list1)
# 输出 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]