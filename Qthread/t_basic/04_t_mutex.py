from concurrent import futures
import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)


# * https://iredays.tistory.com/125
class data_store_thread:
    # 공유 변수(value)
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()   #* LOCK

    def update_01(self, name):
        logger.info(f"name [{name},{threading.current_thread().name}] starting value{self.value}")
        v = self.value
        v = v+1
        time.sleep(0.1)
        self.value = v
        logger.info(f"name [{name},{threading.current_thread().name}] finishing value{v}")

    def update_02(self, name):
        logger.info(f"name [{name},{threading.current_thread().name}] starting value{self.value}")
        logger.info(f"name [{name},{threading.current_thread().name}] LOCK")
        self._lock.acquire()
        v = self.value
        v = v+1
        time.sleep(0.1)
        self.value = v
        logger.info(f"name [{name},{threading.current_thread().name}] finishing value{v}")
        self._lock.release()
        logger.info(f"name [{name},{threading.current_thread().name}] UNLOCK")

    # 변수 업데이트 함수

if __name__ == "__main__":
    # Logging format 설정
    # 클래스 인스턴스화

    store = data_store_thread()

    logging.info("Testing update. Starting value is %d.", store.value)
    # With Context 시작
    start_time =  time.time()
    # ------------------------------ Race condition ------------------------------ #
    # with ThreadPoolExecutor(max_workers=3) as executor:
    #     for n in ['t1', 't2', 't3']:
    #         executor.submit(store.update_01, n)

    # ------------------------------ Mutex solution ------------------------------ #
    with ThreadPoolExecutor(max_workers=3) as executor:
        for n in ['t1', 't2', 't3']:
            executor.submit(store.update_02, n)

    logging.info("Testing update. Ending value is %d.", store.value)
    print(f"{time.time()-start_time} sec")
