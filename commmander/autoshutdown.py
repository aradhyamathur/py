__author__ = 'krishna'
import os
import tkinter as tk
from datetime import *
import threading

#var = None
thread1 = None
var = ""

class myThread(threading.Thread):
    def __init__(self, threadID, name, shutTime):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.shutTime = shutTime

    def run(self):
        print(var)
        os.system("shutdown -h " + var)
        print(var)


class ShutDownClass(tk.Tk):


    def __init__(self):
        tk.Tk.__init__(self)
        self.shutdownLabel = tk.Label(self, text="Enter shutdown countdown")
        self.shutdownLabel.pack()

        self.shutdownButton = tk.Button(self, text="Shutdown", command=self.on_click)
        self.shutdownButton.pack()

        self.stopButton = tk.Button(self, text="stop", command=self.stopTime)
        self.stopButton.pack()

        self.timeEntry = tk.Entry(self)
        self.timeEntry.pack()

    def on_click(self):

        global var
        var = self.timeEntry.get()
        print(var)
        thread1 = myThread(1, "thread-1", var)

        if var == "":
            print("no value")

        else:
            '''  if type(var) == time:
                        print("ok")
                else:
                    print("wrong val")
                    print(type(var))
            '''

            self.timeEntry.delete(0, 'end')
            self.timeEntry.insert(0, "started")

            try:
                thread1.start()


            except:
                self.timeEntry.delete(0, 'end')
                self.timeEntry.insert(0, "check time value")

    def stopTime(self):
        print("stop")
        # os.system('^C')

        self.timeEntry.delete(0, 'end')
        self.timeEntry.insert(0, "stopped")


app = ShutDownClass()
app.mainloop()
