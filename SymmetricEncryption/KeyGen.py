from Crypto.PublicKey import RSA
from Crypto import Random

def generate_key():
	rng = Random.new().read
	RSAkey = RSA.generate(1024, rng) 

	Key = RSAkey
	print(Key.exportKey()) #export under the 'PEM' format (I think)
	file = open("Keys\\Key.txt", "w")
	file.write(Key.exportKey()) #save exported key
	file.close()

generate_key()