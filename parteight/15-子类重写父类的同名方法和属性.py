class Master(object):
    def __init__(self):
        self.gongfu = '摊煎饼'

    def make_cookie(self):
        print(f'摊煎饼{self.gongfu}')


class School(object):
    def __init__(self):
        self.gongfu = '学校学习摊煎饼'

    def make_cookie(self):
        print(f'学校学习的摊煎饼{self.gongfu}')


class Apprentice(School, Master):
    def __init__(self):
        self.gongfu = '这是徒弟自创的摊煎饼技术'

    def make_cookie(self):
        print(f'这是徒弟自创的做煎饼方法{self.gongfu}')


pancake = Apprentice()
print(pancake.gongfu)
pancake.make_cookie()

print(Apprentice.__mro__)
# 输出 (<class '__main__.Apprentice'>, <class '__main__.School'>, <class '__main__.Master'>, <class 'object'>)

# 输出
# 这是徒弟自创的摊煎饼技术
# 这是徒弟自创的做煎饼方法这是徒弟自创的摊煎饼技术
