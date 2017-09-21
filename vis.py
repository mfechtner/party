import cv2, numpy, time
from imutils import perspective
import math

class MouseHandler(object):
    def __init__(self, videos=[]):
        self.edit = False
        self.drag = False
        self.videos = videos
        self.candidate = None

    def callback(self, event, x, y, flags, param):
        for video in self.videos:
            if video.points is None:
                return

        if event == cv2.EVENT_LBUTTONDOWN:
            self.drag = not self.drag
            self.edit = self.drag
            print('drag', self.drag)
            return

        if not self.drag or event != cv2.EVENT_MOUSEMOVE:
            self.candidate = None
            return

        if not self.candidate:
            for video in self.videos:
                index = 0
                for point in video.points:
                    px,py = point
                    distance = math.sqrt( (x - px)**2 + (y - py)**2 )
                    if self.candidate is None or self.candidate[0] > distance:
                        self.candidate = (distance, index, video)
                    index += 1
        self.candidate[2].points[self.candidate[1]] = (x,y)

class Video(object):
    def __init__(self, video_capture, points=None):
        self.video_capture = video_capture
        self.points = points


def run():
    window_name = "preview"

    videos = [
        Video(cv2.VideoCapture('Test_01.mp4')),
        Video(cv2.VideoCapture('Test_01.mp4'))
    ]

    handler = MouseHandler(videos)
    
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, handler.callback)
    



    dim  = (700,858,3)
    sh,sw,d = dim

    while True:
        canvas = numpy.zeros((sh,sw,d), numpy.uint8)

        x_ = 0.0

        for video in videos:
            video_count = len(videos)
            

            ret, image = video.video_capture.read()

            if video.points is None:
                i_h, i_w, _ = image.shape

                scale = sw / video_count / i_w

                video.points = numpy.array([
                    (x_, 0.0), 
                    (x_+i_w*scale, 0), 
                    (x_+i_w*scale, i_h*scale), 
                    (x_, i_h*scale),
                ], dtype='float32')

                x_ += i_w*scale

            M = cv2.getPerspectiveTransform(
                numpy.array((
                        (0.0, 0.0), 
                        (i_w, 0), 
                        (i_w, i_h), 
                        (0, i_h),
                    ), 
                    dtype='float32'
                ),
                video.points,
            )

            image = cv2.warpPerspective(image, M, dsize=(sw,sh))
            y_offset = 0
            x_offset = 0

            canvas = cv2.addWeighted(canvas,1,image,1,0)
            #canvas[y_offset:y_offset+image.shape[0], x_offset:x_offset+image.shape[1]] = image
        
        if handler.edit:
            for video in videos:
                for p in video.points:
                    cv2.circle(canvas, tuple(p), 10, (0,0,255), -1)
        
        cv2.imshow(window_name, canvas)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyWindow(window_name)

if __name__ == '__main__':
    run()