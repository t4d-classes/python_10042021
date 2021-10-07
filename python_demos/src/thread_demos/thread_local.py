""" thread local demo """

import threading
import time

my_data = threading.local()

def do_it2() -> None:
    """ do it 2 """

    print("doIt2: thread id: " + str(threading.get_ident()) + ", my data: " + my_data.x)

def do_it() -> None:
    """ do it """

    time.sleep(1)

    my_data.x = "x: " + threading.current_thread().name

    print("".join([
        "thread id: ",
        str(threading.get_ident()),
        ", thread name: ",
        threading.current_thread().name
    ]))

    do_it2()

thread1 = threading.Thread(target=do_it, name="thread1")
thread1.start()

thread2 = threading.Thread(target=do_it, name="thread2")
thread2.start()
