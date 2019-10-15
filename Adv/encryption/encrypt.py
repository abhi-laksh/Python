import os
import random
try:
	from Crypto.Cipher import AES
except ModuleNotFoundError:
	os.system("python -m pip install pycrypto")
	from Crypto.Cipher import AES

key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
iv = bytes([chr(random.randint(0, 0xFF)) for i in range(16)])

print([x for x in key ])
print(len(iv))
aes = AES.new(key, AES.MODE_CBC, iv)
data = 'hello world 1234'
encd = aes.encrypt(data)
# print(len(data))