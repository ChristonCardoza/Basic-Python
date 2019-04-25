import os
import  threading

# MULTITHREADING
# def print_cube(num):
#     print(threading.current_thread().name, os.getpid())
#     print('Cube {}'.format(num * num * num))
# def print_squre(num):
#     print(threading.current_thread().name, os.getpid())
#     print('Squre {}'.format(num * num))
# if __name__ == '__main__':
#     t1 = threading.Thread(target = print_cube, args = (3,), name = 't1')
#     t2 = threading.Thread(target = print_squre, args = (4,), name = 't2')
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()

#THREAD SYNCHRONIZATION
x = 0
def increament():
    global x
    x += 1
def thread_task(lock):
    for _ in range(1000):
        lock.acquire()
        increament()
        lock.release()
def main_task():
    global x
    x = 0
    lock = threading.Lock()
    t1 = threading.Thread(target = thread_task, args = (lock,))
    t2 = threading.Thread(target = thread_task, args = (lock,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
if __name__ == '__main__':
    for _ in range(10):
        main_task()
        print(x)