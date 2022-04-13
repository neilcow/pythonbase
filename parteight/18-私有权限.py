class Master(object):
    def __init__(self):
        self.gongfu = '摊煎饼'

    def make_cake(self):
        print(f'师傅教的摊煎饼{self.gongfu}')


class School(Master):
    def __init__(self):
        self.gongfu = '学校学习摊煎饼'

    def make_cake(self):
        print(f'学校学习的摊煎饼{self.gongfu}')
        super(School, self).__init__()
        super(School, self).make_cake()


class Apprentice(School):
    def __init__(self):
        self.gongfu = '这是徒弟自创的摊煎饼技术'
        self.__monkey = 10000

    # 注意 要调用一次 子类的初始化方法，保证每次是子类的初始化属性，并且不用传self
    def make_cake(self):
        self.__init__()
        print(f'这是徒弟自创的做煎饼方法{self.gongfu}')

    # 需要调用父类的初始化方法，并且都要传self，否则找不到是哪个对象调用的
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    # 需要调用父类的初始化方法，并且都要传self，否则找不到是哪个对象调用的
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

    def make_old_cake(self):
        super(Apprentice, self).__init__()
        super(Apprentice, self).make_cake()

    def make_new_cake(self):
        super().__init__()
        super().make_cake()

    def __print_info(self):
        self.__init__()
        print('我是私有方法')


pancake = Apprentice()
# print(pancake.gongfu)
print(pancake.gongfu)
print(pancake.monkey)
pancake.print_info()

# 输出
# AttributeError: 'Apprentice' object has no attribute 'monkey'

