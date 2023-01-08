import asyncio
import socket

HOST = "localhost"  # 서버 주소
PORT = 5050  # 서버 포트


async def tcp_sender() -> None:
    # 소켓 객체 생성
    # 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용.
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # HOST와 PORT를 사용하여 서버 접속
    client_sock.connect((HOST, PORT))
    data = bytes()
    # 메시지 전송

    client_sock.sendall("text \n".encode())
    # 메시지 수신
    data = client_sock.recv(1024)
    print("Received", repr(data.decode()))
    # 소켓 close
    client_sock.close()


async def main() -> None:
    while True:
        asyncio.create_task(tcp_sender())
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
