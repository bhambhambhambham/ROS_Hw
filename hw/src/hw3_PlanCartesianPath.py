#!/usr/bin/env python3
# roslaunch hw hw3launch.launch

import rospy
import copy
import moveit_commander
from geometry_msgs.msg import PoseStamped , Pose

waypoints = []
move_group = moveit_commander.MoveGroupCommander("panda_arm")

def plan_cartesian_path(data:PoseStamped):
    global x
    global waypoints
    wpose = Pose()
    wpose.position = data.pose.position
    wpose.position.z = 0.5
    waypoints.append(copy.deepcopy(wpose))

    (plan,fraction) = move_group.compute_cartesian_path(waypoints, 0.01, 0.0)
    print("Planned")
    print(len(waypoints))

    if len(waypoints)<x:
        pass
    else:
        move_group.execute(plan, wait=True)
def cartesianplan():
    global x
    rospy.init_node("cartesian_plan_and_execute", anonymous=True)
    x = int(input("Input amount of points here : "))
    print("Ready")
    rospy.Subscriber("/goal", PoseStamped, plan_cartesian_path)
    rospy.spin()

if __name__ == "__main__":
    cartesianplan()