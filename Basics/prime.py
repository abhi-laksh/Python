n=int(input("Enter number to check for prime : "))

def isPrime(n):
    for i in range(2,n):
        if (n%i)==0:
            return False
            break
    else:
        return True

check = isPrime(n)
if check==0:
    print(n," is not Prime")
else:
    print(n, " is Prime")
