import threading
import datetime, time


class mythread1(threading.Thread):
    def run(self) -> None:
        for i in range(10):
            print(f"thread1 print {i}")
            time.sleep(0.2)

class mythread2(threading.Thread):
    def run(self) -> None:
        for i in range(10):
            print(f"thread2 print {i}")
            time.sleep(0.3)

th1 = mythread1()
th2 = mythread2()
th2.daemon=True
th1.start()
th2.start()