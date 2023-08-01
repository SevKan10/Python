import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('OpenCV/img/z4533842960509_92f4ffbf7b11c54cbe5a2102aa643814.jpg',cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()