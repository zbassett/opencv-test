import matplotlib
matplotlib.use('Agg')

import cv2
import numpy as np
from matplotlib import pyplot as plt
matplotlib.use('Agg')

img = cv2.imread('beast.jpg',0)
plt.hist(img.ravel(),256,[0,256])
plt.savefig('histogram.png')