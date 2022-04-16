class ShortInputExcept(Exception):
    def __init__(self, length, min_length):
        self.length = length
        self.min_length = min_length

    def __str__(self):
        return f'您的密码是{self.length}位数，最小密码长度是{self.min_length}位数'


def test():
    try:
        num = input('请输入密码')
        if len(num) < 3:
            raise ShortInputExcept(len(num), 3)
    except Exception as result:
        print(result)
    else:
        print('密码正确')


test()