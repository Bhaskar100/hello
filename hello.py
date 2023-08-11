from threading import Thread
import threading
import time
def disp(name):
    lock.acquire()
    for x in range(10):
        print("Good Morning..... ",name)
        time.sleep(1)
        lock.release()
lock = threading.Lock()
t1 = Thread(target=disp,args=("ratan",))
t2 = Thread(target=disp,args=("anu",))
t1.start()
t2.start()