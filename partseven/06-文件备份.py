# 1、接收用户输入目标文件
old_name = input('请输入要备份文件的名字')
print(old_name)
print(type(old_name))
# 2、规划备份文件名
index = old_name.rfind('.')
if index > 0:
    print(index)
    new_name = old_name[:index] + '[备份]' + old_name[index:]
    print(new_name)
    # 输出test[备份].txt
    # 3、备份写入数据
    # 3.1 打开原文件和备份文件
    old_f = open(old_name, 'rb')
    new_f = open(new_name, 'wb')

    # 3.2 原文件读取，备份文件写入
    while True:
        con = old_f.read(1024)
        if len(con) == 0:
            break
        new_f.write(con)
    # 3.3 关闭文件
    old_f.close()
    new_f.close()
else:
    print('输入的文件名错误，请重新输入')