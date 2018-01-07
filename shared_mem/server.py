import mmap
import contextlib
import time
import os
import threading
import random
import json

from shared_mem.client import *
from shared_mem.store_buffer import *


class server(threading.Thread):
    def __init__(self, mutex, buff):
        super(server, self).__init__()
        self.mutex = mutex
        self.buff = buff
        self.all_ready = False


    def generate_new_data(self, i):
        a = random.randint(10000, 20000)
        b = random.randint(10000, 20000)
        c = random.randint(10000, 20000)
        return [i, a,b,c]

    def send_data(self, new_data):
        self.buff.open_mmap()
        ret, s = self.buff.buffer_read()
        if s != "":
            print("[Server] Get sm:" + s)
            old_data = json.loads(s)
            list = old_data["data"]
        else:
            list = []
        list.append(new_data)
        data = {}
        data["data"] = list
        json_str = json.dumps(data)
        self.buff.buffer_reset()
        self.buff.buffer_write(json_str)
        self.buff.close_mmap()

    def run(self):
        for i in range(0, 100000):
            if self.mutex.acquire(1):
                #print("[Server] Get Lock")
                new_data = self.generate_new_data(i)
                time_s = time.time()
                self.send_data(new_data)
                time_e = time.time()
                print("[Server]" + str(time_e - time_s))
                #print("[Server] Send Data")
                time.sleep(random.random())
                #print("[Server] Release Lock")
                self.mutex.release()
        print("[Server] End")

if __name__ == '__main__':
    mutex_lock = threading.Lock()
    buff = store_buffer()
    buff.initialize()
    serv = server(mutex_lock, buff)
    serv.start()
    time.sleep(0.2)
    if serv.all_ready == True or True:
        print("Open Client")
        client = client(mutex_lock, buff)
        client.start()

