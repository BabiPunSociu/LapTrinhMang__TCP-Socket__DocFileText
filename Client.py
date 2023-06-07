# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 00:23:29 2023

@author: ADMIN
"""

import socket

if __name__ == '__main__':
    ip = 'localhost'
    port = 9050

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((ip, port))

    fileName = input('nhap ten file .txt: ')
    clientSocket.send(fileName.encode('utf-8'))

    msg = clientSocket.recv(1024).decode('utf-8')
    print(msg)