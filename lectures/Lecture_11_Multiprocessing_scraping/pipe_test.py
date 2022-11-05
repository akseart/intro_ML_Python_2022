from time import sleep
def f(conn):
    sleep(1)
    conn.send([42, None, 'hello'])
    sleep(1)
    print(conn.recv())
    conn.close()
