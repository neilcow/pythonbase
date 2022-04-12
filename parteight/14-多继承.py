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
    pass


pancake = Apprentice()
print(pancake.gongfu)
pancake.make_cookie()
# 输出
# 学校学习摊煎饼
# 学校学习的摊煎饼学校学习摊煎饼
