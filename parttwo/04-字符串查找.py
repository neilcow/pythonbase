str1 = 'hello world and python and python and python'
# print(str1.find('and'))  # 在整个字符串中查找and，找到后返回第一个下标，找不到返回 -1
# print(str1.find('and', 1, 28))  # 在下标1-28 查找and ，如果找到就返回第一个and的下标
# print(str1.find('ddd'))

print(str1.index('and'))
# print(str1.index('and', 1, 28))
# print(str1.index('dddd'))

# print(str1.count('and', 1, 28))  # 在整个字符串中查找and 子串的个数
#
# print(str1.count('ddddd'))  # 查找子串是ddddd，找不到的时候返回的是0

print(str1.rfind('and'))
print(str1.rindex('and'))
