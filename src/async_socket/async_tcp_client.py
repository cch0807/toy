import asyncio
import random
import socket
import time

HOST = "localhost"  # 서버 주소
PORT = 5050  # 서버 포트


async def tcp_sender(task_num: int) -> None:

    random_num = random.randrange(0, 5)

    data = bytes()

    # 소켓 객체 생성
    # 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용.
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # HOST와 PORT를 사용하여 서버 접속
    client_sock.connect((HOST, PORT))

    # 메시지 전송
    client_sock.sendall(f"task number is {task_num} \n".encode())

    # 메시지 수신
    data = client_sock.recv(1024)
    time.sleep(random_num)
    print("Received", repr(data.decode()))

    # 소켓 close
    client_sock.close()


async def main() -> None:
    task_num = 0
    while True:
        print(f"task {task_num} start")
        asyncio.create_task(tcp_sender(task_num))
        await asyncio.sleep(0.1)
        task_num += 1


if __name__ == "__main__":
    asyncio.run(main())
