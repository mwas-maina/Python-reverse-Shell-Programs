import socket
import sys


def create_socket():
    #create a socket or connection between two computers
    try:
        global host
        global port
        global sock
        host = ""
        port = 9999
        sock = socket.socket()
    except socket.error as msg:
        print('connection failed: ' + str(msg))


#binding the socket and host /listening for connections
def bind_socket():
    try:
        global host
        global port
        global sock
        print('binding the port: ' + str(port))
        sock.bind((host, port))
        sock.listen(5)
    except socket.error as msg:
        print('Socket connection failed: ' + str(msg) + 'Retrying...')
        bind_socket()


#accepted connections
def socket_accept():
    conn, address = sock.accept()
    print('Connection Established for ' + 'IP' + address[0] + ' and port ' +
          str(address[1]))
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            sock.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
