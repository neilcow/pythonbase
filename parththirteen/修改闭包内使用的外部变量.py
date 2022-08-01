
def func_out():
    num1 = 10

    def func_inner():

        nonlocal num1
        num1 = 20
        result = num1 + 10
        print(result)

    return func_inner


new_func = func_out()
new_func()