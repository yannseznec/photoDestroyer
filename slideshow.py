# !/bin/python
import time
import os
import random
import threading

def displayDestroy():
  threading.Timer(5.0, displayDestroy).start()
  random_file=random.choice(os.listdir("photos"))
  print(random_file)
  os.system("feh -F photos/"+random_file)
  os.system("killall feh")


displayDestroy()
