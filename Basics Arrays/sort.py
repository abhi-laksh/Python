def sorted(array):
	tempArr=[]
	while array:
		minim=array[0]
		for elem in array:
			if elem<minim :
				minim=elem
		tempArr.append(minim)
		array.remove(minim)
	return tempArr

arr=[-2,5,8,-8,9,-7,0,1,5]

print(sorted(arr))