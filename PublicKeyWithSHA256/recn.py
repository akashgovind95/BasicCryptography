import socket                   # Import socket module
from Crypto.PublicKey import RSA
from Crypto import Random  
import hashlib
import time

s = socket.socket()             # Create a socket object
host = "127.0.0.1"              # Ip address that the TCPServer  is there
port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s.connect((host, port))
s.send("Hello server!")

def get_privateKey():
    file = open("Keys\\PrivateKey.txt", "r")
    privatestr = file.read() # retrieve exported private key from file
    file.close()
    privateKey = RSA.importKey(privatestr)
    return privateKey

def get_hash():
    sha256_hash = hashlib.sha256()
    with open("RecieversData\\sample_rec.txt","rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        print("Calculated hash of the file" + str(sha256_hash.hexdigest()))
    return sha256_hash.hexdigest()

def recieve_data(privateKey):
    with open('RecieversData\\sample_rec.txt', 'wb') as f:
        print 'File opened'
        while True:
            print('Receiving data...')
            data = s.recv(1024)
            enc_data = privateKey.decrypt(data)
            print('data=%s', (enc_data))
            if not data:
                break
            # write data to a file
            f.write(enc_data)

    f.close()
    print('Successfully recieved the file')
    
def recieve_hash():
	file = open("Hash\\recieved_hash.txt", "r")
	recieved_hash = file.read()
	file.close()
	print('Recieved hash: '+recieved_hash)
	calculated_hash = get_hash()
	if(calculated_hash == recieved_hash):
		print("\nSuccess..Untampered file recieved.")
	else:
		print("\nFailure..File is tampered.")


privateKey = get_privateKey()
recieve_data(privateKey)
recieve_hash()