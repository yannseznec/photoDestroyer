# !/bin/python
import time
import os
import random
import threading

def displayDestroy():
  # threading.Timer(5.0, displayDestroy).start()
  random_file="photos/"+random.choice(os.listdir("photos"))
  print(random_file)
  os.system("feh -F "+random_file)
  sleep(3.0)
  os.system("convert -resize 10% -filter Point -resize 1000% -filter Point "+random_file+" "+random_file)
  os.system("kill -2 $pid")
  
displayDestroy()
