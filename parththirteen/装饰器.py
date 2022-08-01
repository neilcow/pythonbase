
def decorator(func):
    def inner():
        print("已添加登录验证")
        func()
    return inner


# 装饰器语法糖写法， 装饰器函数的名字
@decorator
def comment():
    print("发表评论")


# comment = decorator(comment)
comment()