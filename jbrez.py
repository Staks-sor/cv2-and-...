import cv2
import os

path = 'Image'
d_path = 'Image_resize'
filelist = os.listdir(path)
i = 1
for item in filelist:
    if item.endswith('.jpg'):
        src = os.path.join(os.path.abspath(path), item)
        dst = os.path.join(os.path.abspath(d_path), '' + str(i) + '.jpg')
        i += 1

        src_img = cv2.imread(src)
        img = src_img[115:350, 210:445]
        img_resize = cv2.resize(img, (119, 119), interpolation=cv2.INTER_CUBIC)
        # x, y, w, h = 300, 300, 350, 445
        # crop_img1 = img[y: y + h, x: x + w]
        # crop_img2 = img[x: x + w, y: y + h]
        cv2.imshow("cropped", img_resize)
        writefile = 'Image_resize/is42{0:05d}.jpg'.format(i)
        isWritten = cv2.imwrite(writefile, img_resize)
        if isWritten:
            print(img_resize.shape)
            print(f"фаил сохранен")
cv2.waitKey(0)
