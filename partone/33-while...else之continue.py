i = 0
while i < 5:
    if i == 2:
        i += 1
        continue
    print(f'我是while循环{i}')
    i += 1
else:
    print('我是循环执行后才执行的')
