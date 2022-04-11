class Washer():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print(f'洗衣机宽度是{self.width},高度是{self.height}')

    def __str__(self):
        return '洗衣机的说明书'


haier1 = Washer(10, 20)
print(haier1)
