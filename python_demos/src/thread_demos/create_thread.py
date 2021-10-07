""" create thread demo """

import threading
import time


def do_it() -> None:
    """ do it """

    # print("".join([
    #     "entering thread id: ",
    #     str(threading.get_ident()),
    #     ", thread name: ",
    #     threading.current_thread().name
    # ]))

    # y = 1
    # for x in range(50000000):
    #     y = x

    # while True:
    #     ...

    # print(y)

    time.sleep(1)

    print("".join([
        "exiting thread id: ",
        str(threading.get_ident()),
        ", thread name: ",
        threading.current_thread().name
    ]))

thread1 = threading.Thread(target=do_it, name="thread1")
thread1.start()

thread2 = threading.Thread(target=do_it, name="thread2")
thread2.start()

print("".join([
    "thread id: ",
    str(threading.get_ident()),
    ", thread name: ",
    threading.current_thread().name
]))
print("made it here")

