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
	for i in range(n):
		print(end=" " * (n-i))
		print("_ " * i)

# pyramid(10)

def pyramindRev(n):
	for i in range(n+1):
		print(end=" "*i)
		print("- "*(n-i)) 

# pyramindRev(10)

def sandclock(n):
	for i in range(n+1):
		print(end=" "*i)
		print("# "*(n-i))
		print(end=" "*(n-i))
		print("# "*(i))
		

# sandclock(10)

def diamond(n):
	for i in range(n):
		print(end=" "*(n-i))
		print("* "*(i))
	for i in range(n+1):
		print(end=" "*(i))
		print("* "*(n-i))		

# diamond(5)


def A(n):
	if n>=3:
		rows = (2*n)+1
		for r in range(rows):
			for c in range(n):
				if (r!=0 and (c==0 or c==n-1)) or ((r==rows//2 or r==0) and (c>0 and c<n-1)):
					print("*",end=" ")
				else:
					print(end="  ")
			print()
	else:
		print("|--  Least value 3 is needed  --|")

# A(2)



def F(n):
	if n>=3:
		rows = (2*n)+1
		for r in range(rows):
			for c in range(n):
				if (r!=0 and (c==0)) or ((r==rows//2 or r==0) and (c>0 and c<n-1)):
					print("*",end=" ")
				else:
					print(end="  ")
			print()
	else:
		print("|--  Least value 3 is needed  --|")

# F(5)
def E(n):
	if n>=3:
		rows = (2*n)+1
		for r in range(rows):
			for c in range(n):
				if (r!=0 and (c==0)) or ((r==rows//2 or r==0 or r==rows-1) and (c>0 and c<n-1)):
					print("*",end=" ")
				else:
					print(end="  ")
			print()
	else:
		print("|--  Least value 3 is needed  --|")

# E(5)


def C(n):
	if n>=3:
		rows = (2*n)+1
		for r in range(rows):
			for c in range(n):
				if ((r!=0 and r!=rows-1) and (c==0)) or ((r==0 or r==rows-1) and (c>0 and c<n-1)):
					print("*",end=" ")
				else:
					print(end="  ")
			print()
	else:
		print("|--  Least value 3 is needed  --|")

# C(5)

def D(n):
	rows = (2*n)+1
	for r in range(rows):
		for c in range(n):
			if (c==0) or (c==n-1 and (r!=rows-1 and r!=0)) or ((r==0 or r==rows-1) and (c > 0 and c<n-1)):
				print("O",end=" ")
				# print(r , c)
			else:
				print(end="  ")
				# pass
		print()
# D(5)

def M(n):
	rows = n
	for r in range(rows):
		for c in range(n):
			if (c==0 or c==n-1) or ((r==c) and (c>0 and c<(n//2) + 1)) or (r == 1 and c==n-1) or (r==1 and c==(n//2)+1):
				print("#",end=" ")
				# print(r , c)
			else:
				print(end="  ")
				# pass
		print()
# M(5)



def H(n):
	rows = (2*n)+1
	for r in range(rows):
		for c in range(n):
			if (r!=0 and (c==0 or c==n-1)) or (r==rows//2):
				print("*",end=" ")
			else:
				print(end="  ")
		print()

# H(5)

def rightTri2(n):
	spaces = (n - 1) * 2
	for i in range(0, n+1):
		if i % 2 !=0:
			print(" * "*i)
		print("\r")

# rightTri2(10)


def triangleBorder(n):
	# spaces = 2*(n-1)
	for r in range(n):
		for c in range(n):
			if (c==r) or (r==0 or c==n-1):
				print("#",end=" ")
			else:
				print(end="  ")
				# print()
		print("\r")

# triangleBorder(10)


def X(n):

	for r in range(1,n+1):
		j=n-r
		for c in range(1,n+1):
			i=c-1
			if (r==c):
				print("*",end=" ")
			elif c==j or r==i:
				print("*",end="") 
			else:
				print(end=" ") 

		# print("*",end=" ")
		print()
			
X(8)
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

# Q3 : 			1
# 				2 3
# 				4 5 6 
# 				7 8 9 10

def numpat2(n):
	num = 1
	for i in range(n):
		for j in range(i+1):
			print(num , end=" ")
			num+=1
		print("\r")
# numpat2(4)

# Q3  		1
# 		  2   2
# 	    3   3   3
def numpat3(n):
	num = 1
	spaces = (n - 1) * 2
	for i in range(n+1):
		for j in range(spaces):
			print(end=" ")
		spaces-=1
		print((str(i) + " " ) * i)
		print("\r")
# numpat3(4)
# Q3  		1
# 		  2   3
# 	    4   5   6
def numpat3(n):
	num = 1
	spaces = (n - 1) * 2
	for i in range(n):
		for j in range(spaces):
			print(end=" ")
		spaces-=1
		# print("\r")
		for k in range(i+1):
			print(num , end=" ")
			num+=1
		print("\n")
# numpat3(4)

# Q4 : wave
def numpat4(n):
	print("\n")
	num = 1
	spaces = (n - 1) * 2
	tempSpace = spaces
	for i in range(n):
		for j in range(spaces):
			print(end=" ")
		spaces-=i
		# print("\r")
		for k in range(i+1):
			print("/", end=" ")
			num+=1
		print("\n")
# numpat4(7)

# Q5: circle
def circle(n):
	print("\n")
	num = 1
	spaces = (n - 1) * 2
	tempSpace = spaces
	for i in range(n):
		for j in range(spaces):
			print(end=" ")
		spaces-=i
		# print("#" ,end=" ")
		# print("\r")
		for k in range(i+1):
			print("#", end=" ")
			num+=1
		print("\n")
# circle(10)