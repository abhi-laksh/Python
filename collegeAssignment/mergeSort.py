#--- DATE : May 27, 2019 | 18:59:07
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): Merge Sort In List (Divide and Conquer)
about='Merge Sort In List'
print('About :' + about)
import os
try:
	import random
except ImportError:
	os.system("python -m pip install random")
	import random

a = [11,22,33,44,55,66,77,88,99,100]
random.shuffle(a)
print(a)
def divide(arr):
	if len(arr) > 1:
		n = len(arr)
		mid = n//2
		left = arr[ : mid]
		right = arr[mid : ]
		# print(left  , " | " , right)
		divide(left)
		divide(right)
		i = j = k = 0
		print("Before : ", arr)
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				arr[k] = left[i]
				i+=1
			else:
				arr[k] = right[j]
				j+=1
			k+=1
		print(i , j , k)

		while i < len(left):
			arr[k] = left[i]
			i+=1
			k+=1
		while j < len(right):
			arr[k] = right[j]
			j+=1
			k+=1
			
		print("After : ", arr)
		
divide(a)
print(a)

