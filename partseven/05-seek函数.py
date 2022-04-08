"""
语法：文件对象.seek(偏移量，起始位置) 0 开头 1 当前 2 结尾
目标：
   1、r 改变文件指针位置，改变读取数据开始位置或把文件指针放结尾（无法读取数据）
   2、a 改变文件指针位置，做到可以读取数据
"""
# f = open('test.txt', 'r')
# # f.seek(3, 0)
# f.seek(0, 2)
# con = f.read()
# print(con)
# 输出
# aa
# bbbbb
# ccccc
# ddddd
# eeeee

# 输出 空

f = open('test.txt', 'a+')
f.seek(0, 0)
con = f.read()
print(con)
# 输出
# aaaaa
# bbbbb
# ccccc
# ddddd
# eeeee
