from std_msgs.msg import Float32
import rospy

class angle_publisher():
    def __init__(self, parent, side):
        self.parent = parent
        self.side = side
        
        self.first_name_part = '/workshop_setup/pod_steer/'
        self.last_name_part = '_steer'

        self.msg = Float32()
        self.create_publisher()

    def create_publisher(self):
        publisher_name = self.first_name_part + self.side + self.last_name_part

        self.pub = rospy.Publisher(publisher_name, Float32, queue_size=10)


    def set_angle(self, angle):
        '''
        
        '''
        # The trust input must be between -1000 and 1000
        max_size = 89.9
        if angle > max_size:
            angle = max_size
        elif angle < -max_size:
            angle = -max_size

        self.msg.data = angle
        self.pub.publish(self.msg)
