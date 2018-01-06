import mmap
import contextlib
import time
import threading
import json



class client(threading.Thread):
    def __init__(self, mutex, buff):
        super(client, self).__init__()
        self.mutex = mutex
        self.buff = buff
        self.ready = False

    def fetch_data(self):
        self.buff.open_mmap()
        ret, s = self.buff.buffer_read()
        if s != "":
            sm_data = json.loads(s)
            list = sm_data["data"]
            val = list.pop(0)
            if len(list) == 0:
                json_str = ""
            else:
                data = {}
                data["data"] = list
                json_str = json.dumps(data)
            #print("[Client] Store " + json_str)
            self.buff.buffer_reset()
            self.buff.buffer_write(json_str)
            self.buff.close_mmap()
        else:
            val = []

        return val


    def run(self):
        while True:
            if self.mutex.acquire(1):
                #print("[Client] Get Lock")
                val = self.fetch_data()
                #print("[Client] Fetch Data")
                if val != []:
                    print(val)
                self.mutex.release()
                #print("[Client] Release Lock")
            time.sleep(0.08)
        print("[Client] End")
