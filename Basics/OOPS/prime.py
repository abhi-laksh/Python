class isPrime:
	def __init__(self,num):
		for i in range(2,num):
			while i<=(num**0.5):
				if(num%i==0):
					print("No Prime")
					break
			else:
				print("Prime")
			




n=int(input("Enter number : "))

result=isPrime(n)