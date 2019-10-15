n=int(input("Enter nth term for fibonacci : "))
t1,t2=0,1
print(t1,t2,end=" , ")
for i in range(1,n+1):
    if i==1: 
        t1=i
    else:
        t3=t1+t2
        t1=t2
        t2=t3
        print(t3, end=" , ")
    
    