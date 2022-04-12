class A(object):
    def __init__(self):
        self.num = 1

    def print_info(self):
        print(self.num)


class B(A):
    pass


b = B()
b.print_info()
# 输出 1