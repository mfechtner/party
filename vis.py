import cv2, threading, numpy

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
megusta = cv2.imread('megusta.png', -1)

def overlay(dest, source, posx, posy, S=None, D=None):
    S = S or (0.5, 0.5, 0.5, 0.5)
    D = D or (0.5, 0.5, 0.5, 0.5)

    

def run():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    layers = [None, None, None]
    offset = 0

    while True:
        ret, image = vc.read()
        width, height, colors = image.shape
        scale = 640.0 / width
        #image = cv2.resize(image, (0,0), fx=scale, fy=scale)
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray,50,150, apertureSize = 3)

        layers[offset%len(layers)] = edges

        for layer in layers:
            if layer is not None:
                continue
            edges = numpy.concatenate((layer, edges))

        cv2.imshow('Camera stream', edges)
        
        offset += 1

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyWindow("preview")

if __name__ == '__main__':
    run()