import cv2
import os.path

vid_capture = cv2.VideoCapture('Camera.mp4')
if (vid_capture.isOpened() == False):
    print("Ошибка открытия видеофайла")
# Чтение fps и количества кадров
else:
    # Получить информацию о частоте кадров

    fps = vid_capture.get(5)
    print('Фреймов в секунду: ', fps, 'FPS')
    # Получить количество кадров

    frame_count = vid_capture.get(7)
    print('Частота кадров: ', frame_count)
    print('\n-----------------------------\nДля завершения нажмите "q" или Esc...')
file_count = 0
i = 0
while (vid_capture.isOpened()):
    # Метод vid_capture.read()
    ret, frame = vid_capture.read()
    if ret == True:
        cv2.imshow('Look', frame)
        file_count += 1
        if file_count == 15:
        # if file_count%15 == 0:
            print(f'Кадр {file_count}')
            # cv2.imwrite(f'image/{file_count}.png', img)
            file_count = 0

            writefile = 'Image/is42_{0:04d}.jpg'.format(i, file_count)
            isWritten = cv2.imwrite(writefile, frame)
            if isWritten:
                print(f"фаил сохранен {file_count}")

            i += 1

        key = cv2.waitKey(20)

        if (key == ord('q')) or key == 27:
            break
    else:
        break

vid_capture.release()
cv2.destroyAllWindows()
