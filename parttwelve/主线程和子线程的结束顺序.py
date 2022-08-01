import time
import threading


def work():
    for i in range(3):
        print("工作.....")
        time.sleep(0.2)


if __name__ == '__main__':
    sub_thread = threading.Thread(target=work)
    sub_thread.setDaemon(True)
    sub_thread.start()

    time.sleep(1)
    print("主线程停止工作.....")



