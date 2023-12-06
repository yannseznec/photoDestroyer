# !/bin/python
import time
import os
import random
import threading

currentTime = 0
rate = 10
displayTime = 100
random_file = "imagename"

def timeCounter():
  global currentTime
  global random_file
  global displayTime
  threading.Timer(rate, timeCounter).start()
  event = threading.Event()
  currentTime+=1
  resize1 = str((1/currentTime)*100)
  resize2 = str(currentTime*100)
  os.system("convert -resize "+resize1+"% -resize "+resize2+"% "+random_file+" "+random_file)
  event.wait(8)
  print(resize1)
  if resize1 < 2:
    os.system("rm "+random_file)
    print("deleted")
    randomImage()
    os.system("feh -F --hide-pointer --reload=3 "+random_file + "&")
    currentTime = 0
    


def randomImage():
  global random_file
  # random_file="../usb/photos/"+random.choice(os.listdir("../usb/photos/"))
  # running from a USB stick seems to make it freeze, maybe need a better stick?
  random_file="photos/"+random.choice(os.listdir("photos"))
  print(random_file)




randomImage()
os.system("feh -F --hide-pointer --reload=3 "+random_file + "&")
timeCounter()
