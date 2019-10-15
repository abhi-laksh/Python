# Inserting into a dictionary
a={}
n=int(input("Enter num of elem ; "))

for i in range(1,n+1):
	key=input("Enter key : ")
	value=input("Enter value : ")
	a[key]=value

	print(a[key])