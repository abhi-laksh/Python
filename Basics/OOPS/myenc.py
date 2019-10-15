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
class SecureIt(object):
	def __init__(self):
		self.__orgPwd = ''
		self.__traces = []
		self.__encoders = ['^'  ,'~' ,'`' , '#','/|' , '\\' , '{' , '}' , '[' , ']' , '&' ,
		'!' , '@', '>' ,'<' , '?' ,'$' , '(' , ')' , ';' , ':' , '¿' , '_+' , '_-' , '_*=' , '_=','NaN','./','.,','.|','._','_|','_/','_,','.+','.-','.*']
		self.__alpha = "abcdefghijklmnopqrstuvwxyz 0123456789"
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

	f = open("test.txt",'w', encoding = 'utf-8')
	message = input("Enter a string. ")
	
	encPass = input("Enter password to encrypt : ")
	cod = ci.encrypt(message.lower(),encPass)
	f.write(cod)
	f.close()
	print("Encoded : " , cod)
	decPass = input("Enter a password to decrypt : ")

	try:
		f = open("test.txt",'r', encoding = 'utf-8')
		d = f.read()
		print(d)
		decod = ci.decrypt(d,decPass)
		print("Decoded : ",decod)
	except Exception as e:
		print(e)
if __name__ == '__main__':
	main()