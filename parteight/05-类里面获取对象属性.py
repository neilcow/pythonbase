class Washer():
    def wash(self):
        print(f'洗衣机宽度是{self.width}')
        print(f'洗衣机高度是{self.height}')


haier1 = Washer()
haier1.width = 100
haier1.height = 200
haier1.wash()