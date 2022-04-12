class Master(object):
    def __init__(self):
        self.gongfu = '摊煎饼'

    def make_cake(self):
        print(f'师傅教的摊煎饼{self.gongfu}')


class School(object):
    def __init__(self):
        self.gongfu = '学校学习摊煎饼'

    def make_cake(self):
        print(f'学校学习的摊煎饼{self.gongfu}')


class Apprentice(School, Master):
    def __init__(self):
        self.gongfu = '这是徒弟自创的摊煎饼技术'

    # 注意 要调用一次 子类的初始化方法，保证每次是子类的初始化属性，并且不用传self
    def make_cake(self):
        self.__init__()
        print(f'这是徒弟自创的做煎饼方法{self.gongfu}')

    # 需要调用父类的初始化方法，并且都要传self，否则找不到是哪个对象调用的
    def make_Master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    # 需要调用父类的初始化方法，并且都要传self，否则找不到是哪个对象调用的
    def make_School_cake(self):
        School.__init__(self)
        School.make_cake(self)


pancake = Apprentice()
# print(pancake.gongfu)
pancake.make_cake()
pancake.make_Master_cake()
pancake.make_School_cake()
pancake.make_cake()
