# 三以内数字累计和计算
def sum_num(num):
    if num == 1:
        return 1
    return num + sum_num(num-1)


res = sum_num(3)
print(res)