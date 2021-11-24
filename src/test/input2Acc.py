#test case: import, from, as, while, continue, if, return, raise

import numpy
from matplotlib.image import imread
from matplotlib import pyplot as plt
from random import normalvariate
from math import sqrt
from PIL import Image
import time

i = 0
while i <= 10:    
    if i == 7:
        i += 1
        continue  
    print("The Number is  :" , i)
    i += 1

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = 3
    if i != len(a) and a[i] == x:
        return i
    raise ValueError