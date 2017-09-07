import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
megusta = cv2.imread('megusta.png', -1)

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

    counter = 0

    faces = []

    last_frame = []

    while rval:
        counter += 1
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.GaussianBlur(frame, (21, 21), 0)       

        if len(last_frame) > 0:
            frame_delta = cv2.absdiff(last_frame, frame)
            thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        else:
            thresh = None
            frame_delta = None
        last_frame = frame

        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        if thresh:
            faces = face_cascade.detectMultiScale(
                gray_image,
                scaleFactor=1.3,
                minNeighbors=10,
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
                        data =  megusta_fit[sy,sx]
                        mask = data[3]
                        if mask > 0:
                            color = data[0:3]
                            frame[y+sy,x+sx] = color
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
        


        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(40)
        if key == 27: # exit on ESC
            break
    cv2.destroyWindow("preview")

if __name__ == '__main__':
    run()