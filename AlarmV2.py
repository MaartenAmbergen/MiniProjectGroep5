from gpiozero import LED, Button
from time import sleep

led1 = LED(17)
led2 = LED(27)
led3 = LED(13)
button = Button(2)
alarm_aan = False

while True:
    if button.is_pressed and alarm_aan == False:
        alarm_aan = True
        led2.on()
        sleep(5)
        if alarm_aan:
            led3.on()
            print("er moet nu een alarm naar de server worden gestuurd")
    elif button.is_pressed and alarm_aan:
        alarm_aan == False
        led2.off()
        led3.off()
        led1.on()
        sleep(1)
        led1.off()
        sleep(1)
        led1.on()
        sleep(1)
        led1.off()
        print("het alarm is gereset")
    
