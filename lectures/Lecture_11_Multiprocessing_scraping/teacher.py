from multiprocessing import current_process
from time import sleep
def foo(studs, result):
    while True:
        current_stud = studs.get()
        name = current_process().name
        result.put(f"{name} начал    проверять студента {current_stud[1]}")
        sleep(current_stud[0] / 20)
        result.put(f"{name} закончил проверять студента {current_stud[1]}")
        if studs.empty():
            break
