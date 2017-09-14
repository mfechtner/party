import cv2, threading, numpy

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
megusta = cv2.imread('megusta.png', -1)

def overlay(dest, source, posx, posy, S=None, D=None):
    S = S or (0.5, 0.5, 0.5, 0.5)
    D = D or (0.5, 0.5, 0.5, 0.5)

circles = []

def draw_cirlce(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        circles.append((x, y))

def run():
    window_name = "preview"

    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, draw_cirlce)

    vc = cv2.VideoCapture(0)

    layers = [None, None, None]
    offset = 0

    while True:
        ret, image = vc.read()

        for x, y in circles:
            print(x, y)
            cv2.circle(image,(x,y),100,(255,0,0),-1)

        cv2.imshow(window_name, image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyWindow(window_name)

if __name__ == '__main__':
    run()