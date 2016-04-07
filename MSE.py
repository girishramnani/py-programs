from matplotlib import pyplot
from matplotlib.pyplot import imshow, plot

__author__ = 'girish'

from PIL import Image
from numpy import  *
f = open("dirty.jpg")
x =Image.open("dirty.jpg")

data = asarray(x)
print(data)