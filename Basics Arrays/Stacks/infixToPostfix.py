## Date : Mar 11 2019 , 00:25
## ----  Created By Abhishek Soni
## ------  Format - UTF-8
## ---  Solves Postfix expression : e.g = 592/+ = 9
try:
	from stacking import Stack 
except (ImportError):
	print("File not found !")

def calc(x,y,oper ,postfix = True):
	if postfix:
		if oper=="^":
			return str(x) +  str(y) + oper
		if oper=="/":
			return str(x) +  str(y) + oper
		if oper=="*":
			return str(x) +  str(y) + oper
		if oper=="+":
			return str(x) +  str(y) + oper
		if oper=="-":
			return str(x) +  str(y) + oper
		else:
			return "Improper Operator"
	else:
		if oper=="^":
			return oper + str(x) +  str(y)
		if oper=="/":
			return oper + str(x) +  str(y)
		if oper=="*":
			return oper + str(x) +  str(y)
		if oper=="+":
			return oper + str(x) +  str(y)
		if oper=="-":
			return oper + str(x) +  str(y)
		else:
			print("Improper Operator")


def precednce(oper):
	if oper=="^":
		return oper
	if oper=="/":
		return oper
	if oper=="*":
		return oper
	if oper=="+":
		return oper
	if oper=="-":
		return oper
	else:
		return ""
def prefixEval(exp , stack):
	for i in range(1,len(ques)+1):
		each = ques[-i]
		if each != "-" and each != "+" and each != "/" and each != "*" and each != "^" :
			stack.push(each)
		else:
			a = stack.pop()
			b = stack.pop()
			try: 
				res = calc(int(a),int(b),each)
				stack.push(res)
			except ValueError:
				res = calc(str(a),str(b),each)
				stack.push(res)
	return stack.pop()
def postfixEval(exp , stack):
	for i in range(0,len(ques)):
		each = ques[i]
		if each != "-" and each != "+" and each != "/" and each != "*" and each != "^" :
			stack.push(each)
		else:
			a = stack.pop()
			b = stack.pop()
			try: 
				res = calc(int(a),int(b),each)
				stack.push(res)
			except ValueError:
				res = calc(str(a),str(b),each)
				stack.push(res)
	return stack.pop()
def main():
	global option , ques ,ans
	n=int(input("Enter Size : "))
	st = Stack(n)
	ques = "(A – ((B / C + (D % E * F) / G) * H))".replace(" ","")
	isEnd = False
	operand = []
	for i in range(0,len(ques)):
		each = ques[i]
		if each == "(" or each == "^" or each == "/" or each == "*" or each == "+" or each == "-":
			st.push(each)
		elif each==")":
			isEnd = True
			while isEnd:
				a = st.pop()
				if a=="(":
					isEnd =False
				else:
					if 
			# st.display()
			while len(operand) !=0:
				del operand[0]
			# st.push(ans)
			operand.append(ans)
			print(operand)
		else:
			operand.append(each)
	print(ans)
		
if __name__=="__main__":
	global option , ques ,ans
	main()