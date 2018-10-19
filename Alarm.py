from gpiozero import LED, Button

led1 = LED(17)
led2 = LED(27)
led3 = LED(13)
button = Button(2)
status_1 = 0
status_2 = 0

while True:
    if button.is_pressed:
        led1.on()
        led2.on()
        led3.on()
        if status_1 == status_2:
            print("led is aan gedaan")
            status_1 = status_1 + 1
    else:
        led1.off()
        led2.off()
        led3.off()
        if status_1 > status_2:
            status_2 = status_2 + 1
        
