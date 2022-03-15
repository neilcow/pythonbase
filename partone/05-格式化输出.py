"""
1、准备数据
2、格式化输出数据
"""
age = 18
name = 'tester'
weight = 60.4
stu_id = 1
stu_id2 = 12234

# 1、今年的年龄是x岁
print('今年的年龄是%d岁' % age)
# 2、我的名字是xxx
print('我的名字是%s' % name)
# 3、我的体重是xx公斤
print('我的体重是%.2f公斤' % weight)
# 4、我的学号是xx
print('我的学号是% d' % stu_id)
# 4.1我的学号是001
print('我的学号是%03d' % stu_id)
print('我的学号是%03d' % stu_id2)
# 5、我名字是xxx,我的年龄是xxx
print('我名字是%s,我的年龄是%d' % (name, age))
# 5.1 我的名字是xxx，我明年的年龄是xxxx
print('我的名字是%s，我明年的年龄是%d' % (name, age+1))
# 我的名字是xxx， 我的年龄是xxx， 我的学号是xxx， 我的体重是xxxx
print('我的名字是%s， 我的年龄是%d， 我的学号是%03d， 我的体重是%.2f' % (name, age, stu_id, weight))
