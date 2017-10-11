#!/usr/bin/env python
import json
import requests
import numpy as np
from Tkinter import *
import os
import sys
import Tkinter as tk
import socket
import re
import subprocess
#master = Tk()

TCP_IP = '10.1.0.22'
TCP_PORT = 6000
BUFFER_SIZE = 40  
still = True




def get_payload(method, params):
    return {
	"method": method,
	"params": params, 
        "id": 1,
	"version": "1.0"
    }

def get_payloadzi(method):
    return {
	"method": method,
	"params": ["in","start"], 
        "id": 1,
	"version": "1.0"
    }

def get_payloadzo(method):
    return {
	"method": method,
	"params": ["out","start"], 
        "id": 1,
	"version": "1.0"
    }
        
def get_payloadzs(method):
    return {
	"method": method,
	"params": ["in","1shot"], 
        "id": 1,
	"version": "1.0"
    }
               
        
def take_picture():
    payload = get_payload("actTakePicture", [])
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://10.0.0.1:10000/sony/camera', data=json.dumps(payload), headers=headers)
    url = response.json()['result']
    strurl = str(url[0][0])
#    datas = json.PARSE(ARGF.read)
#    print datas
    #os.system("grep -Eo '(https?|ftp|file)://[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*[-A-Za-z0-9\+&@#/%=~_|]'`")
    #os.system("wget -O Pictures/Snapshot-`date +%Y-%m-%d-%H%M%S`.jpeg")
    #urls = re.findall('http[s]://[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*[-A-Za-z0-9\+&@#/%=~_|]', data)
    #print urls
    return strurl


def startrec():
    payload = get_payload("startMovieRec", [])
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://10.0.0.1:10000/sony/camera', data=json.dumps(payload), headers=headers)
    url = response.json()['result']
    strurl = str(url[0][0])
    data = response.json()
    print data
    return strurl

def stoprec():
    payload = get_payload("stopMovieRec", [])
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://10.0.0.1:10000/sony/camera', data=json.dumps(payload), headers=headers)
    url = response.json()['result']
    strurl = str(url[0][0])
    data = response.json()
    print data
    return strurl

def moviemode():
    payload = get_payload("setShootMode", ["movie"])
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://10.0.0.1:10000/sony/camera', data=json.dumps(payload), headers=headers)
    data = response.json()
    print data


def stillmode():
    payload = get_payload("setShootMode", ["still"])
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://10.0.0.1:10000/sony/camera', data=json.dumps(payload), headers=headers)
    data = response.json()
    print data

def zoomin():
    payload = get_payloadzi("actZoom")
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://10.0.0.1:10000/sony/camera', data=json.dumps(payload), headers=headers)
    data = response.json()
    print data

def zoomout():
    payload = get_payloadzo("actZoom")
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://10.0.0.1:10000/sony/camera', data=json.dumps(payload), headers=headers)
    data = response.json()
    print data

def zoomstep():
    payload = get_payloadzs("actZoom")
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://10.0.0.1:10000/sony/camera', data=json.dumps(payload), headers=headers)
    data = response.json()
    print data

#def startcam():
#    subprocess.Popen(['./Startcam.sh'], shell=True)
#    os.system("./Startcam.sh")

def spi():
    os.system("/home/pi/Prj/SonyCtrl/./StartcamPI.sh &")

def small():
    os.system("./picsd.sh &")

def original():
    os.system("./pichd.sh &")    

def wlan():
    os.system("sudo ifup --force wlan0")

    
def close():
    conn.close()


    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if data == "actTakePicture" and still == True:
        take_picture()
    if data == "actTakePicture" and still == False:
        conn.send("Error")       
    if data == "stillmode":
        stillmode()
        still = True
    if data == "moviemode":
        moviemode()
        still = False
    if data == "zoomin":
        zoomin()     
    if data == "zoomout":
        zoomout()
    if data == "zoomstep":
        zoomstep()         
    if data == "close":
        close()
    if data == "startrec":
        startrec()
    if data == "stoprec":
        stoprec()          
    if data == "close":
        close()
    if data == "Startcam":
        startcam()    
    if data == "original":
        original()   
    if data == "small":
        small()
    if data == "StartcamPI":
        spi()
    if data == "wlan":
        wlan()
    
#conn.close()

mainloop()
