from flask import Flask, render_template, Response, send_file
from camera import VideoCamera

app = Flask(__name__)
@app.route('/')
def status():
    while True:
        frame,ball = VideoCamera().get_frame()
        return render_template('index.html',ball=ball)

def gen(camera):
    while True:
        frame,detect= camera.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
#sends videofeed
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(debug=True)
