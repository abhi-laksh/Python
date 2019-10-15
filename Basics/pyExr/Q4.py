#Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list and a tuple which contains every number.

data=input("Enter number ( seprerated by comas ) : ")

nums=data.split(",")

print("List is : ", nums)

tup=tuple(nums)

print("Tuple : ",tup)