# Web streaming example
# Source code from the official PiCamera package
# http://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming

import os
import io
import picamera
import logging
import socketserver
import RPi.GPIO as GPIO
import time
import threading
from threading import Condition
from http import server

PAGE="""
<html>
<head>
<title>Raspberry Pi - Surveillance Camera</title>

<center><h1>Raspberry Pi - Surveillance Camera</h1></center>

<center><img src="stream.mjpg" width="640" height="480"></center><br>
<style>

.button {

  background-color: #4CAF50; /* Green */

  border: none;

  color: white;

  padding: 10px 16px;

  text-align: center;

  text-decoration: none;

  display: inline-block;

  font-size: 16px;

  margin: 4px 2px;

  cursor: pointer;

}





.button1 {

  background-color: white; 

  color: black; 

  border: 2px solid #4CAF50;

}



.button2 {

  background-color: white; 

  color: black; 

  border: 2px solid #008CBA;

}

</style>
<form action="/Auto">
    <center><button type="submit" value = "1" class="button button1">Auto Mode</button></center>
</form>

<form action="/Hand">
    <center><button type="submit" value = "1" class="button button2">Hand Mode</button></center>
</form>

</body>

</html>
"""


Auto_PAGE="""
<html>
<head>
<title>Raspberry Pi - Surveillance Camera</title>
</head>

<body>

<style>

.button {

  background-color: #4CAF50; /* Green */

  border: none;

  color: white;

  padding: 10px 16px;

  text-align: center;

  text-decoration: none;

  display: inline-block;

  font-size: 16px;

  margin: 4px 2px;

  cursor: pointer;


}

</style>

<center><h1>Raspberry Pi - Surveillance Camera</h1></center>

<center><img src="stream.mjpg" width="640" height="480"></center><br>

<center><text>Auto Mode is Runing</text></center><br>

<form action="/index.html">

    <center><button type="submit" class="button">Back</button></center>
    
</form>

</body>

</html>

"""

Hand_PAGE="""\
<html>
<head>
<title>ITD102 Mini Project : Manual Mode Servo CCTV</title>
</head>
<body>

​
<style>

.button {

  background-color: #4CAF50; /* Green */

  border: none;

  color: white;

  padding: 10px 16px;

  text-align: center;

  text-decoration: none;

  display: inline-block;

  font-size: 16px;

  margin: 4px 2px;

  cursor: pointer;

  float: left;

  margin-left: 20%;

}

​

.button1 {

  background-color: white; 

  color: black; 

  border: 2px solid #4CAF50;

}

​

.button2 {

  background-color: white; 

  color: black; 

  border: 2px solid #008CBA;

}

​

.button3 {

  background-color: white; 

  color: black; 

  border: 2px solid #f44336;

}

​

</style>

​

<center><h1>Raspberry Pi - Surveillance Camera</h1></center>

<center><img src="stream.mjpg" width="640" height="480"></center>

<center><text>Hand Mode is Runing</text></center>

<center><text>Now is toward to  degree</text></center>

<form action="/Hand">

    <center>Input : <input type="text" name = "Angle"></center><br>

    <center><button type="submit" class="button button1">Yes</button></center>

</form>

<form action="/Hand">

    <center><button type="submit" class="button button2">Reset</button></center>

</form>

<form action="/index.html">

    <center><button type="submit" class="button button3">Back</button></center>

</form>

</body>

</html>


"""
class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)
-
class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

class StreamingHandler(server.BaseHTTPRequestHandler):
    def methods(self,PAGE):
        content = PAGE.encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(content))
        self.end_headers()
        self.wfile.write(content)


if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif '/Auto?' == self.path:
            global Mode
            self.methods(Auto_PAGE)
            Mode = 0
        elif '/Hand?' in self.path:
            global Mode
            Mode = 1
            Angle = self.path.replace("/Hand","")
            Angle = Angle.replace("?","")
            Angle = Angle.replace("Angle=","")
            s = Angle
            if Angle == "":
                Angle = 0

            if s.isdecimal() == False:
                New_Hand_PAGE = Hand_PAGE.replace("Now is toward to  degree","You must enter the integer to control")

            else:

                New_Hand_PAGE = Hand_PAGE[:899] + str(Angle ) + Hand_PAGE[899:]
            self.methods(New_Hand_PAGE)
            InputValue = str(Angle)
        elif '/index.html' in self.path:

            global Mode
            global InputValue
            InputValue = "q"
            Mode = -1
            self.methods(PAGE)

        elif '/stream.mjpg' == self.path:
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; bounda$
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                            self.end_headers()
                    self.wfile.write(frame)



            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:

            self.send_error(404)
            self.end_headers()
##########
class Auto_Mode:
    def Main(self):
        global Mode
        while True:
            for index in range(5,91,5):
                if Mode == -1:
                    break
                dc = 7.5 + DC.Calculate(index)

                p.ChangeDutyCycle(dc)
                time.sleep(0.5)
            for index in range(5,91,5):
                if Mode == -1:
                    break
                dc = 12.5 - DC.Calculate(index)
                p.ChangeDutyCycle(dc)
                time.sleep(0.5)
            for index in range(5,91,5):
                if Mode == -1:
                    break

                dc = 7.5 - DC.Calculate(index)
                p.ChangeDutyCycle(dc)
                time.sleep(0.5)
            for index in range(5,91,5):
                if Mode == -1:
                    break
                dc = 2.5 + DC.Calculate(index)
                p.ChangeDutyCycle(dc)
                time.sleep(0.5)

            if Mode == -1:

                p.ChangeDutyCycle(7.5)
                break
class Manual_Mode:

    def Main(self):
        global InputValue
        InputValue = ""
        while True:
            if InputValue == "q" or InputValue == "Q":
                os.system('clear')
                 break
            else:
                if self.Check_Error():
                    pass
                else:
                    self.dc = 7.5 - DC.Calculate(float(InputValue))
                    try:
                        p.ChangeDutyCycle(self.dc)
                    except KeyboardInterrupt:
                        p.stop()
                        GPIO.cleanup()
                    os.system('clear')

                    break



    def Check_Error(self):

        Error = False
        if Check_Input.Number(InputValue,float):
            if float(InputValue) < -90 or float(InputValue) > 90:
                Error = True
        else:

            Error = True

        return Error






        ####Manual mode motor code####


class DC:

    def Calculate(Angle):
        dc = 5 * (Angle / 90)
        return dc


##########
class Check_Input:



    def Number(Input,type):
        try:
            type(Input)
        except ValueError:
            return False
        else:
            return True


#####Run in Mode#####


def Main():
    global Mode
    Mode = -1
    while True:
        #Mode_Select().Main()
        if Mode == 0:
            Auto_Mode().Main() ###Auto mode methods
        elif Mode == 1:
            print("Manual_Mode successful")
            Manual_Mode().Main()
        elif Mode == "Exit":


            os.system('clear')
            break

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(7.5) # Initialization



with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    output = StreamingOutput()
    #Uncomment the next line to change your Pi's Camera rotation (in degrees)
    #camera.rotation = 90
    camera.start_recording(output, format='mjpeg')
    try:
        t1 = threading.Thread(target = Main)
        t1.start()
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)

        server.serve_forever()
    finally:
        camera.stop_recording()




