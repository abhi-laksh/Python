class SecureIt(object):
	def __init__(self):
		self.__orgPwd = ''
		self.__traces = []
		self.__encoders = ['^'  ,'~' ,'`' , '#','/|' , '\\' , '{' , '}' , '[' , ']' , '&' ,
		'!' , '@', '>' ,'<' , '?' ,'$' , '(' , ')' , ';' , ':' , '¿' , '_+' , '_-' , '_*=' , '_=','NaN']
		self.__alpha = "abcdefghijklmnopqrstuvwxyz "

	def __shuffle(self,data):
		for i in range(len(data)):
			calc = ((len(data) - 1) % (i+1))
			data.append(data[calc])
			data.remove(data[calc])

	def encrypt(self , message,pwd):
		self.__orgPwd = pwd
		self._enc = []
		for i in message:
			try:
				index = self.__alpha.index(i)
				self._enc.append(self.__encoders[index])
			except (IndexError , ValueError):
				index = 26
				self._enc.append(self.__encoders[index])
		self.__traces.extend(self._enc)
		self.__shuffle(self._enc)
		return "".join(self._enc)

	
	def decrypt(self , enc_message,pwd):
		self.__decPwd = pwd
		enc_msg_list = []
		if self.__decPwd == self.__orgPwd:
			self._dec = []

			for j in self.__traces:
				try: 
					ind = self.__encoders.index(j)
					self._dec.append(self.__alpha[ind])
				except (IndexError , ValueError):
					pass
			return "".join(self._dec)
		else:
			raise Exception

def main():
	ci = SecureIt()

	a = "^NaN$:[`&NaN~(<_+>NaN\\<_-NaN]:@?)NaN<¿/|(NaN;}/|NaN!^_=_*=NaN#<{"

	message = "96455645"
	encPass = input("Enter password to encrypt : ")
	cod = ci.encrypt(message.lower(),encPass)
	print("Encoded : " , cod)
	decPass = input("Enter a password to decrypt : ")

	try:
		decod = ci.decrypt(cod,decPass)
		print("Decoded : ",decod)
	except:
		print("Invalid Password!")

if __name__ == '__main__':
	main()