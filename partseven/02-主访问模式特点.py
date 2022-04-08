"""
1、访问模式对文件的影响
2、访问模式对write()的影响
3、访问模式是否可以省略
"""
# r,如果文件不存在，就会报错,不支持写入操作，只支持只读
f = open('test.txt', 'r')
# f.write('aa')
f.close()

# w 如果文件不存在，就会生成一个新的文件，写入的内容会覆盖以前的内容
f = open('1.txt', 'w')
f.write('bbbb')
f.close()

# a 如果文件不存在，就会生成一个新的文件，写入的内容会追加到原有内容后面
f = open('2.txt', 'a')
f.write('dddd')
f.close()

# 访问模式参数是否可以省略,可以省略，省略表示访问模式为 r
f = open('1.txt')
f.close()