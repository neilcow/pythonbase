def make_p(func):
    print("make_p装饰器执行了")

    def inner():
        result = "<p>" + func() + "</p>"
        return result
    return inner


def make_div(func):
    print("make_div装饰器执行了")

    def inner():
        result = "<div>" + func() + "</div>"
        return result
    return inner


@make_div
@make_p
def content():
    return "多个装饰器的使用"


test = content()
print(test)