""" thread queues demo """

import threading
import queue
import time
from random import randint

nums: queue.Queue[int] = queue.Queue()
double_nums: queue.Queue[int] = queue.Queue()

generate_nums_done = threading.Event()
double_nums_done = threading.Event()


def generate_nums(
    number_of_nums: int,
    queue_nums: queue.Queue[int],
    done: threading.Event) -> None:
    """ generate nums """

    for _ in range(number_of_nums):
        num = randint(1, 11)
        print("generate number: " + str(num))
        queue_nums.put(num)

    done.set()

def double_the_nums(
    queue_nums: queue.Queue[int],
    queue_double_nums: queue.Queue[int],
    nums_done: threading.Event,
    done: threading.Event) -> None:
    """ double the nums """

    one_last_time = False

    while True:
        try:
            num = queue_nums.get(timeout=0.1)
            print("get num: " + str(num))
            double_num = num * 2
            queue_double_nums.put(double_num)
            print("calc double num: " + str(num) + " => " + str(double_num))
        except queue.Empty:
            if nums_done.is_set():
                if one_last_time:
                    done.set()
                    break
                else:
                    one_last_time = True
                    continue


def output_nums(
    queue_double_nums: queue.Queue[int],
    p_double_nums_done: threading.Event) -> None:
    """ output nums """

    one_last_time = False

    while True:
        try:
            num = queue_double_nums.get(timeout=0.1)
            print("output nums: " + str(num))
        except queue.Empty:
            if p_double_nums_done.is_set():
                if one_last_time:
                    break
                else:
                    one_last_time = True
                    continue

generate_nums_thread = threading.Thread(
    target=generate_nums,
    args=(10, nums, generate_nums_done))

double_the_nums_thread = threading.Thread(
    target=double_the_nums,
    args=(nums, double_nums, generate_nums_done, double_nums_done))

output_nums_thread = threading.Thread(
    target=output_nums,
    args=(double_nums, double_nums_done))

generate_nums_thread.start()
double_the_nums_thread.start()
output_nums_thread.start()

generate_nums_thread.join()
double_the_nums_thread.join()
output_nums_thread.join()
