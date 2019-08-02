import os
import socket

# create, bind, listen
sock = socket.socket()
sock.bind(('localhost', 8000))
sock.listen(1)


def echo_server():
    while True:
        client_conn, client_add = sock.accept()
        child_pid = os.fork()

        if child_pid == 0:
            child_process(client_conn)
            break


def child_process(connection):
    try:
        while True:
            data = connection.recv(1024)

            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()


echo_server()

