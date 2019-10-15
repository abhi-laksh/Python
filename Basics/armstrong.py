num=int(input("Enter number to check for armstrong : "))
def isArmstrong(a):
    s= 0
    temp=a
    while temp>0:
        digit = temp % 10
        s+=digit**3
        temp//=10
    if s==num:
        return True
    else:
        return False

check=isArmstrong(num)
if check==1:
    print("armstrong")
else:
    print("No Armstrong")
