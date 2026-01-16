import time

class UpperLip():

    def __init__(self,kit):

        self.kit = kit 

        print("Initializing Jaw")

        #Initializing channels for the jaw

        self.LIP = 10  #This is an extra part

        #Adding a flag to set the default poaition of the jaw i.e closed

        self.set_position = "down"

        
        # Adding both eyebrow angle values as tuples
        # Left Brow, Right Brow
        self.positions = {
            "up":20,
            "down": 0,
            "angle_1":12,
            "angle_2":15
        }

    def move_lip(self,position_name,delay=0.5):
        
        if position_name not in self.positions:
            print("Invalid Command!")
            return
        
        lip_angle = self.positions[position_name]

        if self.set_position != position_name:
            self.kit.servo[self.LIP].angle = lip_angle
            time.sleep(delay)
            self.set_position = position_name
            print(f"Lip {position_name} ")
        else:
            print(f"Lip already {position_name}")