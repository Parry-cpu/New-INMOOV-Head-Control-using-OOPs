import time
class Cheeks():

    def __init__(self,kit):

        self.kit = kit
        
        print("Initializing cheeks")

        #Intializng channels for the cheesk

        self.LEFT_CHEEK = 12
        self.RIGHT_CHEEK = 13

        #The lower values need to be adjusted accordingly
        self.positions = {
            "center":(100,80),
            "up":(80,100),
            "down":(120,60)
        }

    
    def move_cheeks(self,position_name,delay = 1.0):

        if position_name not in self.positions:
            print("Invalid Command!")
            return
        
        left_angle,right_angle = self.positions[position_name]

        self.kit.servo[self.LEFT_CHEEK].angle = left_angle
        self.kit.servo[self.RIGHT_CHEEK].angle = right_angle
        time.sleep(delay)