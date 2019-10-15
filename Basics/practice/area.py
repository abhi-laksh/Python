a=int(input("Enter a side of a triangle : "))
b=int(input("Enter a side of a triangle : "))
c=int(input("Enter a side of a triangle "))

s=(a+b+c)/2

if s>a and s>b and s>c:
	area=(s*(s-a)*(s-b)*(s-c))**0.5
	print(s)
	print("The area of the triangle of a given sides is : ",area)
else:
	print("Sorry S <= (side of a triangle). So, the area would be negative")