f = open('test.txt', 'r')
print(f.read())
f.close()
# 输出
# aaaaa
# bbbbb
# ccccc
# ddddd
# eeeee

f = open('test.txt', 'r')
print(f.readlines())
f.close()
# 输出['aaaaa\n', 'bbbbb\n', 'ccccc\n', 'ddddd\n', 'eeeee\n']


f = open('test.txt', 'r')
print(f.readline())
print(f.readline())
f.close()
# 输出 aaaaa
# bbbbb