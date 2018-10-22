from gpiozero import LED, Button
from time import sleep

led1 = LED(17)
led2 = LED(27)
led3 = LED(13)
button = Button(2)
alarm_aan = False
tijd_aan = 0

def alarm():
    while True:
        led2.off()
        led3.on()
        sleep(1)
        led2.on()
        led3.off()
        sleep(1)


while True:
    if button.is_pressed and alarm_aan == False:
        alarm_aan = True
        led2.on()
        while not GPIO.input(button):
            time.sleep(0.01)
            tijd_aan = tijd_aan + 1
            if tijd_aan == 500:
                alarm()
        continue


