import copy

# num1 = 1
# num2 = copy.deepcopy(num1)
# print("num1:", id(num1), "num2:", id(num2))
#
# str1 = 'hello'
# str2 = copy.deepcopy(str1)
# print("str1:", id(str1), "str2:", id(str2))
#
# my_tuple1 = (1, 2)
# my_tuple2 = copy.deepcopy(my_tuple1)
# print("my_tuple1:", id(my_tuple1), "my_tuple2:", id(my_tuple2))
#
#
# my_tuple3 = (1, [1, 2])
# my_tuple4 = copy.deepcopy(my_tuple3)
# print("my_tuple3:", id(my_tuple3), "my_tuple4:", id(my_tuple4))


# 输出
# num1: 8791250992192 num2: 8791250992192
# str1: 35017200 str2: 35017200
# my_tuple1: 34967496 my_tuple2: 34967496
# my_tuple3: 35475400 my_tuple4: 35350920
my_list1 = [1, [2, 3]]
my_list2 = copy.deepcopy(my_list1)
print("my_list1:", id(my_list1), "my_list2:", id(my_list2))
print("my_list1[0]:", id(my_list1[0]), "my_list2[0]:", id(my_list2[0]))
print("my_list1[1]:", id(my_list1[1]), "my_list2[1]:", id(my_list2[1]))

# 输出
# my_list1: 31877064 my_list2: 31877384
# my_list1[0]: 8791250992192 my_list2[0]: 8791250992192
# my_list1[1]: 31877000 my_list2[1]: 31884040