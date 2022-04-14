class Dog(object):

    @staticmethod
    def get_tooth():
        print('这是一个静态方法')


dahuang = Dog()
dahuang.get_tooth()
Dog.get_tooth()
# 输出
# 这是一个静态方法
# 这是一个静态方法
