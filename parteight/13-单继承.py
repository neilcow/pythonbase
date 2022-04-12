class Master(object):
    def __init__(self):
        self.gongfu = '摊煎饼'

    def make_cookie(self):
        print(f'做煎饼{self.gongfu}')


class Apprentice(Master):
    pass


pancake = Apprentice()
print(pancake.gongfu)
pancake.make_cookie()