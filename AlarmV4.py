from gpiozero import LED, Button
from signal import pause
from time import sleep

ledG = LED(17)
ledY = LED(27)
ledR = LED(13)
button1 = Button(2)
button2 = Button(3)


def Alarmtriggered():
    ledG.off()
    ledY.on()
    tijd = 0
    while tijd <500:
        tijd = tijd+1
        if button2.is_pressed:
            AlarmAan()
            break
        sleep(0.01)
    ledR.on()
    ledY.off()
    ledG.off()

def AlarmAan():
    ledG.on()
    ledY.off()
    while True:
        if button1.is_pressed:
            Alarmtriggered()
            
AlarmAan()
if button1.is_pressed and button2.is_pressed:
    exit()

