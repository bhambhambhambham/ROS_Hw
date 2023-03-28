#!/usr/bin/env python3
# roslaunch hw hw2launch.launch

import rospy
import moveit_commander
from geometry_msgs.msg import PoseStamped , Pose
# from moveit_commander.conversions import pose_to_list

move_group = moveit_commander.MoveGroupCommander("panda_arm")

def movetogoal():
    rospy.init_node("planner", anonymous=True)
    rospy.Subscriber("/goal", PoseStamped, callback)
    rospy.spin()

def callback(data:PoseStamped):
    global pose_goal
    pose_goal = Pose()
    pose_goal = data.pose
    pose_goal.position.z = 0.5
    
    move_group.set_pose_target(pose_goal)
    success = move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()

if __name__ == "__main__":
    movetogoal()