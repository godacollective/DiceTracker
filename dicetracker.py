import argparse

parser = argparse.ArgumentParser() 
parser.add_argument("-t", "--threshold", help = "type threshold lower and upper arguments as '127 255'", 
default = "127 255", type = str)
parser.add_argument("-osc", "--osc", help = "type osc ip adress and channel as '127.0.0.1 5005'", 
default = "127.0.0.1 5005", type = str)
args = parser.parse_args()

import numpy as np
import cv2

from pythonosc import osc_message_builder
from pythonosc import udp_client

#display a video
cap = cv2.VideoCapture('test.mp4')

kernel = np.ones((3,3), np.uint8)

while(1):
    ret, frame = cap.read()

    try:
        #convert BGR to HSV
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        thresargs = args.threshold.split()
        ret,thres = cv2.threshold(gray,int(thresargs[0]),int(thresargs[1]),cv2.THRESH_BINARY)
        erosion = cv2.erode(thres, kernel, iterations=1)
        
        im,contours,hierarchy = cv2.findContours(erosion, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        
        cv2.drawContours(frame, contours, -1, (1,0,255), 2)

        try:
            parents = []
            for idx, i in enumerate(hierarchy[0]):
                peri = cv2.arcLength(contours[idx], True) 
                approx = cv2.approxPolyDP(contours[idx], 0.04*peri, True)
                if len(approx) == 4: 
                    (x, y, w, h) = cv2.boundingRect(approx) 
                    ar = w / float(h)
                if ar >= 0.95 and ar <= 1.05 and i[3] == -1: 
                    parents.append(idx)
            #print (parents)
                    
            total = [0] * len(parents)
            
            for idx, i in enumerate(parents):
                for p in hierarchy[0]:
                    if p[3] == i:
                        total[idx] += 1
            print (total)

            osc = args.osc.split()
            ip = osc[0]
            port = osc[1]
            client = udp_client.SimpleUDPClient(ip, port)
            client.send_message("/dice", total)
        except:
            pass
        
        cv2.imshow('frame',frame)

    except:
        print ("END")
        break

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        print ("EXIT")
        break
    
cv2.destroyAllWindows()
