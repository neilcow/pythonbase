list1 = ["name", "age", "sex"]
list2 = ["test", 11, "男"]


dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)


