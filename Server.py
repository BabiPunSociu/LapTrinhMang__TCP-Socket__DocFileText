# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 00:23:29 2023

@author: ADMIN
"""

import socket

if __name__ == '__main__':
    ip = 'localhost'
    port = 9050
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((ip, port))
    serverSocket.listen(5)
    sk, add = serverSocket.accept()

    data = sk.recv(1024)
    try:
        file = open(data.decode('utf-8'), 'r')
        data = file.read()
    except FileNotFoundError:
        data = "Khong tim thay file"
    sk.send(data.encode('utf-8'))
    sk.close()