import os
# 1、rename()，重命名
# os.rename('test[备份文件].txt', '11.txt')

# 2、remove(),删除文件
# os.remove('11.txt')
# 3、mkdir创建文件夹
# os.mkdir('aaa')
# os.rmdir('aaa')
# print(os.getcwd())

# os.mkdir('aaa')
# os.chdir('aaa')
# os.mkdir('bbb')

# print(os.listdir('aaa'))
# 输出 ['01-体验文件操作.py', '02-主访问模式特点.py', '03-读取函数之read().py', '04-访问模式特点02.py']

os.rename('aaa', 'ccc')