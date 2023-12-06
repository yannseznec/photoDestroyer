# !/bin/python
import time
import os
import random
import threading

currentTime = 0
rate = 5
displayTime = 100
random_file = "imagename"

def timeCounter():
  global currentTime
  global random_file
  global displayTime
  threading.Timer(rate, timeCounter).start()
  event = threading.Event()
  currentTime+=3
  resize1 = str((1/currentTime)*100)
  resize2 = str(currentTime*100)
  os.system("feh -F --reload=3 "+random_file + "&")
  os.system("convert -resize "+resize1+"% -resize "+resize2+"% "+random_file+" "+random_file)
  event.wait(4)
  print(resize1)
  if currentTime > displayTime:
    os.system("rm "+random_file)
    randomImage()
    currentTime = 0
    print("deleted")

def randomImage():
  global random_file
  random_file="../usb/photos/"+random.choice(os.listdir("../usb/photos"))




randomImage()
timeCounter()
