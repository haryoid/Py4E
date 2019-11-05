import socket

url = input('Enter - ')
delimiter = '/'
splithost = url.split(delimiter)
host = str(splithost[2])
host = 'data.pr4e.org'
print(host)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

'''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
'''