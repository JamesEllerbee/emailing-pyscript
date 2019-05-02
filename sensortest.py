import RPi.GPIO as GPIO
import time

LEDpin = 13
SignalPin = 11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
 
GPIO.setup(SignalPin, GPIO.IN)
GPIO.setup(LEDpin, GPIO.OUT)
p = GPIO.PWM(LEDpin, 50)
#GPIO.output(LEDpin,0)
def main():
    
        
    while True:
        i = GPIO.input(SignalPin)
        if i == 0:
            print("nothing detected")
            GPIO.output(LEDpin,0)
        else:
            print("motion dected")
            GPIO.output(LEDpin,1)
        time.sleep(0.1)
            
def testPWM():
    p.start(0)
    for i in range(1,100,20):
        p.ChangeDutyCycle(i);
        time.sleep(2)
    for i in range(100, 1, -20):
        p.ChangeDutyCycle(i)
        time.sleep(1)
    print("done")
