arr = [11,25,36,78,69,63,45,85,13,22]

print("Your list is : ",arr)
toFind = int(input("ENter number to search : "))

def linearSearch(lst,num):
	for elem in lst:
		if elem == num:
			return 1
	else:
		return 0

if linearSearch(arr,toFind):
	print("Present")
else:
	print("Not Present")
