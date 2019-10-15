
org = ['^'  ,'~' ,'`' , '#','/|' , '\\' , '{' , '}' , '[' , ']' , '&' ,
		'!' , '@', '>' ,'<' , '?' ,'$' , '(' , ')' , ';' , ':' , '¿' , '_+' , '_-' , '_*=' , '_=','NaN']

alpha = "abcdefghijklmnopqrstuvwxyz "
msg = "Hello, I am Abhishek Soni".lower()
data = list(msg)
# traces = list(enumerate(msg))
mainShuf = "".join(data)
enc = []
dec = []
for i in data:
	try:
		index = alpha.index(i)
		enc.append(org[index])
	except (IndexError , ValueError):
		index = 26
		enc.append(org[index])

traces = []
traces.extend(enc)

def shuffle(data):
	for i in range(len(data)):
		calc = ((len(data) - 1) % (i+1))
		data.append(data[calc])
		data.remove(data[calc])
	return None

print("".join(enc))
shuffle(enc)
print("".join(enc))
for i in data:
	if i not in msg:
		print(i , "not present")
for j in traces:
	try: 
		ind = org.index(j)
		dec.append(alpha[ind])
	except (IndexError , ValueError):
		print("err")
print("".join(dec))


a = "^NaN$:[`&NaN~(<_+>NaN\\<_-NaN]:@?)NaN<¿/|(NaN;}/|NaN!^_=_*=NaN#<{"
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
print(convertToList(org,a))
# print(a[1:1+2])

