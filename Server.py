import socket 


host = ' local host'
port = 50000

b = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

b.bind(('', port))

b.listen(1)

cl, ard = b.accept()

print("CONNECTION?:", str(ard))

cl.send(b"Enter input...")

##TO FINISH 