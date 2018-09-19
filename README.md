# BasicCryptography
Get started with the basics of cryptography in Python.

I'm assuming that the basics of crytography are already clear to you.   
If not, click [here](https://en.wikipedia.org/wiki/Cryptography)  
Read more here - [PublicKey Crpytography](https://en.wikipedia.org/wiki/Public-key_cryptography), [Symmetric Cryptography](https://en.wikipedia.org/wiki/Symmetric-key_algorithm), [SHA256](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms)  

The code deals with three types of problems.  
1. Symmetric key cryptography i.e. One key for both sender and reciever.  
2. Public Key cryptography i.e Two keys (Public key for encryption and Private Key for decryption).  
3. Public Key cryptograhy with SHA256 i.e. (Same as previous one but hashing helps in checking the authenticity of the file transferred).  

## Description
The programs aim to transfer a file from sender to reciever via socket programming in an encrypted fashion.
The sender sends a sample.txt in chunks of 1024 bytes (every chunk is encrypted before sending). The reciever then recieves these chunks, decryptes them and save them to a file. Hence the file is transferred (Securely).

## Requirements  
1. [Python2.7](https://www.python.org/ftp/python/2.7/python-2.7.amd64.msi)  
2. Pycrypto library. Run the following command to get Pycrypto: "C:\python27\Scripts\easy_install pycrypto"  

## Steps  
1. First things first, we need keys. Irrespective what program you wish to execute, run KeyGen.py first. This shall create key(s) in the keys folder.  
`python KeyGen.py`
2. Secondly, run sendn.py, this shall wait for a reciever before sending out a file to reciever.  
`python sendn.py`
3. Lastly, run recn.py, this shall connect to a sender and starts to recieve file.  
`python recn.py`


