class Washer():
    def __init__(self):
        self.width = 200
        self.height = 300

    def print_info(self):
        print(f'洗衣机宽度是{self.width}')
        print(f'洗衣机高度是{self.height}')


haier1 = Washer()
haier1.print_info()

