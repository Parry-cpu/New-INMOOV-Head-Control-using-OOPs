import time
# --- Import our new classes using the FULL package path here ---
from inmoov_driver.head.eyes import Eyes
from inmoov_driver.head.eyebrows import EyeBrows
from inmoov_driver.head.cheeks import Cheeks
from inmoov_driver.head.jaw import Jaw
from inmoov_driver.head.upbrows import UpBrows
from inmoov_driver.head.upperlip import UpperLip

# --- Import our hardware "remotes" ---
# This one line imports kit_42, whether it's REAL or SIMULATED
# All the old hardware setup lines (busio, board, servokit) are gone!
from inmoov_driver.hardware_setup import kit_42

# --- 1. SETUP HARDWARE (ONLY ONCE) ---

# This is now handled by importing from hardware_setup.py
print("Hardware objects imported.")

# --- 2. CREATE ROBOT PARTS (OBJECTS) ---
print("Assembling robot parts...")
# We give the "remote" (kit_42) to each part that needs it.
inmoov_eyes = Eyes(kit_42)
inmoov_eyebrows = EyeBrows(kit_42)
inmoov_cheeks = Cheeks(kit_42)
inmoov_jaw = Jaw(kit_42)
inmoov_upbrow = UpBrows(kit_42)
inmoov_upperlip = UpperLip(kit_42)


# --- 3. Using the created objects---
print("Starting command loop...")
try:
    while True:
        # We add the new eyebrow commands to the prompt
        cmd = input("Enter command: ").strip().lower()
        
        if cmd == "open_eyes":
            inmoov_eyes.open_eyes()
        
        elif cmd == "close_eyes":
            inmoov_eyes.close_eyes()

        elif cmd == "look_left":
            inmoov_eyes.look_left()
        
        elif cmd == "look_right":
            inmoov_eyes.look_right()
        
        elif cmd == "look_up":
            inmoov_eyes.look_up()
        
        elif cmd == "look_down":
            inmoov_eyes.look_down()

        elif cmd == "look_center":
            inmoov_eyes.look_center()

        elif cmd == "blink":
            inmoov_eyes.blink()

        elif cmd == "eyebrow_up":
            inmoov_eyebrows.move_brows("up")
        
        elif cmd == "eyebrow_down":
            inmoov_eyebrows.move_brows("down")
        
        elif cmd == "eyebrow_center":
            inmoov_eyebrows.move_brows("center")

        elif cmd == "cheeks_up":
            inmoov_cheeks.move_cheeks("up")
        
        elif cmd == "cheeks_down":
            inmoov_cheeks.move_cheeks("down")
        
        elif cmd == "cheeks_center":
            inmoov_cheeks.move_cheeks("center")

        elif cmd == "open_jaw":
            inmoov_jaw.move_jaw("open")

        elif cmd == "close_jaw":
            inmoov_jaw.move_jaw("close")

        elif cmd == "set_jaw":
            jaw_angle = int(input("Enter the Jaw angle: "))
            inmoov_jaw.set_jaw_angle(angle= jaw_angle)

        elif cmd == "upbrow_up":
            inmoov_upbrow.move_upbrows("up")

        elif cmd == "upbrow_down":
            inmoov_upbrow.move_upbrows("down")
        
        elif cmd == "upbrow_center":
            inmoov_upbrow.move_upbrows("center")

        elif cmd == "lip_up":
            inmoov_upperlip.move_lip("up")
        
        elif cmd == "lip_down":
            inmoov_upperlip.move_lip("down")

        elif cmd == "neutral":
            inmoov_eyes.look_center()
            inmoov_eyebrows.move_brows("center")
            inmoov_jaw.move_jaw("close")

        elif cmd == "exit":
            print("Exiting...")
            break

except KeyboardInterrupt:
    print("\nExiting...")