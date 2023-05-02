import tkinter as tk

class gui:
    def __init__(self, master):
        self.master = master
        self.master.geometry('600x600')
        
        self.left_trust_text_variable, self.left_trust_image,\
        self.left_trust_label =\
            self.generate_text_box((0.5, 0.1), 'Left trust')
        self.left_trust_scale =\
            self.generate_slider((0.5, 0.18), -1000, 1000, 0, 250)
                
        # self.right_trust_text_variable, self.right_trust_image,\
        # self.right_trust_label =\
        #     self.generate_text_box((0.5, 0.3), 'Right trust')
        # self.right_trust_scale =\
        #     self.generate_slider((0.5, 0.38), -250, 250, 0, 50)
        
        
        self.left_angle_text_variable, self.left_angle_image,\
        self.left_angle_label =\
            self.generate_text_box((0.5, 0.6), 'Left angle')
        self.left_angle_scale =\
            self.generate_slider((0.5, 0.68), -90, 90, 0, 10)

        # self.right_angle_text_variable, self.right_angle_image,\
        # self.right_angle_label =\
        #     self.generate_text_box((0.5, 0.8), 'Right angle')
        # self.right_angle_scale =\
        #     self.generate_slider((0.5, 0.88), -90, 90, 0, 10)
            
        self.master.bind('a', self.a)
        self.master.bind('w', self.w)
        self.master.bind('d', self.d)
        self.master.bind('s', self.s)
        self.master.bind('m', self.m)
        self.master.bind('r', self.r)
        
        self.speed = 0
        self.angle = 0
        self.r_mode = False

    def r(self, event):
        self.speed = 0
        self.angle = 0
        self.left_angle_scale.set(self.angle)
        self.left_trust_scale.set(self.speed)
        self.r_mode = not self.r_mode

    def m(self, event):
        self.speed = 0
        self.angle = 0
        self.left_angle_scale.set(self.angle)
        self.left_trust_scale.set(self.speed)
        
    def d(self, event):
        self.angle += 5
        if self.angle > 89.9:
            self.angle = 89.9
        self.left_angle_scale.set(self.angle)
    
    def a(self, event):
        self.angle -= 5
        if self.angle < -89.9:
            self.angle = -89.9
        self.left_angle_scale.set(self.angle)
    
    def w(self, event):
        self.speed += 10
        if self.speed > 1000:
            self.speed = 1000
        self.left_trust_scale.set(self.speed)
    
    
    def s(self, event):
        self.speed -= 10
        if self.speed < -1000:
            self.speed = -1000
        self.left_trust_scale.set(self.speed)
    

    def generate_text_box(self, position, default_text):
        x, y = position
        text_variable = tk.StringVar()
        text_variable.set(default_text)
        label_image = tk.Label(self.master,
                               borderwidth = 0)
        label_image.place(relx = x,
                          rely = y,
                          anchor = 'center')
        label_text = tk.Label(self.master,
                              textvariable=text_variable,
                              borderwidth = 0)
        label_text.place(relx = x,
                         rely = y,
                         anchor = 'center')
        return text_variable, label_image, label_text

    def generate_slider(self, position, range_start, range_end, default_value=0,
                        tickinterval=250):
        x, y = position
        scale = tk.Scale(self.master, from_=range_start, to=range_end,
                         length=500, tickinterval=tickinterval,
                         orient=tk.HORIZONTAL)
        scale.set(default_value)
        scale.place(relx = x,
                    rely = y,
                    anchor = 'center')
        return scale