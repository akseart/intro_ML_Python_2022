from time import sleep
def f(q):
    sleep(1)
    q.put([42, None, 'hello'])
    sleep(1)
    q.put([21, None, 'hell'])
