arr = [4, 5, 6, 7, 8, 22, 23, 44, 68, 74]


print("List is :",arr)
item = int(input("Enter num to find : "))
def binarySearch(lst,num):
	lowIndex = 0 
	highIndex = len(lst) - 1
	found = False
	while not found and lowIndex<=highIndex:
		midIndex = ( lowIndex + highIndex ) // 2
		if arr[midIndex] == item:
			found=True
			break
		elif item > arr[midIndex] :
			# print(arr[midIndex])
			lowIndex = midIndex + 1
		else:
			highIndex = midIndex - 1
	return found
if binarySearch(arr,item):
	print(item ,"is present ")
else:
	print(item ,"is not Present ")

