import cv2

# Читать картинку
img = 'C:/Users/stass/OneDrive/Pictures/dev.jpg'
img = cv2.imread(img)
cv2.imshow('original', img)

# Выберите ROI
roi = cv2.selectROI(windowName="original", img=img, showCrosshair=True, fromCenter=False)
x, y, w, h = roi
print(roi)

# Показать ROI и сохранить картинку
if roi != (0, 0, 0, 0):
    crop = img[y:y+h, x:x+w]
    cv2.imshow('crop', crop)
    cv2.imwrite('crop.jpg', crop)
    print('Saved!')

# выбывать
cv2.waitKey(0)
cv2.destroyAllWindows()