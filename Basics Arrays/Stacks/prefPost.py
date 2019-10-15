## Date : Mar 11 2019 , 00:25
## ----  Created By Abhishek Soni
## ------  Format - UTF-8
## ---  Solves Postfix expression : e.g = 592/+ = 9
try:
	# import the file as a module
	from stacking import Stack 
except (ImportError):
	print("File not found !")


def calc(x,y,oper):
	if type(x) == int and type(y) == int:
		if oper=="^":
			return int(x)  **  int(y)
		elif oper=="/":
			return int(x) // int(y)
		elif oper=="*":
			return int(x) * int(y)
		elif oper=="+":
			return int(x) + int(y)
		elif oper=="-":
			return int(x) - int(y)
		else:
			print("Improper Operator")
	else:
		return "(" + x + " " + oper + " " + y + ")"

def prefixEval(exp , stack):
	for i in range(1,len(ques)+1):
		# scanning from the last
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
		# scanning from the beginning

		if each != "-" and each != "+" and each != "/" and each != "*" and each != "^" :
			stack.push(each)
		else:
			a = stack.pop()
			b = stack.pop()
			try: 
				res = calc(int(b),int(a),each)
				stack.push(res)
			except ValueError:
				res = calc(str(b),str(a),each)
				stack.push(res)
	return stack.pop()
def main():
	global option , ques ,ans
	n=int(input("Enter Size : "))
	# Creating object of Class STACK and then calling its methods
	st = Stack(n)
	# ques = "/*+AB-CDE"\
	ans=None
	while True:
		ask = input("Choose : \n 1) Prefix Evaluation \n 2) Postfix Evaluation \n Enter chice here :")

		if ask=="1":
			option = "pref"
			ques= input("\n Enter a prefix expression ( E.g : - + 98 - 32 ) : ")
			if ques!="" and not " " in ques:
				print(ques)
				break
			elif " " in ques:
				print("\n No Space Please! Choose Again ! \n")

			else:
				print("\nBlank Value Found ! Choose Again ! \n")

		elif ask=="2":
			option = "post"
			ques= input("\n Enter a postfix expression ( E.g : 23 - 89 + * ) : ")
			if ques!="" and not " " in ques:
				print(ques)
				break
			elif " " in ques:
				print("\n No Space Please! Choose Again ! \n")
			else:
				print("\nBlank Value Found ! Choose Again ! \n")

		else:
			print("\nBad Choice.\n")

	if option == "pref":
		try:
			ans = prefixEval(ques,st)
		except Exception as e:
			print(e)
	elif option == "post":
		try:
			ans = postfixEval(ques,st)
		except Exception as e:
			print(e)
	print(ans)

if __name__=="__main__":
	global option , ques ,ans
	main()