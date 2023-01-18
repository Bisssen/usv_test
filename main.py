import rospy
import tkinter as tk

from src.gui import gui
from src.node import usv_control_node

# The broad rate must be the same, is 250 kw ? 

class mission():
    def __init__(self):
        self.node = usv_control_node(self)
        self.root = tk.Tk()
        self.gui = gui(self.root)
        
        self.old_angle_left = None
        self.old_angle_right = None

if __name__ == "__main__":
    mis = mission()
    rate = rospy.Rate(10)
    
    
    while not rospy.is_shutdown():

        try:
            mis.root.update()
        except tk.TclError:
            break
        # Get the values from the gui
        left_trust = mis.gui.left_trust_scale.get()
        right_trust = mis.gui.right_trust_scale.get()
        
        left_angle = mis.gui.left_angle_scale.get()
        right_angle = mis.gui.right_angle_scale.get()        

        # Update the ros topic
        mis.node.left_trust.set_trust(left_trust)
        mis.node.right_trust.set_trust(right_trust)
        
        # Only update the angle, when the command changes
        if mis.old_angle_left is not None:
            if not mis.old_angle_left == left_angle:
                mis.node.left_angle.set_angle(left_angle)
        
            if not mis.old_angle_right == right_angle:
                mis.node.right_angle.set_angle(right_angle)
        
        mis.old_angle_left = left_angle
        mis.old_angle_right = right_angle
        

        # Keep the rate of the loop
        rate.sleep()
        

