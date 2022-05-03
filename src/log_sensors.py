#!/usr/bin/env python

import rospy
import sys
from std_msgs.msg import Float64
import time
from datetime import datetime

filename = 'sensor_log.txt'

def callback_receive_data(msg):
    #rospy.loginfo(msg)
    f = open(filename, "a")
    f.write("{0} {1}\n".format(datetime.now().strftime("%H:%M"), msg))
    f.close()
    time.sleep(300)

class sensor_log:
    def __init__(self):
        self.sub = rospy.Subscriber("/sensor_values/humidity",Float64,self.callback)
        self.i=0
        self.filename = 'sensor_log.txt'

    def callback(self,data):
        f = open(self.filename, "a")
        f.write("{0} {1} {2}\n".format(datetime.now().strftime("%H:%M"), self.i, data))
        f.close()
        rospy.loginfo(data)
        time.sleep(300)
        self.i=self.i+5

class sensor_log2:
    def __init__(self):
        self.sub = rospy.Subscriber("/sensor_values/pm25",Float64,self.callback)
        self.i=0
        self.filename = 'pm25_log.txt'

    def callback(self,data):
        f = open(self.filename, "a")
        f.write("{0} {1} {2}\n".format(datetime.now().strftime("%H:%M"), self.i, data))
        f.close()
        rospy.loginfo(data)
        time.sleep(300)
        self.i=self.i+5

class sensor_log3:
    def __init__(self):
        self.sub = rospy.Subscriber("/sensor_values/pm10",Float64,self.callback)
        self.i=0
        self.filename = 'pm10_log.txt'

    def callback(self,data):
        f = open(self.filename, "a")
        f.write("{0} {1} {2}\n".format(datetime.now().strftime("%H:%M"), self.i, data))
        f.close()
        rospy.loginfo(data)
        time.sleep(300)
        self.i=self.i+5


if __name__=="__main__":
    obc = sensor_log3()
    rospy.init_node('sensor_log3', anonymous=True)

    # sub = rospy.Subscriber("/sensor_values/humidity", Float64, callback_receive_data)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
