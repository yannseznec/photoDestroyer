# !/bin/python
import time
import os
import random
import threading

def displayDestroy():
  threading.Timer(5.0, displayDestroy).start()
  random_file=photos/random.choice(os.listdir("photos"))
  print(random_file)
  os.system("feh -F "+random_file)
  os.system("killall feh")
  os.system("rm "+random_file)



displayDestroy()
