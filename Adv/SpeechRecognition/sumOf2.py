lst = [4,9,6,7,2,3,4,6,8]


lst2 = []
n=10

for i in lst:
	x= n - i
	if x not in lst2.index(x):
		lst2.append(x)
	

print(lst2)