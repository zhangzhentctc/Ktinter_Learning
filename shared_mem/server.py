import mmap
import contextlib
import time
import os
import threading
import random
import json

from shared_mem.client import *


FILE_NAME = "./test.dat"
FILE_SIZE = 1024




class server(threading.Thread):
    def __init__(self, mutex):
        super(server, self).__init__()
        self.mutex = mutex
        self.all_ready = False

    def init_all(self):
        self.f_handler = open(FILE_NAME, "w")
        self.f_handler.write('\x00' * FILE_SIZE)
        self.f_handler.close()
        self.f_handler = open(FILE_NAME, "r+")
        self.mmap = mmap.mmap(self.f_handler.fileno(), FILE_SIZE, access=mmap.ACCESS_WRITE)

    def create_shared_mem(self):
        try:
            self.f_handler = open(FILE_NAME, "w")
            self.f_handler.write('\x00' * FILE_SIZE)
            self.f_handler.close()
            self.if_sm_create = True
            print("[Server] Create Shared Mem OK")
        except:
            self.if_sm_create = False
            print("[Server] Create Shared Mem Fail")

    def open_shared_mem_file(self):
        try:
            self.f_handler = open(FILE_NAME, "r+")
            self.if_sm_f_open = True
            print("[Server] Open Shared Mem OK")
        except:
            self.if_sm_f_open = False
            print("[Server] Open Shared Mem Fail")
        return

    def open_shared_mem(self):
        try:
            self.mmap = mmap.mmap(self.f_handler.fileno(), FILE_SIZE, access=mmap.ACCESS_WRITE)
            self.if_mmap_open = True
        except:
            self.if_mmap_open = False
            print("[Server] Open MMAP Fail")

    def if_ready(self):
        if self.if_sm_f_open == True and \
           self.if_sm_create == True:
            self.all_ready = True
            print("[Server] All OK")
        else:
            self.all_ready = False

    def prepare_client(self):
        self.create_shared_mem()
        self.open_shared_mem_file()
        self.open_shared_mem()
        self.if_ready()

    def generate_new_data(self):
        a = random.randint(10000, 20000)
        b = random.randint(10000, 20000)
        c = random.randint(10000, 20000)
        return [a,b,c]

    def run(self):
        self.prepare_client()
        if self.all_ready == True:
            print("[Server] Start")

            for i in range(1, 10001):
                if self.mutex.acquire(1):
                    print("[Server] Get Lock")
                    self.open_shared_mem()
                    self.mmap.seek(0)
                    s = self.mmap.read(FILE_SIZE).decode().replace('\x00', '')
                    if s != "":
                        print("[Server] Get sm:" + s)
                        old_data = json.loads(s)
                        list = old_data["data"]
                    else:
                        list = []
                    # new_data = self.generate_new_data()
                    new_data = [i, i, i]
                    list.append(new_data)
                    data = {}
                    data["data"] = list
                    json_str = json.dumps(data)

                    # json_str.rjust(FILE_SIZE, '\x00')
                    self.f_handler.write('\x00' * FILE_SIZE)
                    self.mmap.seek(0)
                    self.mmap.write(json_str.encode())
                    self.mmap.flush()
                    self.mmap.close()
                    print("[Server] Release Lock")
                    self.mutex.release()
                    print("[Server] " + json_str)

                time.sleep(random.random())
        print("[Server] End")

if __name__ == '__main__':
    mutex_lock = threading.Lock()
    serv = server(mutex_lock)
    serv.start()
    time.sleep(0.2)
    if serv.all_ready == True:
        print("Open Client")
        client = client(mutex_lock)
        client.start()

