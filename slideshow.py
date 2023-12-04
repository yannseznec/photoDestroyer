# !/bin/python
import time
import os
import random

def displayDestroy():
  random_file=random.choice(os.listdir("photos"))
  print(random_file)
  time.sleep(1)
  os.system("feh -F photos/"+random_file)

displayDestroy()
