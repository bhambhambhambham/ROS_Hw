#!/usr/bin/env python3
# In the first terminal, rosrun hw Hw1_Draw.py
# In another terminal, rviz : Add path and change the topic to /Topic

# roslaunch hw hw1launch.launch

import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path
import math
ll = []
global readytobeshutdown

pubpath = rospy.Publisher("Topic", Path, queue_size = 1000)
def getpose():
    rospy.init_node("getpose", anonymous=True)
    print("Ready")
    rospy.Subscriber("/move_base_simple/goal", PoseStamped, callback)
    rospy.spin()

def callback(data):
    global first
    global distance
    global readytobeshutdown
    path = Path()
    posepose = PoseStamped()
    posepose = data

    if len(ll)>0:
        distance = math.sqrt((first.pose.position.x-data.pose.position.x)**2+(first.pose.position.y-data.pose.position.y)**2+(first.pose.position.z-data.pose.position.z)**2)
        print(distance)
        if distance < 0.5 :
            ll.append(posepose)
            ll.append(first)
            readytobeshutdown = True

        else : 
            ll.append(posepose)
            readytobeshutdown = False
    else: 
        ll.append(posepose)
        first = ll[0]
        readytobeshutdown = False
        
    path.poses = ll
    path.header.frame_id = "map"
    pubpath.publish(path)

    if readytobeshutdown == True:
        rospy.signal_shutdown("Done")

if __name__ == "__main__":
    getpose()