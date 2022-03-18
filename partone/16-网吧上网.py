"""
1、输入一个年龄
2、判断年龄
3、输出结果
需要注意input返回的类型是str
"""

age = int(input('请输入您的年龄'))
if age >= 18:
    print(f'您的年龄是{age}，可以上网')
else:
    print(f'您的年龄不满18周岁，不能上网')
