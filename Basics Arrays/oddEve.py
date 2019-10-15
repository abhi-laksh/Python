a=int(input("Enter number of elm in list : "))
arr=[]
eve=[]
odd=[]
ind=0
for i in range(1,a+1):
    b=int(input("Enter elem  : "))
    arr.append(b)
for j in arr:
    if(j%2==0):
        ind=arr.index(j)
        eve.append(j)
    else:
        odd.append(j)
ask=input("Enter to check odd OR eve (o/e) : ")[0]
if ask=="o":
    print(odd)
elif ask=="e":
    print(eve)
else:
    print("Unexpected keyword   ")
