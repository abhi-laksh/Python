import os
try:
	import numpy as np 
except (ModuleNotFoundError , ModuleError , NameError):
	os.system("python -m pip install numpy")
	import numpy as np

global length , top , n
length = 0
top = -1


def display(st):
	global top 
	if top==-1:
		# print("Under Flow")
		return 0
	else:
		print(st[:top+1])

def push(st,num=None):
	global top , n
	if top == n-1:
		print("Over Flow")
	else:
		if num!=None:
			top+=1
			st[top] = num
		else:
			print("Expected a value but got nothing .")
def pop(st):
	global top
	if top == -1:
		# print("Under Flow")
		return 0
	else:
		temp = st[top]
		top -= 1
		return temp

def main():
	global length , top , n
	decimal = int(input("Enter a decimal to convert : "))
	res = decimal

	while res>0:
		length+=1
		rem = res%2
		res = res//2

	n=length
	stack = np.zeros(n, dtype = int)
	res = decimal

	while res>0:
		rem = res%2
		push(stack , rem)
		res = res // 2 

	while top>-1:
		a = pop(stack)
		print(a,end=" ")

main()
