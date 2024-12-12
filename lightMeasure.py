from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.framerate = 20
camera.resolution = (1980, 1020)

camera.start_preview() 

sleep(2)
camera.capture('dm_blue2.png') # Take a picture - и сохранение фото

#camera.stop_preview() - остановка предварительного просмотра

#camera.resolution = (1280, 720) - задание разрешения снимка
#camera.contrast = 10 - задание контраста снимка

#camera.close() -   метод для освобождения ресурсов камеры
