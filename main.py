import cv2
import os
from image_to_ascii_lib.converter import image_to_ascii, ascii_to_image

frames = 0

if not os.path.exists('input_img'):
    os.makedirs('input_img')

if not os.path.exists('output_img'):
    os.makedirs('output_img')

def extract():
    cam = cv2.VideoCapture("./input.mp4")

    currentframe = 0

    while(True):
        ret,frame = cam.read()

        if ret:
            name = './input_img/frame' + str(currentframe) + '.jpg'
            cv2.imwrite(name, frame)

            currentframe += 1
        else:
            break

    cam.release()
    cv2.destroyAllWindows()
    # better way to do dis but i am lazy
    global frames
    frames = currentframe
    print("extracted")

def convert(inputFileName, outFileName):
    ascii_art = image_to_ascii(inputFileName, size=(30, 50))
    ascii_art_image = ascii_to_image(ascii_art)
    ascii_art_image.save(outFileName)

extract()
for i in range(1, frames):
    inputFileName = f"input_img/frame{i}.jpg"
    outFileName = f"output_img/frame{i}.jpg"
    convert(inputFileName=inputFileName, outFileName=outFileName)