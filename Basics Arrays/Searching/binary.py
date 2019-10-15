arr = [10,2,4,5,1,3,6,8,7,9]
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Sorting it first
def bubbleSort(array):
	size = len(array)
	for i in range(size):
		for j in range((size-i)-1):
			if array[j+1]< array[j]:
				array[j+1] , array[j] = array[j] , array[j+1]
	return True

def binary(array , item):
	if bubbleSort(array):
		high = len(array) - 1
		low = 0
		found = False
		while low <= high and not found:
			 mid = (high + low) // 2
			 if array[mid] == item:
			 	found = True
			 	break
			 else:
			 	if item > array[mid]:
			 		low = mid + 1
			 	else:
			 		high = mid - 1
		return found
	else:
		return False

def main():
	item = int(input("Enter to find "))
	if binary(arr , item):
		print("Found %d" %item + " at postion %d" %arr.index(item) )
	else:
		print("Not Found")

if __name__ == "__main__":
	main()
