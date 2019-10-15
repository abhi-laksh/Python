# Write a program which can compute the factorial of a given numbers

def fact(nums):
	if nums==0:
		return 1
	else:
		return nums* fact(nums-1)

n=int(input("Enter the nth term for factorial : "))
print(fact(n))