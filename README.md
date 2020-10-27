# ImageProcessing
# Green Ball Detection and Percentage Calculation:
The webpage streams the video from a webcam or external camera and detects the presence of a green ball and calculates its percentage

## Libraries Used:
* opencv
* numpy
* imutils
* flask
* serial

## Installing the above packages using 'pip' :
open your terminal and run the following commands,
* pip install opencv-python
* pip install numpy
* pip install imutils
* pip install Flask
* pip install pyserial

## To run this on your computer :
* download the folder in your pc
* open the terminal and change the path to the path where this folder is stored 
* for example "cd D:\Ball track"
* enter the command 'python main.py' in your terminal
* copy the link generated and paste it in a browser to open your localhost for the video stream

## Video Capture :
* The default device to capture video is the webcam and is accessed by cv2.VideoCapture(0) for external camera change 0 to 1

## Processing:

Import opencv,numpy,imutils,flask. Run an infinite loop. Inside the loop define frame using cv2.VideoCapture(0)(0 for webcam and 1 for external camera). Create two arrays using numpy to store the upper and lower limit of the green colour. Next is to convert it to hsv by using cv2.cvtColor() and pass the parameter cv2.COLOR_BGR2HSV to convert the colour format. Then, mask it to get just the green colour using cv2.inRange(hsv,x,y) where x and y are the lower and upper limits respectively.

Use cv2.erode() and cv2.dilate() to reduce the excess white noise but retain its original structure. cv2.bitwise_and() is used to mask the frame with the mask which consists of only the green colour.

Next is to find the contours using cv2.findContours(). findContours() changes the variable passed as a parameter so mask.copy() is used to prevent any changes to the original mask. cv2.RETR_EXTERNAL keeps the surroundings of the green ball instead of discarding it and cv2.CHAIN_APPROX_SIMPLE approximates the contour. Next, using imutils we have grab_contours() to extract the contours. If the contour length is non-zero then we find the maximum contour and store it. Then, using moments we determine the center and draw the circle. Then we calculate the green percentage by dividing the area of green by the total area of frame. 
  
