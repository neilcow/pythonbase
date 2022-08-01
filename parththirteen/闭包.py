

def func_out():
    # 外部变量
    num1 = 10

    def func_inner(num2):
        result = num1 + num2
        print('结果是：', result)

    return func_inner


func_new = func_out()
func_new(11)