import socket
import os

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            elif data.decode().startswith('SEND_FILE'):
                filename = data.decode().split()[1]
                print(f'Receiving file: {filename}')
                with open(filename, 'wb') as f:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                print(f'File received: {filename}')
                conn.sendall(b'FILE_RECEIVED')
            else:
                print('Received:', repr(data))
