import logging
import threading
import time



formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)



def mysleep(number : int):
    logger.info(f"name[{threading.current_thread().name}] Starting Sleep [{number}] sec")
    time.sleep(number)
    logger.info(f"name[{threading.current_thread().name}] Finishing Sleep [{number}] sec")

def mysleep_blocking():
    mysleep(3)
    mysleep(4)
    mysleep(5)

def mysleep_thread():
    x=threading.Thread(target=mysleep, args=(3,))
    y=threading.Thread(target=mysleep, args=(4,))
    z=threading.Thread(target=mysleep, args=(5,))
    x.start()
    y.start()
    z.start()

def mysleep_thread_join():
    x=threading.Thread(target=mysleep, args=(3,))
    y=threading.Thread(target=mysleep, args=(4,))
    z=threading.Thread(target=mysleep, args=(5,))
    x.start()
    y.start()
    z.start()
    x.join()
    y.join()
    z.join()

def mysleep_thread_join_deamon():
    x=threading.Thread(target=mysleep, args=(3,))
    y=threading.Thread(target=mysleep, args=(4,))
    z=threading.Thread(target=mysleep, args=(5,))
    x.start()
    y.start()
    z.daemon =True
    z.start()
    x.join()
    y.join()
    #z.join()

if __name__ == "__main__":
    start_time = time.time()
    logger.info(f"name[{threading.current_thread().name}] Main start")
# ----------------------------------- sync ----------------------------------- #
    # mysleep_blocking()
    # 15.029629945755005 sec
# ---------------------------------- thread ---------------------------------- #
    # mysleep_thread()
    # 5.003507375717163 sec
# -------------------------------- thread join ------------------------------- #
    # mysleep_thread_join()
    # 5.002264499664307 sec

# ------------------------------- thread daemon ------------------------------ #
    mysleep_thread_join_deamon()

    logger.info(f"name[{threading.current_thread().name}] Main finishing")
    duration = time.time() - start_time
    print(f"{duration} sec")



