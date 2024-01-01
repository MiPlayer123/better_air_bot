#!/usr/bin/env python

import rospy
import sys
import time
from std_msgs.msg import Float64
from std_msgs.msg import Bool
from PIL import Image,ImageDraw,ImageFont

sys.path.insert(1, '/home/mikul/git_clones/Environment_sensor_fot_jetson_nano')
import SH1106 #OLED

oled = SH1106.SH1106()
image = Image.new('1', (oled.width, oled.height), "BLACK")
draw = ImageDraw.Draw(image)
x = 0
font = ImageFont.load_default() # truetype('Font.ttc', 10) #'Font.ttc', 10

class sensor_log:
    def __init__(self):
        self.subHumid = rospy.Subscriber("/sensor_values/humidity",Float64,self.humid_callback)
        self.humid = Float64(0.0)
        self.subTemp = rospy.Subscriber("/sensor_values/temp",Float64,self.temp_callback)
        self.temp = Float64(0.0)
        self.subVoc = rospy.Subscriber("/sensor_values/voc",Float64,self.voc_callback)
        self.voc = Float64(0.0)
        self.subPm25 = rospy.Subscriber("/sensor_values/pm25",Float64,self.pm25_callback)
        self.pm25 = Float64(0.0)
        self.subPm10 = rospy.Subscriber("/sensor_values/pm10",Float64,self.pm10_callback)
        self.pm10 = Float64(0.0)

        self.subVision = rospy.Subscriber("/vision",Bool, self.vision_callback)
        self.vision = Float64(0.0)

    def humid_callback(self,data):
        self.humid = data.data
    def getHumid(self):
        return self.humid

    def temp_callback(self,data):
        self.temp = data.data
    def getTemp(self):
        return self.temp

    def voc_callback(self,data):
        self.voc = data.data
    def getVoc(self):
        return self.voc

    def pm25_callback(self,data):
        self.pm25 = data.data
    def getPm25(self):
        return self.pm25

    def pm10_callback(self,data):
        self.pm10 = data.data
    def getPm10(self):
        return self.pm10

    def vision_callback(self,data):
        self.vision = data.data
    def getVision(self):
        return self.vision

if __name__=="__main__":
    sensors = sensor_log()
    rospy.init_node('main', anonymous=True)
    blank = Image.new('1', (oled.width, oled.height), "BLACK")
    oled.display(blank)
    rospy.loginfo("Main node started")
    try:
        while not rospy.is_shutdown():
            
            #Display stuff
            draw.rectangle((0, 0, 128, 64), fill = 0)

            draw.text((0, 0), str(sensors.getTemp()), font = font, fill = 1)
            draw.text((30, 0), 'C', font = font, fill = 1)
            draw.text((50, 0), str(sensors.getHumid()), font = font, fill = 1)
            draw.text((85, 0), '%RH', font = font, fill = 1)

            draw.text((0, 15), str(sensors.getVoc()), font = font, fill = 1)
            draw.text((45, 15), 'VOCs', font = font, fill = 1)

            draw.text((0, 30), str(sensors.getPm25()), font = font, fill = 1)
            draw.text((30, 30), 'PM2.5', font = font, fill = 1)
            draw.text((65, 30), str(sensors.getPm10()), font = font, fill = 1)
            draw.text((95, 30), 'PM10', font = font, fill = 1)

            draw.text((0, 45), "Background", font = font, fill = 1)
            draw.text((65, 45), "Per: " + str(sensors.getVision()), font = font, fill = 1)

            oled.display(image)

    
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
        oled.display(blank)
        rospy.loginfo("Shutting Down")
        exit()
    print("Shutting down")
    oled.display(blank)
    exit()