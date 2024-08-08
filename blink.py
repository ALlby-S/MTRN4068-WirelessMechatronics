from gpiozero import LED, Servo
from time import sleep

led = LED(17)

motor = Servo(27)

while True:
    led.on()
    motor.value =0.5
    print("LED should be ON")
    sleep(1) #Sleep for 1 second
    led.off()
    motor.value = 0
    print("LED should be OFF")
    sleep(1)