class Dog(object):
    tooth = 10


Dog.tooth = 222
print(Dog.tooth)
dahuagn = Dog()
xiaohei = Dog()
dahuagn.tooth = 3333
print(Dog.tooth)
print(dahuagn.tooth)
# 输出
# 222
# 222
# 3333