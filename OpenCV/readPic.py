import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('OpenCV/img/z4533842960509_92f4ffbf7b11c54cbe5a2102aa643814.jpg') #Hàm đọc ảnh, cv2.IMREAD_GRAYSCALE thêm vào sau để chuyển chế độ xám

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # để ẩn giá trị dấu chấm trên trục X và Y
plt.plot([200, 300, 400], [100, 200, 300], 'c', linewidth=5)
plt.show()
