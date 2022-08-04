import threading
import time
def print_hello(n): 
  for i in range(n):
    if i == 10:
      time.sleep(2)
    print("Hello")
def print_numbers(num): 
  for i in range(num):
    print(i+1)
print("Staring of Main thread.")
thread1 = threading.Thread(target = print_hello, args = (20,))
thread2 = threading.Thread(target = print_numbers, args = (10,))
thread1.start()
thread2.start() 
print("It's the main thread again!")