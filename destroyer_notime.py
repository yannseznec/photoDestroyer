# !/bin/python
import time
import os
import random
import threading
import subprocess

currentTime = 0
rate = 10
displayTime = 100
newTime = 1
random_file = "imagename"

def timeCounter():
  global currentTime
  global random_file
  global displayTime
  global newTime
  if currentTime > 10:
    os.system("rm "+random_file)
    print("deleted")
    randomImage()
    currentTime = 0
   # os.system("feh -F --hide-pointer --reload=2 "+random_file + "&")
    timeCounter()
  if currentTime < newTime:
    currentTime+=1
    resize1 = str((1/currentTime)*100)
    resize2 = str(currentTime*100)
   # os.system("convert -resize "+resize1+"% -resize "+resize2+"% "+random_file+" "+random_file)
    newTime = currentTime + 1
    print(currentTime)
    time.sleep(2)
    timeCounter()

    


def randomImage():
  global random_file
  # random_file="../usb/photos/"+random.choice(os.listdir("../usb/photos/"))
  # running from a USB stick seems to make it freeze, maybe need a better stick?
  random_file="photos/"+random.choice(os.listdir("photos"))
  print(random_file)




randomImage()
# os.system("feh -F -R --hide-pointer "+random_file + "&")
# os.system("feh -F --hide-pointer --reload=2 "+random_file + "&")
os.system("display "+random_file + "&")
timeCounter()
