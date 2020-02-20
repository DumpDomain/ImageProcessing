#from imutils.video import VideoStream
import numpy as np
import imutils
import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(1)
        global detect

    def __del__(self):
        self.video.release()
        
    def output():
        return detect

    
    def get_frame(self):
        while True:
            detect='NO BALL!'
            _, frame=self.video.read();
            
            hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV);
            low=np.array([25,52,72]);
            high=np.array([102,255,255]);
            
            mask=cv2.inRange(hsv,low,high);
            mask=cv2.erode(mask, None, iterations=2)
            mask=cv2.dilate(mask, None, iterations=2)
            green=cv2.bitwise_and(frame,frame,mask=mask);

            contour=cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            contour=imutils.grab_contours(contour)
            center=None
            if(len(contour)>0):
                # finding the largest contour and use it to draw an enclosing circle around the outer surface of the ball
                c=max(contour, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M=cv2.moments(c)
                center=(int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                if(radius>10):
                    # drawing outline over the ball
                    cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                
            percent_green = cv2.countNonZero(mask)/(frame.size/3)
            if(percent_green!=0):
                detect='GREEN BALL!'
            #print('Percentage Green:', np.round(percent_green*100, 2))
            #cv2.imshow("Ball Track", frame)
            
            
            #cv2.imshow("Green",green);
            key=cv2.waitKey(1)
            if(key==27):
                cv2.destroyAllWindows();
                break;

            ret, jpeg = cv2.imencode('.jpg', frame)
            # self.output(a)
            return jpeg.tobytes(),detect
