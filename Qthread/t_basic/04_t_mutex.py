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

    def update_01(self, name):
        v = self.value
        logger.info(f"name [{name},{threading.current_thread().name}] starting value{v}")
        v = v+1
        time.sleep(0.1)
        self.value = v
        logger.info(f"name [{name},{threading.current_thread().name}] finishing value{v}")

    # 변수 업데이트 함수

if __name__ == "__main__":
    # Logging format 설정
    # 클래스 인스턴스화
    store = data_store_thread()

    #! Race condition
    logging.info("Testing update. Starting value is %d.", store.value)
    # With Context 시작
    with ThreadPoolExecutor(max_workers=3) as executor:
        for n in ['t1', 't2', 't3']:
            executor.submit(store.update, n)
    logging.info("Testing update. Ending value is %d.", store.value)

