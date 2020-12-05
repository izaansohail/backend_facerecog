# Importing all necessary libraries
import cv2
import os
import PIL
# Read the video from specified path
cam = cv2.VideoCapture( 'testvideo.mp4')
try:
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')
# if not created then raise error
except OSError:
    print('Error: Creating directory of data')
# frame
final = 0
currentframe = 0
while(True):
    # reading from frame
    ret, frame = cam.read()
    if ret:
        # if video is still left continue creating images
        name = './data/' + str(currentframe) + '.jpg'
        print('Creating...' + name)
        # writing the extracted images
        cv2.imwrite(name, frame)
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
        final = currentframe
    else:
        break
# Release all space and windows once done
cam.release()
currentframe = 0
while(currentframe < final):
           img = cv2.imread('D:\\izaan\\Work\\University\\university docs\\Semester 5\\Database Systems\\Project\\BackEnd\\data\\' + str(currentframe) + '.jpg')
           path = 'D:\\izaan\\Work\\University\\university docs\\Semester 5\\Database Systems\\Project\\BackEnd\\new'
           cv2.imwrite(os.path.join(path, str(currentframe) + '.jpg'), img)
           currentframe += 1
           cv2.destroyAllWindows()
