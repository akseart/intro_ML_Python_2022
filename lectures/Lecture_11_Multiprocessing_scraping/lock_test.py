import time
import random
def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
        time.sleep(random.random())
    finally:
        l.release()
