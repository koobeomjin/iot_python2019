# -*- coding:utf-8 -*-
import bluetooth
import RPi.GPIO as GPIO
import time

one = 0
two = 0
three = 0
four = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)


server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 2
server_socket.bind(("B8:27:EB:41:2B:FC", port))
server_socket.listen(1)

client_socket, address = server_socket.accept()
print("Accepted connection from", address)
while 1:
    data = client_socket.recv(1024)
    data = data.decode('utf-8')
    # print("Received:%s" % data)
    if (data == "q"):
        print("quit")
        break
    elif (data == '1'):
        one += 1
        if one%2 == 1:
            GPIO.output(2,True)
            print('가습기 켜짐')
        elif one%2 == 0:
            GPIO.output(2, False)
            print('가습기 꺼짐')
    elif (data == '2'):
        two += 1
        if two%2 == 1:
            print('제습기 켜짐')
        elif two%2 == 0:
            print('제습기 꺼짐')
    elif (data == '3'):
        three += 1
        if three%2 == 1:
            print('창문 열림')
        elif three%2 == 0:
            print('창문 닫힘')
    elif (data == '4'):
        four += 1
        if four%2 == 1:
            print('에어컨 켜짐')
        elif four%2 == 0:
            print('에어컨 꺼짐')


GPIO.output(2, False)
client_socket.close()
server_socket.close()