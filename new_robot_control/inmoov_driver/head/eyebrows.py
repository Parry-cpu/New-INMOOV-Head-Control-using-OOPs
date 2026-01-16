import time

class EyeBrows():

    def __init__(self,kit):

        self.kit = kit 

        print("Initializing eye brows")

        #Initializing channels for the eye brows

        self.LEFT_BROW = 0
        self.RIGHT_BROW = 1

        
        # Adding both eyebrow angle values as tuples
        # Left Brow, Right Brow
        self.positions = {
            "center" : (75,75),   
            "up" : (55,95),
            "down" : (120,30)
        }

    def move_brows(self,position_name,delay=1.0):

        if position_name not in self.positions:
            print("Invalid Command!")
            return
        
        left_angle, right_angle = self.positions[position_name]

        self.kit.servo[self.LEFT_BROW].angle = left_angle
        self.kit.servo[self.RIGHT_BROW].angle = right_angle
        time.sleep(delay)
