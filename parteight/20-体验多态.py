class Dog(object):
    def work(self):
        print('我是父类的狗狗')


class SmallDog(Dog):
    def work(self):
        print('小狗在工作')


class BigDog(Dog):
    def work(self):
        print('大狗在工作')


class Person(object):
    def with_dog(self, dog):
        dog.work()


sd = SmallDog()
bd = BigDog()

p = Person()
p.with_dog(sd)
p.with_dog(bd)
# 输出
# 小狗在工作
# 大狗在工作
