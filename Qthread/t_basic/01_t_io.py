import logging
import threading
import time



formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
logger = logging.getLogger()
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)



def mysleep(number : int):
    logger.info("Starting Sleep")
    time.sleep(number)
    logger.info("Finishing Sleep")



def mysleep_sync():
    mysleep(5)
    mysleep(5)
    mysleep(5)

def mysleep_thread():
    x=threading.Thread(target=mysleep, args=(5,))
    y=threading.Thread(target=mysleep, args=(5,))
    z=threading.Thread(target=mysleep, args=(5,))
    x.start()
    y.start()
    z.start()
    x.join()
    y.join()
    z.join()

if __name__ == "__main__":
    start_time = time.time()
# ----------------------------------- sync ----------------------------------- #
    mysleep_sync()
    # 15.029629945755005 sec
# ---------------------------------- thread ---------------------------------- #
    # mysleep_thread()
    # 5.003507375717163 sec


    duration = time.time() - start_time
    print(f"{duration} sec")



