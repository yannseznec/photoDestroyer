# !/bin/python
import time
import os
import random
import threading

waitTime = 3

def displayDestroy():
  event = threading.Event()
  random_file="photos/"+random.choice(os.listdir("photos"))
  print(random_file)
  os.system("feh -F --reload=1 "+random_file + "&")
  event.wait(waitTime)
  os.system("convert -resize 50% -resize 200% "+random_file+" "+random_file)
  print("destroy1")
  event.wait(waitTime)
  os.system("convert -resize 25% -resize 400% "+random_file+" "+random_file)
  print("destroy2")
  event.wait(waitTime)
  os.system("convert -resize 10% -resize 1000% "+random_file+" "+random_file)
  print("destroy3")
  event.wait(waitTime)
  os.system("convert -resize 5% -resize 2000% "+random_file+" "+random_file)
  print("destroy4")
  event.wait(waitTime)
  os.system("convert -resize 1% -resize 10000% "+random_file+" "+random_file)
  print("destroy5")
  event.wait(waitTime)
  os.system("convert -resize .1% -resize 100000% "+random_file+" "+random_file)
#  os.system("convert -resize .1% -filter Point -resize 100000% -filter Point "+random_file+" "+random_file)
  print("destroy6")
  event.wait(waitTime)
  os.system("rm "+random_file)
  print("deleted")

displayDestroy()
