def user_info(*args):
    print(args)


user_info('test1', 20)
user_info('test2')
user_info()
# 输出
# ('test1', 20)
# ('test2',)
# ()
