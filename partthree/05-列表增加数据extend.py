name_list = ['test1', 'test2', 'test3']
# name_list.extend('test4')
print(name_list)
# 输出 ['test1', 'test2', 'test3', 't', 'e', 's', 't', '4']
name_list.extend(['test4', 'test5'])
print(name_list)
# 输出 ['test1', 'test2', 'test3', 'test4', 'test5']
