#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped , PoseArray , Pose
pub = rospy.Publisher("Pose_Array", PoseArray, queue_size=1000)
poseposearray = PoseArray()
def callback(data:PoseStamped):
    global poseposearray
    posepose = Pose()
    posepose = data.pose
    posepose.position.z = 0.5

    poseposearray.header = data.header
    poseposearray.poses.append(posepose)
    print(len(poseposearray.poses))
    pub.publish(poseposearray)
    
def getpose():
    rospy.init_node("Pose_Array", anonymous=True)
    rospy.Subscriber("/goal", PoseStamped, callback)
    rospy.spin()

if __name__ == "__main__":
    getpose()