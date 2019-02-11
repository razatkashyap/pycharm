import threading
import time
class Hold():
    def loop(self):
        for x in range(5):
            print("First :"+str(x))
            time.sleep(1)

    def hoop(self):
        for x in range(5):
            print("second :"+str(x))
            time.sleep(3)

h = Hold()
threading.Thread(target=h.loop).start()
threading.Thread(target=h.hoop).start()