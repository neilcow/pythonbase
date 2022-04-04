a = 100
print(a)


def test1():
    print(a)


def test2():
    # a = 200  # 修改的a是局部变量，因为再函数调用后又打印了一次a，发现还是100，说明全局变量没有变
    # 使用关键字声明这个变量是全局的
    global a
    a =200
    print(a)


test1()
test2()
print(a)
# 输出
# 100
# 100
# 200
# 200
