# 打印图形
def print_line():
    print('-' * 20)


def print_lines(num):
    for i in range(num):
        print_line()


print_lines(4)


def sum_num(a, b, c):
    return a + b + c


sum_res = sum_num(10, 20, 30)
print(sum_res)


def ave_num(a, b, c):
    ave = sum_num(a, b, c) / 3
    return ave


ave_res = ave_num(22, 33, 44)
print(ave_res)