from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt


rawData = open('./D455/2_Depth.raw', 'rb').read()
# imgSize = (703, 1248)
# img = Image.frombytes('L', imgSize, rawData, 'raw','F;16')
# img.save('./D455/2_Depth.png')
# im = Image.fromstring('F', (512,512), rawData, 'raw', 'F;32F')
# out = im.point(lambda i:i*(1.0/4.0))
# out.show()


img = cv2.imread('./D455/1_Color.png')
type = img.dtype
width, height, channels = img.shape


imgData = np.fromfile('./D455/2_Depth.raw', dtype=type)
imgData = imgData.reshape(width,height,2)
imgData_1 = imgData[:,:,0]
imgData_2 = imgData[:,:,1]
# cv2.imwrite('test_1.png',imgData_1)
# cv2.imwrite('test_2.png',imgData_2)

# ymax = 255.0
# ymin = 0.0
# xmax = np.max(imgData_2)
# xmin = np.min(imgData_2)
# imgData_2_1 = np.round((ymax-ymin)*(imgData_2-xmin)/(xmax-xmin)+ymin)
# cv2.imwrite('test_3.png', imgData_2_1)

MAX_DEPTH =255
cmap = plt.cm.jet
cmap.set_bad(color='black')
sc = plt.imshow(imgData_2, cmap=cmap, vmax=np.log(MAX_DEPTH))
plt.colorbar()
plt.savefig('test_2_cc.png')
# sc_1 = plt.imshow(imgData_1, cmap=cmap, vmax=np.log(MAX_DEPTH))
# plt.savefig('test_1_c.png')
plt.show()


# cv2.imwrite('test_2_c.png', value)
