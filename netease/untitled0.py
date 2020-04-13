# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:33:35 2020

@author: Mat_Laptop
"""

from multiprocessing import Process, Queue


def consumer(tasks,q):
    for i in tasks:
        q.put(i)
        print("task",i)

def producter(q):
    while True:
        t = q.get()
        print(t)  
   
    
if __name__=="__main__":
    taskList = [1,2,3,4]
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"
    q = Queue()
    pCon = Process(target=consumer, args=(q,))
    pPro = Process(target=producter, args=(q,))
    pCon.start()
    pPro.start()
    pCon.join()
    pPro.join()
    print("hello")
    