import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))                                             #First the program makes a connection to port 80 on the server www.py4e.com.
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()                #\r\n signifies an EOL (end of line), so \r\n\r\n signifies nothing between two EOL sequences. That is the equivalent of a blank line.
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysocket.close()