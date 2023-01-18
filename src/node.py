# from rclpy.node import Node # Ros 2
import rospy

from .trust_publisher import trust_publisher
from .angle_publisher import angle_publisher

class usv_control_node():
    def __init__(self, parent):
        self.parent = parent
        # super().__init__('boat_node')  # For logging purpose I think
        rospy.init_node('usv_control', anonymous=True)
       
       
        self.left_trust = trust_publisher(self.parent, 'left')
        self.right_trust = trust_publisher(self.parent, 'right')
        
        self.left_angle = angle_publisher(self.parent, 'left')
        self.right_angle = angle_publisher(self.parent, 'right')
       

