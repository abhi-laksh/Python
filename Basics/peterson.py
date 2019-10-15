# Date - 18 Jan ' 19'
	#  ---  by Abhishek Soni
# ---  Peterson number -----
#  n = 145 , if 1! + 4! + 5! == n then n is PETERSON


n=int(input("Enter a number to check --  "))

# n=145

temp = n
s=0
#  ----   Factorial Function
def fac(n):
	if n==0:
		return 1
	else:
		return n * fac(n-1)

# ---   The program
while temp!=0:
	# Getting digit of number (remainder) e.g = 145 / 10 , rem = 5
	rem = temp%10

	factorial = fac(rem) # Factorial of digit , e.g = 5!

	s+= factorial

	temp = temp//10 	# deleting digit , e.g = 145//10 = 14 (5 deleted)

if s == n:
	print(n, " is Peterson :D") # 145 is a PETERSON NUMBER
else:
	print(n , " is not Peterson :-(")
