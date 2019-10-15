x=int(input("Enter lower range : "))
y=int(input("Enter upper range : "))

def armstrongRange(a,b):
    arr=[]

    for i in range(a,b+1):
        num=i
        temp=num
        summ=0

        while temp>0:
            digit= temp%10
            summ+=digit**3
            temp//=10
        if summ==num:
            arr.append(summ)
        else:
            pass
    return arr

def sumIfYes(a,b):
    s=0
    armsNum=armstrongRange(a,b)
    for i in armsNum:
        s+=i
    return s

checking=sumIfYes(x,y)
print(checking)