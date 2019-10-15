a=int(input("Enter number of items to add : "))
s=[]
for i in range(1,a+1):
    b=int(input("Enter number to add : "))
    s.append(b)
print(s)
c=int(input("Enter number to check : "))
for j in s:
    if sm==c:
        print((j))