# -*- coding:utf-8 -*-

import socket

# 통신 정보 설정
IP = ""
PORT = 5050
SIZE = 1024
ADDR = (IP, PORT)

# 서버 소켓 설정

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
#     server_sock.bind(ADDR)  # 주소 바인딩
#     server_sock.listen()  # 클라이언트의 요청을 받을 준비

#     # 무한 루프 진입
#     while True:
#         (
#             client_socket,
#             client_addr,
#         ) = server_sock.accept()  # 수신대기, 접속한 클라이언트 정보 (소켓, 주소) 반환
#         msg = client_socket.recv(SIZE)  # 클라이언트가 보낸 메시지 반환
#         print(f"[{client_addr} message : {msg}]")
#         print(type(msg))
#         # client_socket.sendall(msg)  # 클라이언트에게 응답

server_socket.close()  # 클라이언트 소켓 종료
