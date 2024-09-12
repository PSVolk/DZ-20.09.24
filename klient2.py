import socket
import os

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

filename = input('Enter the file to send: ')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(f'SEND_FILE {filename}'.encode())
    with open(filename, 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            s.sendall(data)
    response = s.recv(1024)
    if response == b'FILE_RECEIVED':
        print(f'File {filename} sent successfully.')
    else:
        print('Failed to send the file.')
