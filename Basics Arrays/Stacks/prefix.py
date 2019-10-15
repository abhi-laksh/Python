## Date : Mar 11 2019 , 00:13
## ----  Created By Abhishek Soni
## ------  Format - UTF-8
## ---  Solver Prefix expression : e.g = /+592 = 7
import os

try:
	import numpy as np
except Exception as e:
	print("---    ---    " + e + "    ---    ---")
	os.system("python -m pip intall numpy")
	import numpy as np

def calc(x,y,oprs):
	if oprs == "+":
		try:
			return int(x) + int(y)	# Gives ValueError if its alphabet	
		except ValueError:
			return "(" + str(x) + oprs + str(y) + ")"
	elif oprs == "-":
		try:
			return int(x) - int(y)		
		except ValueError:
			return "(" + str(x) + oprs + str(y) + ")"
	elif oprs == "*":
		try:
			return int(x) * int(y)		
		except ValueError:
			return "(" + str(x) + oprs + str(y) + ")"
	elif oprs == "^":
		try:
			return int(x) ** int(y)		
		except ValueError:
			return "(" + str(x) + oprs + str(y) + ")"
	elif oprs == "/":
		try:
			if int(y)!=0:
				return int(x) // int(y)
			else:
				return "Found 0 in denumerator ! Division not possible."
		except ValueError:
			return "(" + str(x) + oprs + str(y) + ")"
	elif oprs == "%":
		try:
			return int(x) % int(y)		
		except ValueError:
			return "(" + str(x) + oprs + str(y) + ")"
	else:
		return "Improper Operator"

def push(stack,item):
	global top
	top+=1
	stack[top] = item

def pop(stack):
	global top
	item = stack[top]
	top-=1
	return item

def display(stack):
	global top
	print(stack[:top+1])

def main():
	global top , n ,ans
	# ques = "*+333" # ( ( ( 2 * 3 ) / 4 ) - 5 ) + 2 ==> ans = 6/4 -> 1-5 -> -4 + 2 -> -2 (answer)
	ques = "-*/+abcde"
	# ques = "+-/%*^abcdefg"
	n= int(input("Enter size : "))
	st = np.zeros(n,dtype=str)
	operand = []
	for each in ques:
		if each=="+" or each=="-" or each=="/" or each=="%" or each=="^" or each=="*":
			push(st,each)
		else:
			operand.append(each)
			if len(operand) == 2:
				operator = pop(st)
				ans = calc(operand[0],operand[1],operator)
				while len(operand)!=0:
					del operand[0]
				operand.append(ans)
	print(ans)

if __name__=="__main__":
	global top , n , ans
	top=-1
	main()