arr = [5,3,7,2,6,9,10,4,1,8]
# arr = [44,2,5,33,6,4,55,40,11,16,45,22 ]

print("Orginal list : " , arr)
def bubbleIt(lst):
	n = len(lst)
	for i in range(n-1):
		for j in range(i+1,n):
			if arr[i] > arr[j]:
				arr[j] ,arr[i] = arr[i] , arr[j]
			else:
				i+=1
bubbleIt(arr)
print("Sorted list : ",arr)