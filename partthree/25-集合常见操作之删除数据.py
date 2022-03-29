# 删除数据
# remove
s1 = {10, 20}
s1.remove(10)
print(s1)
# 输出 {20}
# s1.remove(45)
# 输出 报错

# discard()
s2 = {30, 40}
s2.discard(30)
print(s2)
s2.discard(454)
print(s2)

#pop()
s3 = {50, 60, 70, 80}
s3.pop()
print(s3)
# 输出 {50, 60, 70}