"""
1、判断是否能上车
2、判断是否能坐下
"""
money = 1
seat = 1

if money == 1:
    print('可以上车了')
    if seat == 1:
        print('有空座位，可以坐下')
    else:
        print('没有空座，不能坐')
else:
    print('不可以上车')
