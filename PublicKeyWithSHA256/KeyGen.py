from Crypto.PublicKey import RSA
from Crypto import Random

def generate_key():
	rng = Random.new().read
	RSAkey = RSA.generate(1024, rng) 

	privatekey = RSAkey
	publickey = RSAkey.publickey()
	print(privatekey.exportKey()) #export under the 'PEM' format (I think)
	print(publickey.exportKey())
	file = open("Keys\\PublicKey.txt", "w")
	file.write(publickey.exportKey()) #save exported public key
	file.close()
	file = open("Keys\\PrivateKey.txt", "w")
	file.write(privatekey.exportKey()) #save exported private key
	file.close()

generate_key()