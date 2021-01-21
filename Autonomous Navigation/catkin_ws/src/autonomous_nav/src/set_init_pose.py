#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf.transformations import quaternion_from_euler

rospy.init_node('set_init_pos', anonymous =True)
pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size = 1)

initpose_msg = PoseWithCovarianceStamped()
initpose_msg.header.frame_id = "map"
initpose_msg.pose.pose.position.x = 0.0
initpose_msg.pose.pose.position.y = 0.0
initpose_msg.pose.pose.position.z = 0.0

[x,y,z,w]=quaternion_from_euler(0.0,0.0,0.0)
initpose_msg.pose.pose.orientation.x = x
initpose_msg.pose.pose.orientation.y = y
initpose_msg.pose.pose.orientation.z = z
initpose_msg.pose.pose.orientation.w = w

rospy.sleep(1)
rospy.loginfo ("Setting initial pose")
print initpose_msg
pub.publish(initpose_msg)
rospy.loginfo ("Initial pose SET")
