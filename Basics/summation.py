n=int(input("Enter nth term  : "))
def sumOfn(a):
    s1=0

    for i in range(1,a+1):
        s1+=i
    return s1
def sumOfn2(a):
    s2=0
    for i in range(1,a+1):
        s2+=i**2
    return s2
def sumOfn3(a):
    s3=0
    for i in range(1,a+1):
        s3+=i**3
    return s3

sum1=sumOfn(n)
sum2=sumOfn2(n)
sum3=sumOfn3(n)
print(sum1,sum2,sum3)