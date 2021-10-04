from concurrent import futures
import logging
import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor
import numpy as np

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)


"""
https://www.youtube.com/watch?v=YSjIisKdgD0
event = threading.Event()
event.set()     -> event.is_set() = True
event.clear()   -> event.is_set() = False
event.wait()    -> until event.is_set() = True
event.is_set()
"""


def flag(name):
    cnt = 0
    for i in range(1, 4):
        time.sleep(1)
        cnt = cnt + 1
        logger.info(
            f"count[{cnt}], name[{name},{threading.current_thread().name}], is_set[{event.is_set()}]")
    event.set()
    for i in range(1, 4):
        time.sleep(1)
        cnt = cnt + 1
        logger.info(
            f"count[{cnt}], name[{name},{threading.current_thread().name}], is_set[{event.is_set()}]")
    event.clear()
    for i in range(1, 4):
        time.sleep(1)
        cnt = cnt + 1
        logger.info(
            f"count[{cnt}], name[{name},{threading.current_thread().name}], is_set[{event.is_set()}]")
    event.set()
    for i in range(1, 4):
        time.sleep(1)
        cnt = cnt + 1
        logger.info(
            f"count[{cnt}], name[{name},{threading.current_thread().name}], is_set[{event.is_set()}]")
    event.clear()
    for i in range(1, 4):
        time.sleep(1)
        cnt = cnt + 1
        logger.info(
            f"count[{cnt}], name[{name},{threading.current_thread().name}], is_set[{event.is_set()}]")


def event_loop(name):
    #event.wait()
    #while event.is_set():

    while True:
        event.wait()
        if event.is_set():
            logger.info(
                f"name[{name},{threading.current_thread().name}], Some Operation")
        time.sleep(0.1)


if __name__ == "__main__":
    # Logging format 설정
    # 클래스 인스턴스화
    # With Context 시작
    event = threading.Event()

    start_time = time.time()
    # ------------------------------ Race condition ------------------------------ #

    eventstub_task = threading.Thread(target=flag, args=("flag_thread",))
    background_task = threading.Thread(
        target=event_loop, args=("event_thraed",))
    background_task.daemon = True
    eventstub_task.start()
    background_task.start()

    eventstub_task.join()

    print(f"{time.time()-start_time} sec")
