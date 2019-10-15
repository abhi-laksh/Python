a=int(input("Enter number of items to add : "))
arr=[]
ind=0
for i in range(a):
    b=int(input("Enter elem"))
    arr=arr + [b]
print(arr)
rem=int(input("Enter number to remove : "))
# arr=arr- arr[2]

# for i in arr:
#     if i==rem:
#         # arr=arr[i] + arr
#         print(arr[i])
print(arr[rem])



