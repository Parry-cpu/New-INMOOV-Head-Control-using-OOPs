import time

class Eyes:

    def __init__(self,kit):

        """
        Constructor to initialize all the Head objects
        'kit is pre-initialized ServoKit object
        """

        self.kit = kit #Store the kit object for this instance this contiains the address, i2c and channel values

        #Initializing attributes for eyes
        print("Initializing Eyes...")

        #---- Initializing the channels for the Servo Mortos connected to the PCA

        # --- Left Eye Channels ---
        self.left_upper_lid = 2
        self.left_eye_up_down = 3
        self.left_eye_left_right = 4
        self.left_lower_lid = 5

                    # --- Left eye servo angle values ----#
                    #They are subjected to change and needs to be adjusted

        # ---- Left Eye lids ---- #
        self.L_LID_OPEN_UPPER = 55
        self.L_LID_OPEN_LOWER = 135
        self.L_LID_CLOSE = 85

        # ---- Left Eyeball up down and center ----#
        self.L_EYE_UP = 25
        self.L_EYE_DOWN = 75
        self.L_EYE_CENTER_UD = 45

        # ---- Left Eyeball left right and center ----#

        self.L_EYE_LEFT = 75
        self.L_EYE_RIGHT = 45
        self.L_EYE_CENTER_LR = 60


        
        # --- Right Eye Channels ---#
        
        self.right_upper_lid = 6
        self.right_eye_up_down = 7
        self.right_eye_left_right = 8
        self.right_lower_lid = 9

                     # ---- Right eye servo angle values ----#

        # ---- Left Eye lids ---- #
        self.R_LID_OPEN_UPPER = 85
        self.R_LID_OPEN_LOWER = 120
        self.R_LID_CLOSE = 70

        # ---- Left Eyeball up down and center ----#
        self.R_EYE_UP = 80
        self.R_EYE_DOWN = 50
        self.R_EYE_CENTER_UD = 65

        # ---- Left Eyeball left right and center ----#

        self.R_EYE_LEFT = 60
        self.R_EYE_RIGHT = 35
        self.R_EYE_CENTER_LR = 45


        #Making a dictonary to save all the commands

        #left eye , right eye

        dictionary = {}

    
    # ---- Methods for controlling motions of the eyes ----#

    def open_eyes(self):

        #Left Eye open
        self.kit.servo[self.left_upper_lid].angle = self.L_LID_OPEN_UPPER
        self.kit.servo[self.left_lower_lid].angle = self.L_LID_OPEN_LOWER
        # Right eye open
        self.kit.servo[self.right_upper_lid].angle = self.R_LID_OPEN_UPPER
        self.kit.servo[self.right_lower_lid].angle = self.R_LID_OPEN_LOWER
        print("Eyes opened")

    def close_eyes(self):
        # Left eye close
        self.kit.servo[self.left_upper_lid].angle = self.L_LID_CLOSE
        self.kit.servo[self.left_lower_lid].angle = 100
        # Right eye close
        self.kit.servo[self.right_upper_lid].angle = self.R_LID_CLOSE
        self.kit.servo[self.right_lower_lid].angle = 150
        print("Eyes closed")

    def look_left(self):
        self.kit.servo[self.left_eye_left_right].angle = self.L_EYE_LEFT
        self.kit.servo[self.left_eye_left_right].angle = self.L_EYE_LEFT

    def look_right(self):
        self.kit.servo[self.right_eye_left_right].angle = self.R_EYE_RIGHT
        self.kit.servo[self.right_eye_left_right].angle = self.R_EYE_RIGHT

    def look_up(self):
        self.kit.servo[self.left_eye_up_down].angle = self.L_EYE_UP
        self.kit.servo[self.right_eye_up_down].angle = self.R_EYE_UP

    def look_down(self):
        self.kit.servo[self.left_eye_up_down].angle = self.L_EYE_DOWN
        self.kit.servo[self.right_eye_up_down].angle = self.R_EYE_DOWN

    def look_center(self):
        #For Left right Movement
        self.kit.servo[self.left_eye_left_right].angle = self.L_EYE_CENTER_LR
        self.kit.servo[self.right_eye_left_right].angle = self.R_EYE_CENTER_LR
        # For Up down movement
        self.kit.servo[self.left_eye_up_down].angle = self.L_EYE_CENTER_UD
        self.kit.servo[self.right_eye_up_down].angle = self.R_EYE_CENTER_UD

    def blink(self, i):
        for _ in range(0, i):
            self.close_eyes()
            time.sleep(0.2)
            self.open_eyes()
            time.sleep(0.2)
        print("Blinked")





