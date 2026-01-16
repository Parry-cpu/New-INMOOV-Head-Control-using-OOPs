import time

class Jaw():

    def __init__(self,kit):

        self.kit = kit 

        print("Initializing Jaw")

        #Initializing channels for the jaw

        self.JAW = 15

        #Adding a flag to set the default poaition of the jaw i.e closed

        self.set_position = "close"

        
        # Adding both eyebrow angle values as tuples
        # Left Brow, Right Brow
        self.positions = {
            "open":70,
            "close":0
        }

    def move_jaw(self,position_name,delay=0.5):
        
        if position_name not in self.positions:
            print("Invalid Command!")
            return
        
        jaw_angle = self.positions[position_name]

        if self.set_position != position_name:
            self.kit.servo[self.JAW].angle = jaw_angle
            time.sleep(delay)
            self.set_position = position_name
            print(f"Jaw {position_name}ed ")
        else:
            print(f" Jaw already {position_name}")

    def set_jaw_angle(self,angle):
        if 0<= angle <= 180:
            self.kit.servo[self.JAW].angle = angle
            print(f"Jaw set to {angle}")
        else:
            print("Invalid angle! Must be between 0 and 180")