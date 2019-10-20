import threading
from threading import Thread

print(threading.current_thread().name)


class PrintThread(Thread):
    def run(self):
        print("In thread :", threading.current_thread().name)
        for i in range(1, 50):
            print(i, end=' ')


t = PrintThread()
t.name = 'PrintThread'
t.start()

for i in range(1, 50):
    print(i)
