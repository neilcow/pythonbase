import os

flag = 1
# os.rename('ccc', 'aaa')
file_name = os.listdir('aaa')
print(file_name)
for i in file_name:
    if flag == 1:
        new_name = 'python_' + i
    elif flag == 2:
        num = len('python_')
        new_name = i[num:]
    os.rename(i, new_name)
