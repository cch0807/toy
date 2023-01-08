# -*- coding:utf-8 -*-

import socket
import time

# 통신 정보 설정
IP = ""
PORT = 5050
SIZE = 1024
ADDR = (IP, PORT)

# 서버 소켓 설정
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(ADDR)  # 주소 바인딩

server_sock.listen()

#  무한 루프 진입

while True:
    # 연결을 기다림
    print("waiting for a connection")
    (
        client_socket,
        client_addr,
    ) = server_sock.accept()  # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환
    try:
        print("connection from", client_addr)

        # data I/O
        while True:
            data = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환
            if data:

                print(f"[{client_addr} message : {data}]")
                client_socket.sendall(data)  # 클라이언트에게 응답
            else:
                print("no data from", client_addr)
            break
    finally:
        client_socket.close()
