# print 默认换行符是\n ，可以重新设置换行符
# 同时加上一个print() 利用空的print默认结束换行
"""
思路 是先打印一个 星
    打印一行五个星
    循环打印五行，打出长方形
    打印出三角形
"""
k = 1
j = 0
while j < 5:
    i = 0
    while i < k:
        print('*', end='')
        i += 1
    print()
    j += 1
    k += 1
