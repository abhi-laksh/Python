a=input("enter something : ")
b=input("Enter something once more : ")
print("You entered : ",a ," ", b)

# a,b=b,a #without any temp variable

c=a
a=b
b=c

print("Swaped ",a," ",b)