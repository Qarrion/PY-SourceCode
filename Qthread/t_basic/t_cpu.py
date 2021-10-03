import logging
import threading
import time



formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
logger = logging.getLogger()
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)



def mysum(number : int):
    ret = 0
    for i in range(number):
        number2 = i*i
        for j in range(number2):
            ret += j
    print(ret)

def mysum_sync():
    mysum(500)
    mysum(500)
    mysum(500)

def mysum_thread():
    x=threading.Thread(target=mysum, args=(500,))
    y=threading.Thread(target=mysum, args=(500,))
    z=threading.Thread(target=mysum, args=(500,))
    x.start()
    y.start()
    z.start()
    x.join()
    y.join()
    z.join()

if __name__ == "__main__":
    start_time = time.time()
# ----------------------------------- sync ----------------------------------- #
    #mysum_sync()
    # 2.963186740875244 sec
# ---------------------------------- thread ---------------------------------- #
    mysum_thread()
    # 2.9794647693634033 sec


    duration = time.time() - start_time
    print(f"{duration} sec")



