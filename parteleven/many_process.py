import time
import multiprocessing


def sing(num):
    for i in range(num):
        print("唱歌....")
        time.sleep(0.5)


def dance(num):
    for i in range(num):
        print("跳舞.....")
        time.sleep(0.5)


if __name__ == '__main__':
    sing_process = multiprocessing.Process(target=sing, args=(3,))
    dance_process = multiprocessing.Process(target=dance, kwargs={"num": 4})

    sing_process.start()
    dance_process.start()

