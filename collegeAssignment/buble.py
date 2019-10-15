#--- DATE : May 31, 2019 | 23:02:32
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): Bubble Sort
about='Bubble Sort'
print('About :' + about)

import random
a = [11,12,13,14,15,16,17,18,19,20]
random.shuffle(a)
print(a)
def bubbleSort(arr):
	newArr = [e for e in arr]
	for i in range(len(newArr)):
		for j in range(len(newArr) - (i+1)):
			if newArr[j] > newArr[j+1]:
				newArr[j] , newArr[j+1] = newArr[j+1] , newArr[j] 
	print(newArr)
# bubbleSort(a)

def insertion(arr):
	newArr = [e for e in arr]
	j = 1
	n = len(newArr)
	while j < n:
		minm = newArr[j]
		k = j-1
		while k>=0 and newArr[k] > minm:
			newArr[k+1] = newArr[k]
			k-=1
		newArr[k+1] = minm
		j+=1
	print(newArr)

def selection(arr):
	newArr = [e for e in arr]
	n = len(newArr)
	for i in range(len(newArr)):
		minm = i
		for e in range((i + 1), len(newArr)):
			if newArr[e] < newArr[minm]:
				minm = e
		if minm != i:
			newArr[minm] , newArr[i] = newArr[i] , newArr[minm]
	print(newArr)
selection(a)