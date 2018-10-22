from gpiozero import LED, Button
from time import sleep
import socket

HOST = '145.89.154.183' # Enter IP or Hostname of your server
PORT = 12345 # Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#Lets loop awaiting for your input


ledG = LED(17)
ledY = LED(27)
ledR = LED(13)
button1 = Button(2)
button2 = Button(3)


def Alarmtriggered():
    ledG.off()
    ledY.on()
    tijd = 0
    while tijd < 500:
        tijd = tijd + 1
        if button2.is_pressed:
            AlarmAan()
            break
        sleep(0.01)
    ledR.on()
    ledY.off()
    ledG.off()
    command = raw_input('Enter your command: ')
    s.send(command)


def AlarmAan():
    ledG.on()
    ledY.off()
    while True:
        if button1.is_pressed:
            Alarmtriggered()


AlarmAan()
