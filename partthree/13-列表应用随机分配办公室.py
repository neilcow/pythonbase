"""
思路 ，准备数据 老师8个，教师4个
分配老师到办公室，取到每个老师放到办公室列表，遍历老师列表
验证数据
"""
import random
teachers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
offices = [[], [], [], []]
for teacher in teachers:
    num = random.randint(0, 3)
    offices[num].append(teacher)
# print(offices)

i = 1
for office in offices:
    print(f'{i}办公室人数{len(office)},老师分别是：')
    for teach in office:
        print(teach)
    i += 1
