import time
import math

def calculate_time(func):
    def inner_1(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()

        print("The time required for the execution is :", end - start)

    return inner_1

@calculate_time
def factorial(num):
    time.sleep(2)
    print("This is factorial of given number : ", math.factorial(num))


factorial(10)