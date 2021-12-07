from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

# im = Image.open('./D455/1201/D455采集样例_20211129/depth.tiff')
#
# # im.save('./D455/1201/D455采集样例_20211129/result/depth.png')
#


from libtiff import TIFF

depth_scale = 0.0010000000474974513
tif = TIFF.open('./D455/1201/D455采集样例_20211129/depth.tiff', mode='r')
img = tif.read_image()
img_1 = img * depth_scale

print(np.max(img),np.max(img_1))

plt.imshow(img)
# plt.imshow(img_1)
plt.show()

# cv2.imwrite('./D455/1201/D455采集样例_20211129/result/depth_scale.png',img_1)


MAX_DEPTH =255
cmap = plt.cm.jet
# cmap.set_bad(color='black')
sc = plt.imshow(img, cmap=cmap, vmax=np.log(MAX_DEPTH))
# plt.colorbar()
# plt.savefig('test_1_c.png')
plt.show()
##################################################
