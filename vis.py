import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
megusta = cv2.imread('megusta.png', -1)

def run():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        gray_image = cv2.cvtColor( frame, cv2.COLOR_RGB2RGBA);
        #gray_image = frame

        faces = face_cascade.detectMultiScale(
            gray_image,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(gray_image, (x, y), (x+w, y+h), (0, 255, 0), 2)


        cv2.imshow("preview", gray_image)
        rval, frame = vc.read()
        key = cv2.waitKey(1)
        if key == 27: # exit on ESC
            break
    cv2.destroyWindow("preview")

if __name__ == '__main__':
    run()