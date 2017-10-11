
from Tkinter import *
import Tkinter as tk
import os
import sys
import subprocess
import socket

TCP_IP = '10.1.0.22'
TCP_PORT = 6000
BUFFER_SIZE = 200


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#s.connect((TCP_IP, TCP_PORT))



master = Tk()
master.title("Payload Ctrl")
master.geometry("205x510+0+500")
master.wm_attributes('-topmost', 1)


def coms():
#    s.send("opencoms")
#    s.close()
    s.connect((TCP_IP, TCP_PORT))
    s.send("wlan")
z = Button(master,width=20, text="Open Comms", command=coms)
z.pack()

def closecoms():
    s.send("closecoms")
    s.close()
z = Button(master,width=20, text="Close Comms", command=closecoms)
z.pack()

def liveview():
 #   s.send("Startcam")
    subprocess.Popen(['./StartUDP.sh'], shell=1)
x = Button(master,width=20, text="Start Liveview", command=liveview)
x.pack()

def liveviewpi():
    s.send("StartcamPI")
    subprocess.Popen(['./StartUDPpi.sh'], shell=1)
x = Button(master,width=20, text="Start PI camera", command=liveviewpi)
x.pack()


def liveviewRec():
    subprocess.Popen(["./StartUDPrec.sh"], shell=1)
l = Button(master,width=20, text="Start Liveview REC", command=liveviewRec)
l.pack()


def still():
    d.configure(state=NORMAL)
    d1.configure(state=NORMAL)
    d2.configure(state=NORMAL)
    d3.configure(state=NORMAL)
    c1.configure(state=DISABLED)
    s.send("stillmode")
a = Button(master, width=20, text="Still Mode", command=still)
a.pack()

def movieMode():
    d.configure(state=DISABLED)
    d1.configure(state=DISABLED)
    d2.configure(state=DISABLED)
    d3.configure(state=DISABLED)
    c1.configure(state=NORMAL)
    s.send("moviemode")
b = Button(master,width=20, text="Movie Mode", command=movieMode)
b.pack()

def startMovieRec():
    s.send("startrec")
c1 = Button(master,width=20, text="Start Movie Rec", command=startMovieRec, state=DISABLED)
c1.pack()

def stopMovieRec():
    s.send("stoprec")
c2 = Button(master,width=20, text="Stop Movie Rec", command=stopMovieRec)
c2.pack()

def actTakePicture():
    s.send("actTakePicture")
#    data = s.recv(BUFFER_SIZE)
#    print "received data:", data
d = Button(master,width=20, text="ScreenShot", command=actTakePicture, state=NORMAL)
d.pack()

def superior():
    s.send("superior")
#    data = s.recv(BUFFER_SIZE)
#    print "received data:", data
d1 = Button(master,width=20, text="Still Superior Mode", command=superior, state=NORMAL)
d1.pack()

def intel():
    s.send("intel")
#    data = s.recv(BUFFER_SIZE)
#    print "received data:", data
d2 = Button(master,width=20, text="Still Intelligent M", command=intel, state=NORMAL)
d2.pack()

def programm():
    s.send("programm")
#    data = s.recv(BUFFER_SIZE)
#    print "received data:", data
d3 = Button(master,width=20, text="Still Program WIP", command=programm, state=NORMAL)
d3.pack()


def actTakePictureHD():
#    os.system("./camera.sh setPostviewImageSize 'Original'")
    os.system("./pichd.sh") 
#d2 = Button(master, text="ScreenShot (HD)", command=actTakePictureHD)
#d2.pack()


def zoomIn():
    s.send("zoomin")
f = Button(master,width=20, text="Zoom In", command=zoomIn)
f.pack()

def zoomOut():
    s.send("zoomout")
g = Button(master,width=20, text="Zoom Out", command=zoomOut)
g.pack()

def zoomstep():
    s.send("zoomstep")
h = Button(master,width=20, text="Zoom Step/Stop", command=zoomstep)
h.pack()

var = IntVar()

def stillMode1():
    s.send("small")
i = Radiobutton(master,width=20, indicatoron = 1, variable=var, value=1, text="Still Size 2M", command=stillMode1)
i.pack()

def stillMode2():
    s.send("original") 
j = Radiobutton(master,width=20, indicatoron = 0, variable=var, value=2, text="Still Size HD", command=stillMode2)
j.pack()

def exitapp():
    s.send("zoomstep")
k = Button(master,width=20, text="Exit", command=quit)
k.pack()

#def connect():
#s.connect((TCP_IP, TCP_PORT))

mainloop()  


