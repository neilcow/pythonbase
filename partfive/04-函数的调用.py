def test1():
    print('我是test1的方法')


def test2():
    print('test2 开始')
    test1()
    print('test2 结束')


test2()

# 输出
# test2 开始
# 我是test1的方法
# test2 结束