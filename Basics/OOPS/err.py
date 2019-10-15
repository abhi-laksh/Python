def convertToList( orgList ,message="" ):
	lengthh = len(message)
	i = 0
	b=[]
	while i < lengthh:
		eachChar = message[i]
		for subs in orgList:
			try:
				indexx = orgList.index(eachChar)
				if orgList[indexx] == eachChar:
					b.append(eachChar)
					i+=1
					break
			except (ValueError):
				special = message[i:i+2]
				try:
					indexx = orgList.index(special)
					if orgList[indexx] == special:
						b.append(special)
						i+=2
						break
				except (ValueError):
					special = message[i:i+3]
					indexx = orgList.index(special)
					if orgList[indexx] == special:
						b.append(special)
						i+=3
						break
	return b
#  , '.,' , './','.|','_|','_|-',''
class SecureIt(object):
	def __init__(self):
		self.__orgPwd = ''
		self.__traces = []
		self.__encoders = ['^'  ,'~' ,'`' , '#','/|' , '\\' , '{' , '}' , '[' , ']' , '&' ,
		'!' , '@', '>' ,'<' , '?' ,'$' , '(' , ')' , ';' , ':' , '¿' , '_+' , '_-' , '_*=' , '_=','NaN']
		self.__alpha = "abcdefghijklmnopqrstuvwxyz "
		self.__numeric = "0123456789"
	def encrypt(self , message,pwd):
		self.__orgPwd = pwd
		self._enc = []
		for i in message:
			try:
				index = self.__alpha.index(i)
				self._enc.append(self.__encoders[index])
			except (IndexError , ValueError):
				index = self.__numeric.index(i)
				self._enc.append(self.__alpha[index])
		return "".join(self._enc)
		
	def decrypt(self , enc_message,pwd):
		self.__decPwd = pwd
		enc_msg_list = convertToList(self.__encoders,enc_message)
		if self.__decPwd == self.__orgPwd:
			self._dec = []
			for j in enc_msg_list:
				try: 
					ind = self.__encoders.index(j)
					self._dec.append(self.__alpha[ind])
				except Exception as e:
					print(e)
			return "".join(self._dec)
		else:
			raise Exception("\n Invalid password ! Please Enter valid password")

def main():
	ci = SecureIt()
	message = "Abhi45245shek"
	encPass = input("Enter password to encrypt : ")
	cod = ci.encrypt(message.lower(),encPass)
	print("Encoded : " , cod)
	decPass = input("Enter a password to decrypt : ")

	try:
		decod = ci.decrypt(cod,decPass)
		print("Decoded : ",decod)
	except Exception as e:
		print(e)
if __name__ == '__main__':
	main()