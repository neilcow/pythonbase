class SweetPotato():
    def __init__(self):
        self.cookie_time = 0
        self.cookie_static = '生的'
        self.cookie_condiments = []

    def __str__(self):
        return f'这个地瓜烤的时间{self.cookie_time}, 这个地瓜的状态{self.cookie_static}, 给地瓜添加调料' \
               f'{self.cookie_condiments}'

    def cook(self, time):
        self.cookie_time += time
        if 0 < self.cookie_time < 3:
            self.cookie_static = '生的'
        elif 3 <= self.cookie_time < 5:
            self.cookie_static = '半生不熟'
        elif 5 <= self.cookie_time < 8:
            self.cookie_static = '熟的'
        elif self.cookie_time >= 8:
            self.cookie_static = '烤糊了'

    def add_condiments(self, condiment):
        self.cookie_condiments.append(condiment)


digua1 = SweetPotato()
print(digua1)
digua1 = SweetPotato()
digua1.cook(9)
print(digua1)
digua1.add_condiments('辣椒')
print(digua1)
digua1.add_condiments('盐')
print(digua1)
#输出
# 这个地瓜烤的时间0, 这个地瓜的状态生的, 给地瓜添加调料[]
# 这个地瓜烤的时间9, 这个地瓜的状态烤糊了, 给地瓜添加调料[]
# 这个地瓜烤的时间9, 这个地瓜的状态烤糊了, 给地瓜添加调料['辣椒']
# 这个地瓜烤的时间9, 这个地瓜的状态烤糊了, 给地瓜添加调料['辣椒', '盐']