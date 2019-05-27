'''
两个进程输出的Ping和Pong加起来一共10个
'''
from multiprocessing import Process, Queue
from time import sleep

# counter = 0


def sub_task(string, p):
    # global counter
    while True:
        if p.full():
            return
        print(string, end='', flush=True)
        # counter += 1
        p.put(string)
        sleep(0.01)


def main():
    # p = Queue(maxsize=10)
    p = Queue(maxsize=9)
    Process(target=sub_task, args=('Ping', p,)).start()
    Process(target=sub_task, args=('Pong', p,)).start()

    p.get()


if __name__ == "__main__":
    main()
