import time

try:
    f = open('test.txt')
    try:
        while True:
            con = f.readline()
            if len(con) == 0:
                break
            time.sleep(3)
            print(con)
    except:
        print('程序被意外终止')
except:
    print('该文件不存在')

