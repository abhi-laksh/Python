#,--- DATE : June 07, 2019 | 15:24:39
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): 
about=''
print('About :' + about)
import time
a = list(range(1,100000))
def rot(arr):
	n = len(a)
	k = n//2
	f = 0
	while k>0:
		arr[f] ,arr[n-1] = arr[n-1] ,arr[f]
		n-=1
		f+=1
		k-=1
st = time.time()
rot(a)
print("-- " , (time.time() - st) , " --")




