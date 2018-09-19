import socket
from Crypto.PublicKey import RSA
from Crypto import Random                   # Import socket module
s = socket.socket()             # Create a socket object
host = "127.0.0.1"              # Ip address that the TCPServer  is there
port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s.connect((host, port))
s.send("Hello server!")

def get_privateKey():
    file = open("Keys\\PrivateKey.txt", "r")
    privatestr = file.read() # retrieve exported private key from file
    file.close()
    print(str)
    privateKey = RSA.importKey(privatestr)
    return privateKey

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
    s.close()
    print('Connection closed')

privateKey = get_privateKey()
recieve_data(privateKey)