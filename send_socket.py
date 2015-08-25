import socket

s = socket.socket()
host = "192.168.1.15" #ip of raspberry pi
port = 12345
s.connect((host, port))

s.listen(5)
while True:
  c, addr = s.accept()
  print ('Got connection from',addr)
  c.send('Thank you for connecting')
  c.close()