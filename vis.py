import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
megusta = cv2.imread('megusta.png')

def overlay(dest, source, posx, posy, S=None, D=None):
    S = S or (0.5, 0.5, 0.5, 0.5)
    D = D or (0.5, 0.5, 0.5, 0.5)

    

def run():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        gray_image = cv2.cvtColor( frame, cv2.COLOR_RGB2GRAY);

        faces = face_cascade.detectMultiScale(
            gray_image,
            scaleFactor=1.1,
            minNeighbors=3,
            minSize=(50, 50),
            maxSize=(400, 400),
        )

        fh,fw = frame.shape[0], frame.shape[1]
        for (x, y, w, h) in faces:
            megusta_fit = cv2.resize(megusta, (w, h))
            for sx in range(0,w):
                for sy in range(0,h):
                    if x+sx+1 > fw or y+sy+1 > fh:
                        continue
                    frame[x+sx,y+sy] = megusta_fit[sx,sy]

            #overlay(frame, megusta, x, y)
            #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        


        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(1)
        if key == 27: # exit on ESC
            break
    cv2.destroyWindow("preview")

if __name__ == '__main__':
    run()