n = 1000
def sumIt(nthTerm):
	if nthTerm>=1:
		return nthTerm + sumIt( nthTerm - 1 )
	else:
		return nthTerm

# print(sumIt(n))

def nat(n,x=0):
	print(x)
	if x<n:
		nat(n , x+1)
# nat(n)

def fibb(nthTermrm):
	if nthTermrm<=1:
		return nthTermrm
	else:
		return fibb(nthTermrm-1) + fibb(nthTermrm-2)

# for i in range(n):
# 	print(fibb(i))


#  ---   Patterns ---

# Q1 :   *						  *
# 		 * *		  OR   	    * *
# 	     * * *				  * * *


def rightAngle(n):
	for i in range(1,n+1):
		print("/" * i)
	print("------------------>")
	for i in range(n+1):
		print("\\" * (n-i))
# rightAngle(5)


# Q2 :        *
# 			*   *
# 		  *   *   *

def pyramid(n):
	spaces = (n - 1) * 2
	for i in range(0, n+1):
		for j in range(spaces):
			print(end=" ")
		spaces = spaces - 1
		print("+ " * i)
		# print("\r") 
# pyramid(10)


# Q2 :      1
# 			2 2
# 			3 3 3
# 			4 4 4 4


def numpat(n):
	num = 1
	for i in range(1,n+1):
		print(str(num) * i ,end="")
		print("\r")
		num+=1
# numpat(6)


def sumDigit(n):
	num = 505
	s=0
	for i in str(num):
		s+= int(i)
	print(s)

def arms():
	num = 370
	# temp = num
	s = 0
	for i in str(num):
		s+= int(i) ** 3

	if s==num:
		print("Armstrong")
	else:
		print("No")
# arms()


def reverseIt(n):
	reverse = ''
	if len(str(n)) != 0:
		n = str(n).lower().replace(" ","")
		for i in range(1,len(str(n))+1):
			reverse+= str(n)[-i]

		if reverse == n:
			print("palindrome")
		else:
			print("no pal")
	else:
		raise Exception("Some value is expected !")
# reverseIt("")


def recurReverse(sent):
	sent = str(sent)
	if len(sent):
		
recurReverse(54465)