class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机宽度{self.width}')
        print(f'洗衣机高度{self.height}')


haier1 = Washer(100, 200)
haier1.print_info()

haier2 = Washer(300, 400)
haier2.print_info()
# 输出洗
# 衣机宽度100
# 洗衣机高度200
# 洗衣机宽度300
# 洗衣机高度400
