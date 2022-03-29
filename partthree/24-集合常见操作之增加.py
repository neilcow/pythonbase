# add()
s1 = {10, 20}
s1.add(10)
s1.add(100)
print(s1)
# 输出 {100, 10, 20}

# update()
s2 = {10, 20}
s2.update([10, 20, 30, 50, 60])
s2.update('sad')
print(s2)
# 输出 {'d', 10, 's', 50, 20, 'a', 60, 30}
