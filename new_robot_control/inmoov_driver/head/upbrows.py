import time

class UpBrows():

    def __init__(self,kit):

        self.kit = kit 

        print("Initializing eye brows")

        #Initializing channels for the eye brows

        self.LEFT_UPBROW = 10
        self.RIGHT_UPBROW = 11

        
        # Adding both eyebrow angle values as tuples
        # Left Brow, Right Brow
        self.positions = {
            "center" : (75,75),   
            "up" : (100,50),
            "down" : (65,85)
        }

    def move_upbrows(self,position_name,delay=1.0):

        if position_name not in self.positions:
            print("Invalid Command!")
            return
        
        left_angle, right_angle = self.positions[position_name]

        self.kit.servo[self.LEFT_UPBROW].angle = left_angle
        self.kit.servo[self.RIGHT_UPBROW].angle = right_angle
        time.sleep(delay)
