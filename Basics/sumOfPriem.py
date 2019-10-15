num=int(input("Enter number to check for prime : "))

def isPrime(n):
    if n>1:
        for i in range(2,n):
            if(n%i)==0:
                return False
        else:
            return True
    else:
        return False

def suming(n):
    s=0
    for i in range(1,n+1):
        check = isPrime(i)
        if check==1:
            s+=i
    print(s)
suming(num)