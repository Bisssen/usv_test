from std_msgs.msg import Int16
import rospy

class trust_publisher():
    def __init__(self, parent, side):
        self.parent = parent
        self.side = side
        
        self.first_name_part = ''
        self.last_name_part = ''

        self.msg = Int16()
        self.create_publisher()

    def create_publisher(self):
        publisher_name = self.first_name_part + self.side + self.last_name_part

        self.pub = rospy.Publisher(publisher_name, Int16, queue_size=10)


    def set_trust(self, trust):
        '''
        
        '''
        # The trust input must be between -1000 and 1000
        max_size = 1000
        if trust > max_size:
            trust = max_size
        elif trust < -max_size:
            trust = -max_size

        self.msg.data = trust
        self.pub.publish(self.msg)
