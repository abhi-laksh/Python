
import getpass
class SecureIt:
	def __init__(self, shift):
		self.__orgPwd = ''
		encoder = [None] * 26
		decoder = [None] * 26
		for i in range(26):
			encoder[i] = chr((i + shift) % 26 + ord('A'))
			decoder[i] = chr((i - shift) % 26 + ord('A'))
		self.__forward = "".join(encoder)
		self.__backward = "".join(decoder)
	def _transform(self , orginal , encoded):
		msg = list(orginal)
		for k in range(len(msg)):
			if msg[k].isupper():
				j = ord(msg[k]) - ord('A')
				msg[k] = encoded[j]
		return ''.join(msg)

	def encrypt(self , message):
		self.__orgPwd = getpass.getpass("Enter password ( You will need it while decrypting ) : ")
		return self._transform(message , self.__forward)
	def decrypt(self , enc_message):
		self.__decPwd = getpass.getpass("Enter password ( You entered while encrypting ) : ")
		if self.__decPwd == self.__orgPwd:
			return self._transform(enc_message , self.__backward)
		else:
			raise Exception("Invalid Password !")



ci = SecureIt(10)
message = "I am a good boy."
cod = ci.encrypt(message.upper())
print("Encoded : " , cod)
decod = ci.decrypt(cod)
print("Decoded : ",decod)