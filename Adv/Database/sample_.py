def func(name="", data={}):
	myData = name + ",".join(str(val) for val in data.values())
	print(myData)


diction={'Name' : 'Abhi shek' , 'age' : 9}
func(name="Data : ",data=diction)