# 1、无参数
fn1 = lambda: 100
res = fn1()
print(res)
# 2、一个参数
fn2 = lambda a: a
res2 = fn2('hell python')
print(res2)
# 3、 默认参数
fn3 = lambda a, b, c=100: a + b + c
res3 = fn3(10, 20)
print(res3)
# 4、可变参数 *args
fn4 = lambda *args: args
res4 = fn4(10, 20, 40)
print(res4)
# 5、可变参数 **kwargs
fn5 = lambda **kwargs: kwargs
res5 = fn5(name='test', age=20)
print(res5)
# 输出{'name': 'test', 'age': 20}