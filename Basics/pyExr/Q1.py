# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,

def find(start,end):
	lst=[] # to store nums
	for i in range(start , end+1):
		if i%7==0 and i%5!=0:
			lst.append(i)
	return lst

a=int(input("Enter start : "))
b=int(input("Enter end : "))

nums=find(a,b)

for i in nums:
	print(i,end=" , ")
