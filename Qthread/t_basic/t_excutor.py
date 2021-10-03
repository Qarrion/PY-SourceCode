import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
logger = logging.getLogger()
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)



def mysum(number):
    logger.info(f"name [{threading.current_thread().name}] starting ")
    ret = 0
    for i in range(number):
        number2 = i*i
        for j in range(number2):
            ret += j
    logger.info(f"name [{threading.current_thread().name}] finishing ")
    return(ret)

def mysum_sync():
    print(mysum(500))
    print(mysum(500))
    print(mysum(500))

def mysum_thread():
    executor = ThreadPoolExecutor(max_workers=2)

    task1 = executor.submit(mysum,(500))
    task2 = executor.submit(mysum,(500))
    task3 = executor.submit(mysum,(500))

    print(task1.result())
    print(task2.result())
    print(task3.result())


if __name__ == "__main__":
    start_time = time.time()
# ----------------------------------- sync ----------------------------------- #
    mysum_sync()
    # 3.1195616722106934 sec
# ---------------------------------- thread ---------------------------------- #
    # mysum_thread()
    # 3.0265893936157227 sec


    duration = time.time() - start_time
    print(f"{duration} sec")



