import socket                   # Import socket module
from Crypto.PublicKey import RSA
from Crypto import Random
port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()             # Create a socket object
host = ""   					# Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

def get_Key():
	file = open("Keys\\Key.txt", "r")
	keystr = file.read() # retrieve exported private key from file
	file.close()
	print(keystr)
	Key = RSA.importKey(keystr)
	return Key

def send_data(Key):
	print 'Server listening for recievers'
	while True:
	    conn, addr = s.accept()     # Establish connection with client.
	    print 'Got connection from', addr
	    data = conn.recv(1024)
	    print('Server received', repr(data))

	    
	    f = open("SendersData\\sample.txt.txt",'rb')
	    l = f.read(1024)
	    while (l):
	       enc_data = Key.encrypt(l, 16)
	       #print enc_data
	       conn.send(enc_data[0])
	       print('Sent ',repr(l))
	       l = f.read(1024)
	    f.close()

	    print('Done sending')
	    conn.close()
	    exit(0)

Key = get_Key()
send_data(Key)