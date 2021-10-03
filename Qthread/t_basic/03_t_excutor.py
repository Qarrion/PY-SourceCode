from concurrent import futures
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


#* https://medium.com/humanscape-tech/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%98-future-%ED%81%B4%EB%9E%98%EC%8A%A4-8b6bc15bd6af
def mysum_thread_executor():
    executor = ThreadPoolExecutor(max_workers=3)

    task1 = executor.submit(mysum,(500))
    task2 = executor.submit(mysum,(500))
    task3 = executor.submit(mysum,(500))

    print(task1.result())
    print(task2.result())
    print(task3.result())

def mysum_thread_executor_with():
    #! excutor를 사용할 경우 결과를 쉽게 받을 수 있으며, 순서 와 관계없이 사용 가능
    with ThreadPoolExecutor(max_workers=3) as executor:
        task1 = executor.submit(mysum,(500))
        task2 = executor.submit(mysum,(500))
        task3 = executor.submit(mysum,(500))
    print("all tasks done")
    print(task1.result())
    print(task2.result())
    print(task3.result())

def mysum_thread_executor_with_map():
    # Executor.map()의 경우, 호출한 순서 그대로 결과를 반환합니다
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = executor.map(mysum,[500,500,500])
    print(list(tasks))

def mysum_thread_executor_with_ascompleted():
    # Executor.submit(), Executor.as_completed()를 함께 사용하면, 완료되는 순서대로 결과를 가져오게 됩니다
    funs = [mysum, mysum, mysum]
    tasks = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        for fun in funs:
            future = executor.submit(fun, 500)
            tasks.append(future)
        result = []
        for task in futures.as_completed(tasks):
            res = task.result()
            result.append(res)
    print(result)



if __name__ == "__main__":
    start_time = time.time()
# -------------------------------- mysum_sync -------------------------------- #
    # mysum_sync()
    # 3.119568347930908 sec
# --------------------------- mysum_thread_executor -------------------------- #
    # mysum_thread_executor()
    # 3.093327522277832 sec
# ------------------------ mysum_thread_executor_with ------------------------ #
    # mysum_thread_executor_with()
    # 3.543931484222412 sec
# ---------------------- mysum_thread_executor_with_map ---------------------- #
    # mysum_thread_executor_with_map()
    # 3.057272434234619 sec
# ------------------ mysum_thread_executor_with_ascompleted ------------------ #
    # mysum_thread_executor_with_ascompleted()
    # 3.025169849395752 sec
    duration = time.time() - start_time
    print(f"{duration} sec")



