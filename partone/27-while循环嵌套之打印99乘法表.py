# print 默认换行符是\n ，可以重新设置换行符
# 同时加上一个print() 利用空的print默认结束换行
"""
思路 打印一个乘法表达式
    每一行打印 行号个数的表达式
    循环打印多行
    先打印出一个 表达式，然后长方形，三角形，修改表达式
"""
k = 0
n = 1
while k < 9:
    m = 0
    while m < n:
        print(f'{m+1} * {n} = {(m+1) * n}', end='\t')
        m += 1
    print()
    k += 1
    n += 1
