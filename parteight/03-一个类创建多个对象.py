class Washer():
    def wash(self):
        print(self)
        print('洗衣服')


haier1 = Washer()
haier1.wash()


haier2 = Washer()
haier2.wash()
# 输出
# <__main__.Washer object at 0x0000000001E43EC8>
# 洗衣服
# <__main__.Washer object at 0x0000000001E43F48>
# 洗衣服