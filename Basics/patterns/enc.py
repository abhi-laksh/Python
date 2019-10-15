
a = ['`','~','!','^','_(','_{','_[','_)','_]','_}','/|','_=',
		'_+','_*','_|','#','_-','_:','_;','<','>','.-','.=','.*',
		'.|','.?','NaN','_?','_¿','.¿','\\' ,'.:','.;','.(','.)','.{','.}']


def convertList(enclst,message=""):
	i=0
	lgth = len(message)
	arr = []
	if message!="" and enclst:
		while i<lgth:
			code = message[i]
			for each in enclst:
				try:
					pos = enclst.index(code)
					if enclst[pos] == code:
						arr.append(code)
						i+=1
						break
				except (ValueError):
					subs2 = message[i:i+2]
					try:
						index = enclst.index(subs2)
						if enclst[index] == subs2:
							arr.append(subs2)
							i+=2
							break
					except (ValueError):
						subs3 = message[i:i+3]
						index = enclst.index(subs3)
						if enclst[index] == subs3:
							arr.append(subs3)
							i+=3
							break
		return arr
	else:
		return "----    Either message is blank or Encoder not provided    ----"

class SecureMessage(object):
	def __init__(self):
		self.__encPwd = ""
		self.__encoderList = ['`','~','!','^','_(','_{','_[','_)','_]','_}','/|','_=',
		'_+','_*','_|','#','_-','_:','_;','<','>','.-','.=','.*',
		'.|','.?','NaN','_?','_¿','.¿','\\' ,'.:','.;','.(','.)','.{','.}']
		self.__alpha= "abcdefghijklmnopqrstuvwxyz 0123456789"
	def encrypt(self ,org_msg , pwd):
		self.__encPwd = pwd
		self._encList = []
		for char in org_msg:
			try:
				ind = self.__alpha.index(char)
				self._encList.append(self.__encoderList[ind])
			except (ValueError, IndexError):
				ind = 26
				self._encList.append(self.__encoderList[ind])
		return "".join(self._encList)
	def decrypt(self, encMessage , decPwd):
		msgList = convertList(self.__encoderList,encMessage)
		self.__decList = []
		if decPwd==self.__encPwd:
			for each in msgList:
				try:
					indexx = self.__encoderList.index(each)
					self.__decList.append(self.__alpha[indexx])
				except Exception as e:
					return "----    " + e + "    ----"
			return "".join(self.__decList)
		else:
			raise Exception("----   Invalid Password !!    ----")


# print(a[26])
def main():
	obj = SecureMessage()
	msg = input("Enter message : ").lower()
	pwd = input("Enter password to encrypt : ")
	msg = obj.encrypt(msg,pwd)
	print("Encrypted : ",msg)
	pwd = input("Enter password to decrypt : ")
	try:
		dec = obj.decrypt(msg ,pwd)
		print("Decrypted Message : ",dec.upper())
	except Exception as e:
		print(e)


if __name__ == "__main__":
	main()
