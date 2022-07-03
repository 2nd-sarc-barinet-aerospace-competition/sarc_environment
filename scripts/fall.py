#!/usr/bin/python3

import rospy
import rosnode
import math

from mrs_msgs.msg import UavManagerDiagnostics as UavManagerDiagnostics
from mavros_msgs.srv import CommandBool as CommandBool
from std_srvs.srv import Trigger as Trigger
from gazebo_msgs.srv import DeleteModel, DeleteModelRequest



class Activator:
    
    def callback(self, data):

        dele = DeleteModelRequest()
        dele.model_name = "SARckc_floor"
        self.delete(dele)
        rospy.loginfo('arming')
        self.arm(1)
        rospy.loginfo('activating')
        self.activate()
        rospy.signal_shutdown("yes")

    def __init__(self):

        rospy.init_node('activator', anonymous=True)

        uav_name = "uav1"
        self.delete = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)
        self.subscriber = rospy.Subscriber('/' + uav_name + '/uav_manager/diagnostics', UavManagerDiagnostics, self.callback)
        self.arm = rospy.ServiceProxy('/' + uav_name + '/mavros/cmd/arming', CommandBool)
        self.activate = rospy.ServiceProxy('/' + uav_name + '/uav_manager/midair_activation', Trigger)

        rospy.loginfo('initialized')
        rospy.spin()

if __name__ == '__main__':
    try:
        node_crash_checker = Activator()
    except rospy.ROSInterruptException:
        pass
