# continue 当条件成立，退出当前一次循环，继而执行下一次循环
# 注意 使用continue的时候，需要在continue之前改变i的值
i = 1
while i <= 5:
    if i == 3:
        print(f'第3个不执行')
        i += 1
        continue
    print(f'我是第{i}个')
    i += 1
