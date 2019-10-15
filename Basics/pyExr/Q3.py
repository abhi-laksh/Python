#  With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
#  such that is an integral number between 1 and n (both included). and then the program should
#  print the dictionary.


def dict(fst,last):
	diction={}
	for i in range(fst,last+1):
		key=i
		value=key*key
		diction[key]=value
	return diction


a=int(input("Enter start : "))
b=int(input("Enter end : "))

print(dict(a,b))