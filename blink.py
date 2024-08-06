from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    print("LED should be ON")
    sleep(0.5) #Sleep for 1 second
    led.off()
    print("LED should be OFF")
    sleep(0.5)