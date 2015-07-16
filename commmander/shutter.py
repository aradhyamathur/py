__author__ = 'krishna'
from tkinter import *
import threading
import os


var = None
thread1 = None

def startTime(event):
    print("startTime")


class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name


    def run(self):
        print(var)
        os.system("shutdown -h " + var)
        print(var)

root = Tk
startButton = Button(root, text="start")




root.mainloop()
