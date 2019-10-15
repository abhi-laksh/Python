
# ----   Insertion sort   ----
# arr = [44,2,5,33,6,4,55,40,11,16,45,22 ]
arr = [5,3,7,2,6,9,10,4,1,8]
print("\n----    Unsorted list    ----\n\n", arr)

def insertSort(lst):
	size = len(lst)
	j=0
	print("\n----    This is what happening    ----\n")
	for i in range(1,size):
		while j<i:
			if lst[i]< lst[j]:
				lst[j] , lst[i] = lst[i] ,lst[j]
			j+=1
		j=0
		print(*lst ,sep=" | ")
		print()

		

insertSort(arr)
print("\n----    Sorted List    ----\n")
print(arr)
