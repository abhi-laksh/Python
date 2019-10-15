sen=str(input("Enter a sentence : ")).replace(" ","")
# sen=str(input("Enter a sentence : ")).lower()
alpha="abcdefghijklmnopqrstuvwxyz"
caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a=0
b=0
for i in sen:
    if i.islower():
        sm=alpha.index(i)
        b=b+sm+1
    else:
        cptl=caps.index(i)
        a=a+cptl+1
print(a+b)