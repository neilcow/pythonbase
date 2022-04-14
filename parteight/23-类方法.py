class Dog(object):
    __tooth = 100

    @classmethod
    def print_tooth(cls):
        return cls.__tooth


dahuang = Dog()
res = dahuang.print_tooth()
print(res)
