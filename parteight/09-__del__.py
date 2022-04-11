class Washer():
    def __init__(self):
        self.width = 10
        self.height = 20
        print(f'洗衣机宽度是{self.width},洗衣机高度是{self.height}')

    def __del__(self):
        print('对象被删除')
        

haier1 = Washer()
