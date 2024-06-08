import threading
import time
print("------------------------------------------")
def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Thread 1: {i}")

def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)
        print(f"Thread 2: {letter}")

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Main thread exiting.")


import multiprocessing
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Process 1: {i}")

def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)
        print(f"Process 2: {letter}")

if __name__ == "__main__":
    # Create two processes
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_letters)

    # Start the processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

    print("Main process exiting.")

print("-------------------------------------------------------")

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Thread 1: {i}")

def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)
        print(f"Thread 2: {letter}")

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Main thread exiting.")

print("------------------------------------------------")