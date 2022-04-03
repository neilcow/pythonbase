def buy():
    return '烟'


goods = buy()
print(goods)


def sum_num(a, b):
    """
    求和函数sum_num
    :param a:参数1
    :param b:参数2
    :return:返回值
    """
    return a + b


result = sum_num(3, 4)
print(result)


help(sum_num)

# 输出
# sum_num(a, b)
#     求和函数sum_num
#     :param a:参数1
#     :param b:参数2
#     :return:返回值
