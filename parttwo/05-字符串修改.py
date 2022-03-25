# 1、replace()
str1 = 'hello world and python and python and python'
# 替换次数超出子串的次数，会替换所有子串
# new_str = str1.replace('and', 'he', 10)
# print(new_str)
# print(str1)
# 2、split()   分割字符会被丢失，num是被分割是部分，最后返回的数据个数为num+1
print(str1.split('and', 2))
# 输出 ['hello world ', ' python ', ' python ', ' python']
# 输出 ['hello world ', ' python ', ' python and python']

# 3、jion()
mylist = ['aaaa', 'bbbb', 'cccc']
new_str = '...'.join(mylist)
print(new_str)
# 输出 aaaa...bbbb...cccc