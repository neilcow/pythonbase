def testA(a, b):
    print(a + b)


# __name__ 是系统变量，是模块的标识符，值有两种情况，如果是自身模块，值是__main__，否则是模块的名字
if __name__ == '__main__':
    testA(1, 1)