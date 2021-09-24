import threading
import time
# ----------------------------------- ex 1 ----------------------------------- #
# def  func(sec):
#     print('ran')
#     time.sleep(sec)
#     print('done')
#     time.sleep(1)
#     print('now done')
# x = threading.Thread(target=func, args=(1,)) # , needed

# x.start()

# print(threading.active_count())

# time.sleep(3)
# print('out done')

# ----------------------------------- ex 2 ----------------------------------- #
# def count(n):
#     for i in range(1,n+1):
#         print(i)
#         time.sleep(0.1)

# for _ in range(2):
#     x = threading.Thread(target=count, args=(10,))
#     x.start()

# print('done')

# ----------------------------------- ex 3 ----------------------------------- #
# def count(n):
#     for i in range(1,n+1):
#         print(i)
#         time.sleep(0.1)

# def count2(n):
#     for i in range(1,n+1):
#         print(i)
#         time.sleep(0.2)


# x = threading.Thread(target=count, args=(10,))
# x.start()
# y = threading.Thread(target=count2, args=(10,))
# y.start()

# print('done')


# ---------------------------------------------------------------------------- #
#                            thread synchronization                            #
# ---------------------------------------------------------------------------- #
ls = []
def count(n):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(0.1)

def count2(n):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(0.2)
x = threading.Thread(target=count, args=(10,))
x.start()
y = threading.Thread(target=count2, args=(10,))
y.start()

x.join() #no dot move this line of code until stops run
y.join()


print(ls)
