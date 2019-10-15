#--- DATE : June 01, 2019 | 00:54:54
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): 
about=''
print('About :' + about)
import os
try:
	import random
except ImportError:
	os.system("python -m pip install random")
	import random

a = [44, 88, 11, 22, 33, 55, 100, 66, 77, 99]
# random.shuffle(a)
print(a)
def quick(arr):
	newArr = [e for e in arr]
	i = 1
	n = len(newArr)
	j = n - 1
	while i<n and j>=0:
		p = 0
		if (newArr[i] > newArr[p]) and (newArr[j] < newArr[p]):
			newArr[i] , newArr[j] = newArr[j] , newArr[i]
			print(newArr)
		i+=1
		j-=1
	

quick(a)