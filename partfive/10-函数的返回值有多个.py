def nums():
    # return 1, 3
    # return (1, 3)
    # return [1, 3]
    return {'name':'test', 'age':23}


res = nums()
print(res)
# 输出(1, 3)
# 返回的是一个元组
# 输出[1, 3]
# 当返回的多个数据是 元组，返回的也是元组，当多个数据是列表，返回的还是列表
