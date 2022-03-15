# 1、float() ，将数据类型转换为浮点型
num1 = 23
str1 = '123'
print(type(float(num1)))
print(float(num1))
print(float(str1))
# 2、str(),将数据转化为字符串型
print(type(str(num1)))

# 3、tuple(), 将一个序列转换成元组
list1 = [1, 2, 3, 4]
print(tuple(list1))

# 4、list() 将一个序列转换为列表
tuple1 = (100, 200, 300, 400)
print(list(tuple1))

# 5、eval() 计算在字符串中有效的python表达式，并返回一个对象
str2 = '1'
str3 = '1.1'
str4 = '(1, 2, 3, 4)'
str5 = '[100, 200, 300, 400]'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))

