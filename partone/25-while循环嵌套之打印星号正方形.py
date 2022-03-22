# print 默认换行符是\n ，可以重新设置换行符
# 同时加上一个print() 利用空的print默认结束换行
j = 0
while j < 5:
    i = 0
    while i < 5:
        print('*', end='')
        i += 1
    print()
    j += 1

