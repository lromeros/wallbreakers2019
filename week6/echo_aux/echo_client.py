import socket

# create, connect
sock = socket.socket()
sock.connect(('localhost', 8000))


def receive_output():
    data = sock.recv(1024)
    print(data.decode('utf-8'))


def echo_client():
    while True:
        message = input()
        if message == '':
            print("closing connection")
            break
        sock.sendall(message.encode('utf-8'))
        receive_output()

    sock.close()


echo_client()

