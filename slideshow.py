# !/bin/python
import time
import os
import random

print("Slideshow running soon…")
random_file=random.choice(os.listdir("photos"))
print(random_file)
time.sleep(1)
os.system("feh -F "+random_file)

while 1:
  time.sleep(1)