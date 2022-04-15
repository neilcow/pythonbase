try:
    f = open('test.txt', 'r')
except Exception as result:
    f = open('test.txt', 'w')
else:
    print('我是没有异常的时候输出')
finally:
    f.close()
    print('我是不管是否有异常都要输出')

# 输出 我是不管是否有异常都要输出