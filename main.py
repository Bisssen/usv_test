from turtle import left
import rospy
import tkinter as tk
import time

from src.gui import gui
from src.node import usv_control_node

# The broad rate must be the same, is 250 Kbps
# slcanUp -> roslaunch mbzirc_cat_bringup mbzirc_cat.launch can_port:=your_preferred_can_port



class mission():
    def __init__(self):
        self.node = usv_control_node(self)
        self.root = tk.Tk()
        self.gui = gui(self.root)
        
        self.old_angle_left = None
        self.old_angle_right = None

if __name__ == "__main__":
    mis = mission()
    rate = rospy.Rate(7)
    
    
    while not rospy.is_shutdown():

        try:
            mis.root.update()
        except tk.TclError:
            break
        # Get the values from the gui
        left_trust = mis.gui.left_trust_scale.get()
        # right_trust = mis.gui.right_trust_scale.get()
        
        left_angle = mis.gui.left_angle_scale.get()
        # right_angle = mis.gui.right_angle_scale.get()        

        # Update the ros topic
        mis.node.left_trust.set_trust(left_trust)
        if mis.gui.r_mode:
            mis.node.right_trust.set_trust(-left_trust)
        else:
            mis.node.right_trust.set_trust(left_trust)
        
        # Only update the angle, when the command changes
        # Best if maac 60 degreses
        if mis.old_angle_left is not None:
            if not mis.old_angle_left == left_angle:
                mis.node.left_angle.set_angle(left_angle)
                mis.node.right_angle.set_angle(-left_angle)
        
            # if not mis.old_angle_right == right_angle:
                # mis.node.right_angle.set_angle(right_angle)
        
        mis.old_angle_left = left_angle
        # mis.old_angle_right = right_angle
        
        break_now = False
        for i in range(12):
            try:
                mis.root.update()
            except tk.TclError:
                break_now = True
                break
            time.sleep(0.01)
        if break_now:
            break
    
        # Keep the rate of the loop
        rate.sleep()
        

