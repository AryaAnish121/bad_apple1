import cv2
import os
from image_to_ascii_lib.converter import image_to_ascii, ascii_to_image

def extract():
    cam = cv2.VideoCapture("./bad_apple.mp4")

    if not os.path.exists('input_img'):
        os.makedirs('input_img')

    currentframe = 0

    while(True):
        ret,frame = cam.read()

        if ret:
            name = './input_img/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name)

            cv2.imwrite(name, frame)

            currentframe += 1
        else:
            break

    cam.release()
    cv2.destroyAllWindows()

def convert(inputFileName, outFileName):
    ascii_art = image_to_ascii(inputFileName, size=(30, 50))
    ascii_art_image = ascii_to_image(ascii_art)
    ascii_art_image.save(outFileName)


convert("test.jpg", "opt.jpg")