import copy

# num1 = 1
# num2 = copy.copy(num1)
# # 查看内存地址没有发生变化，说明没有对对象进行拷贝，也就说没有开辟新的内存空间
# print("num1:", id(num1), "num2:", id(num2))
#
# my_tuple1 = (3, 5)
# my_tuple2 = copy.copy(my_tuple1)
# print("my_tuple1:", id(my_tuple1), "my_tuple2:", id(my_tuple2))


# num1: 8791254989888 num2: 8791254989888
# my_tuple1: 31363016 my_tuple2: 31363016

# 可变类型： 列表 、字典、集合
my_list1 = [1, 3, [4, 6]]
my_list2 = copy.copy(my_list1)
print("my_list1:", id(my_list1), "my_list2:", id(my_list2))
my_list1.append(5)
print(my_list1, my_list2)
print("my_list1[2]", id(my_list1[2]), "my_list2[2]:", id(my_list2[2]))


# 输出
# my_list1: 35415880 my_list2: 35416200
# [1, 3, [4, 6], 5] [1, 3, [4, 6]]
# my_list1[2] 35415816 my_list2[2]: 35415816


