import os, random

folder=r"/Users/yann/Desktop/photoDestroyer/"

a=random.choice(os.listdir(folder))
print(a)

#os.open(a, os.O_RDWR)
from PIL import Image
file = folder+a
Image.open(file).show()