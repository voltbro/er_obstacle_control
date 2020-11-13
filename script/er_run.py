#!/usr/bin/env python3

import rospy
import random

from er_obstacle_control.srv import Er, ErRequest, ErResponse

rospy.init_node('er_service_node')

def er_resp(req):
    resp = ErResponse()
    if req.er_event_request == 1:
         if random.randint(0,1) == 1:
             resp.resp = "l"
         else:
             resp.resp = "O"
    else:
        resp.resp = "2"
    return resp

rospy.loginfo('Er service ready')
e = rospy.Service('er_obstacle_control', Er, er_resp)
rospy.spin()

