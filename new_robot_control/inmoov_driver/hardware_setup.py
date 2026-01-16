# --- Mock Classes (for simulation if PCA's are not connected)
class MockServo:
    "A fake servo that just prints angles"

    def __init__(self,channel):
        self.channel = channel
        self._angle = 0 
    
    @property
    def angle(self):
        return self._angle
    
    @angle.setter
    def angle(self,value):
        if value <0:value = 0
        if value>180:value = 180
        self._angle = value
        
        print(f"[SIMULATION] Servo C:{self.channel} angle set to {self._angle}")

class MockServoKit:

    """A fake servokit class that has a .servo property"""

    def __init__(self,channels,i2c,address):
        self._address = address
        self._channels = channels

        print("\n" + "="*50)
        print(f"    WARNING: RUNNING IN SIMULSTION MODE ")
        print(f"    Real hardware(I2C Board) not found/missing")
        print(f"    Creating Mock ServoKit ar address {hex(self._address)}")
        print("="*50+"\n" )

        self._servos = [MockServo(i) for i in range(channels)]

    @property
    def servo(self):
        # This is our fake .servo property
        #It must return a list of fake servos made
        return self._servos

"""
In the hardware_setup module in the try block
we will try to import all the real modules and hardware

"""
try:
    from board import SCL, SDA
    import busio
    from adafruit_servokit import ServoKit

    print("Initializing REAL I2C and Servokits")

    #I2C setup
    i2c_bus = busio.I2C(SCL,SDA)

    #PCA9685 set channel and address for i.e set "remote" for board at address 0x42
    #in this section you will have to create 3 remotes for the 3 main PCA's
    kit_42 = ServoKit(channels=16,i2c=i2c_bus, address = 0x42 )
    kit_41 = ServoKit(channels = 16, i2c = i2c_bus, address= 0x41)
    kit_40 = ServoKit(channels=16, i2c=i2c_bus,address=0x40)

    print("Real hardware setup complete")

except (ImportError,RuntimeError,NotImplementedError):
    print("PCA's not connected!!\nEntering simulation mode now")

    i2c_bus = None

    kit_40 = MockServoKit(channels=16,i2c=i2c_bus,address=0x40)
    kit_41 = MockServoKit(channels=16,i2c=i2c_bus,address=0x41)
    kit_42 = MockServoKit(channels=16,i2c=i2c_bus,address=0x42)

# --- Ending Hardware initialization --- #





