import os
import numpy as np
import dmcam
import cv2
import matplotlib.pyplot as plt
from ctypes import cdll, c_char_p

oni_path = bytes("./oni/1129/20211129_smartTOF-s/dmrep_20211129_142008-2-b.oni", encoding="ascii")
dev = dmcam.dev_open_by_uri(oni_path)

dmcam.cap_start(dev)

f = bytearray(640 * 480 * 4 * 2)
count = 0
run = True
while run:
    # get one frame
    finfo = dmcam.frame_t()
    ret = dmcam.cap_get_frames(dev, 1, f, finfo)
    # print("get %d frames" % ret)
    if ret > 0:
        w = finfo.frame_info.width
        h = finfo.frame_info.height

        print(" frame @ %d, %d, %dx%d" %
              (finfo.frame_info.frame_idx, finfo.frame_info.frame_size, w, h))

        dist_cnt, dist = dmcam.frame_get_distance(dev, w * h, f, finfo.frame_info)
        gray_cnt, gray = dmcam.frame_get_gray(dev, w * h, f, finfo.frame_info)
        # dist = dmcam.raw2dist(int(len(f) / 4), f)
        # gray = dmcam.raw2gray(int(len(f) / 4), f)

        dist_img = dist.reshape(h, w)
        gray_img = gray.reshape(h, w)
        #
        # cv2.imwrite('./oni/1129/20211129_smartTOF-s/dmrep_20211129_142008-2-b/depth/depth_frame_%d.png'%finfo.frame_info.frame_idx, dist_img)
        # cv2.imwrite('./oni/dmrep_20211123_172643/gray/gray_frame_%d.png' %finfo.frame_info.frame_idx, gray_img)
        #
        MAX_DEPTH = 255
        cmap = plt.cm.jet
        cmap.set_bad(color='black')
        sc = plt.imshow(dist_img, cmap=cmap, vmax=np.log(MAX_DEPTH))
        # plt.colorbar()
        plt.savefig('./oni/1129/20211129_smartTOF-s/dmrep_20211129_142008-2-b/depth_c/depth_frame_%d_c.png'%finfo.frame_info.frame_idx)
        # plt.show()

        count += 1
        if count >= 100:
            break

    else:
        break
    # time.sleep(0.01)
    # break

#
# dist_cnt, dist_img = dmcam.cmap_dist_u16_to_RGB(len(dist)*3,dist,
#                                                 dmcam.DMCAM_CMAP_OUTFMT_RGB,
#                                                 0,4000, None)
