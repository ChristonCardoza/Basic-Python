import os
import multiprocessing

#BASICS
# def print_cube(num):
#     print(os.getpid())
#     print("cube {}".format(num * num * num))

# def print_square(num): 
#     print(os.getpid())
#     print("cube {}".format(num * num))

# p1 = multiprocessing.Process(target = print_cube, args =(3,))
# p2 = multiprocessing.Process(target = print_square, args = (4,))

# if __name__ == '__main__':
#     p1.start()
#     print(p1.is_alive())
#     p2.start()
#     print(p2.is_alive())

#     p1.join()
#     p2.join()



#SHARED MEMORY
# def square_list(mylist, result, squared_sum):
#     for idx,num in enumerate(mylist):
#         result[idx] = num * num 
#     squared_sum.value = sum(result)
#     #print(squared_sum.value)

# if __name__ == '__main__':
#     mylist = [1,2,3,4]
#     result = multiprocessing.Array('i',4)
#     squared_sum = multiprocessing.Value('i')
#     p1 = multiprocessing.Process(target = square_list, args = (mylist, result, squared_sum))
#     p1.start()
#     p1.join()

#     for i in range(len(result)):
#             print(result[i])
#     print(squared_sum.value)



#SERVER PROCESS
# def print_records(records):
#     for record in records:
#         print("Name : {0}\n Scrore : {1}\n".format(record[0],record[1]))
# def insert_records(record,records):
#     records.append(record)
#     print("New Record is Added!\n")

# if __name__ == '__main__':
#     with multiprocessing.Manager() as manager:
#         records = manager.list([('Sam', 10), ('Adam', 9), ('Kevin', 9)])
#         new_record = ('Jeff', 8)
#         p1 = multiprocessing.Process(target = insert_records, args = (new_record, records))
#         p2 = multiprocessing.Process(target = print_records, args = (records,))
#         p1.start()
#         p1.join()
#         p2.start()
#         p2.join()



#QUEUE
# def squared_list(mylist,q):
#     for num in mylist:
#         q.put(num * num)
# def print_list(q):
#     while not q.empty():
#         print(q.get())

# if __name__ == '__main__':
#     q = multiprocessing.Queue()
#     p1 = multiprocessing.Process(target = squared_list, args = ([1,2,3,4], q))
#     p2 = multiprocessing.Process(target = print_list, args = (q,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()



#PIPE
# msgs = ["Hey", "Hello", "Hru?", "END"]
# def send_msgs(conn,msgs):
#     for msg in msgs:
#         conn.send(msg)
# def recv_msg(conn):
#     while 1:
#         msg = conn.recv()
#         if msg == "END":
#             break
#         print(msg)

# if __name__ == '__main__':
#     parent_conn, child_conn = multiprocessing.Pipe()
#     p1 = multiprocessing.Process(target = send_msgs, args = (parent_conn,msgs))
#     p2 = multiprocessing.Process(target = recv_msg, args = (child_conn,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

#POOLING BETWEEN PROCESS
# def square(n):
#     print(n,os.getpid())
#     return n * n
# if __name__ == '__main__':
#     mylist = [1,2,3,4,5]
#     result = []
#     p = multiprocessing.Pool()
#     result = p.map(square, mylist)
#     print(result)
#     print(multiprocessing.cpu_count())

#PROCESS SYNCHRONIZATION
# def withdraw(balance,lock):
#     for _ in range(10000):
#         lock.acquire()
#         balance.value = balance.value - 1
#         lock.release()
# def deposite(balance,lock):
#     for _ in range(10000):
#         lock.acquire()
#         balance.value = balance.value + 1
#         lock.release()
# def perform_transaction():
#     balance = multiprocessing.Value('i',100)
#     lock = multiprocessing.Lock()
#     p1 = multiprocessing.Process(target = withdraw, args = (balance,lock))
#     p2 = multiprocessing.Process(target = deposite, args = (balance,lock))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print('Final Balance is : {}'.format(balance.value))
# if __name__ == '__main__':
#     perform_transaction()
