def user_info(**kwargs):
    print(kwargs)


user_info(name='test1', age=23, gender='男')
# 输出{'name': 'test1', 'age': 23, 'gender': '男'}