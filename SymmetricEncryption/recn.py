import socket
from Crypto.PublicKey import RSA
from Crypto import Random                   # Import socket module
s = socket.socket()             # Create a socket object
host = "127.0.0.1"              # Ip address that the TCPServer  is there
port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s.connect((host, port))
s.send("Hello server!")

def get_Key():
    file = open("Keys\\Key.txt", "r")
    keystr = file.read() # retrieve exported private key from file
    file.close()
    print(keystr)
    Key = RSA.importKey(keystr)
    return Key

def recieve_data(Key):
    with open('RecieversData\\sample_rec.txt', 'wb') as f:
        print 'File opened'
        while True:
            print('Receiving data...')
            data = s.recv(1024)
            enc_data = Key.decrypt(data)
            print('data=%s', (enc_data))
            if not data:
                break
            # write data to a file
            f.write(enc_data)

    f.close()
    print('Successfully recieved the file')
    s.close()
    print('Connection closed')

Key = get_Key()
recieve_data(Key)