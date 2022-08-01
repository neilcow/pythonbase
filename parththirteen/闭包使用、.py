

def config_name(name):

    def inner(msg):
        print(name + ":" + msg)

    return inner


tom = config_name("tom")
jerry = config_name("jerry")

# 执行tom相当于 执行的是inner
tom("你过来啊")
jerry("过来干什么")
