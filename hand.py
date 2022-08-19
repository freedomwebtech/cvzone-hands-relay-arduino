from cvzone.HandTrackingModule import HandDetector
import cv2
import paho.mqtt.client as mqtt



cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
count=0
def oneon():
    mqttBroker ="mqtt.fluux.io"
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("test2",(bytes('oneon','utf-8')))
def oneoff():
    mqttBroker ="mqtt.fluux.io"
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("test2",(bytes('oneoff','utf-8')))
def twoon():
    mqttBroker ="mqtt.fluux.io"
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("test2",(bytes('twoon','utf-8')))
def twooff():
    mqttBroker ="mqtt.fluux.io"
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("test2",(bytes('twooff','utf-8')))
def threeon():
    mqttBroker ="mqtt.fluux.io"
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("test2",(bytes('threeon','utf-8')))
def threeoff():
    mqttBroker ="mqtt.fluux.io"
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("test2",(bytes('threeoff','utf-8')))
def fouron():
    mqttBroker ="mqtt.fluux.io"
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("test2",(bytes('fouron','utf-8')))
def fouroff():
    mqttBroker ="mqtt.fluux.io"
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("test2",(bytes('fouroff','utf-8')))        
    
while True:
    # Get image frame
    success, img = cap.read()
    count += 1
    if count % 14 != 0:
        continue
    img=cv2.flip(img,-1) 
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw
   

    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmark points
        f = detector.fingersUp(hand1)
        one=f[0]
        two=f[1]
        three=f[3]
        four=f[4]
        
      
        if one==1:
            oneon()
          
        else:
            oneoff()
          
        if two==1:
           
            twoon()
        else:
            twooff()
        if three==1:
           threeon()
        else:
            threeoff()
        if four==1:
            fouron()
        else:
            fouroff()    

    cv2.imshow("Image", img)   
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
