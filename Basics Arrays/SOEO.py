a=int(input('Enter a number : '))
b=int(input('Enter a number : '))
oddEve=str(input("Select odd or even (O/E) : "))[0]

s=0
for i in range(a,b+1):

    if oddEve=="e":
        isEve=i%2
        if isEve==0:
            s=s+i
            
            
    elif oddEve=="o":
        isOdd=i%2
        if isOdd!=0:
            s=s+i
            
    else:
        print("Please select either odd/even")
        # return True #Only works in functions not in loop

if oddEve=="e":
    print("Sum of even numbers in a given range is : ",s)

else :
    print("Sum of odd numbers in a given range is : ",s)
