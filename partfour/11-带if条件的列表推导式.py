list1 = [i for i in range(0, 10, 2)]
print(list1)
list2 = []
for i in range(0, 10):
    if i % 2 == 0:
        list2.append(i)
print(list2)

list3 = [i for i in range(0, 10) if i % 2 ==0]
print(list3)