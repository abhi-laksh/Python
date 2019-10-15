
#Taking the input from the user
a=int(input("Enter a number to check : "))

#defining function
def isPrime(x):
	for i in range(2,x):
		if a%i==0:
			return False
			break
		else:
			return True
			break


checkIf=isPrime(a)

if checkIf==0:
	print(a," is not prime")
else:
	print(a," is prime")
