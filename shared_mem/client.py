import mmap
import contextlib
import time
import threading
import json

FILE_NAME = "./test.dat"
FILE_SIZE = 1024

class client(threading.Thread):
    def __init__(self, mutex):
        super(client, self).__init__()
        self.mutex = mutex
        self.ready = False

    def open_shared_mem(self):
        try:
            self.f_handler = open(FILE_NAME, "r+")
            self.if_sm_open = True
            print("[Client] Open Shared Mem OK")
        except:
            self.if_sm_open = False
            print("[Client] Open Shared Mem Fail")
        return

    def if_ready(self):
        if self.if_sm_open == True:
            self.ready = True
        else:
            self.ready = False

    def prepare_client(self):
        self.open_shared_mem()
        self.if_ready()

    def run(self):
        self.prepare_client()
        if self.ready == True:
            print("[Client] Start")
            while True:
                if self.mutex.acquire(1):
                    print("[Client] Get Lock")
                    try:
                        m = mmap.mmap(self.f_handler.fileno(), FILE_SIZE, access=mmap.ACCESS_WRITE)
                    except:
                        print("[Client] MMap Fail")
                        self.mutex.release()
                        time.sleep(0.2)
                        continue
                    s = m.read(FILE_SIZE).decode().replace('\x00', '')
                    if s != "":
                        sm_data = json.loads(s)
                        list = sm_data["data"]
                        val = list.pop(0)
                        if len(list) == 0:
                            json_str=""
                        else:
                            data = {}
                            data["data"] = list
                            json_str = json.dumps(data)
                        print("[Client] Store "+ json_str)

                        #json_str.rjust(FILE_SIZE, '\x00')
                        m.seek(0)
                        blank = "\0" * FILE_SIZE
                        m.write(blank.encode())
                        m.seek(0)
                        m.write(json_str.encode())
                        m.flush()
                        m.close()
                        print("[Client] Get")
                        print(val)
                    self.mutex.release()
                    print("[Client] Release Lock")
                time.sleep(0.5)
        print("[Client] End")

