a = int(input("Enter a number a rows : "))
arr = []
for i in range(a):
    arr.append([])
    arr[i].append(1)
    for j in range(1, i):
        arr[i].append(arr[i-1][j-1]+arr[i-1][j])
    if(a != 0):
        arr[i].append(1)
for i in range(a):
    print("    "*(a-i), end=" ", sep=" ")
    for j in range(0, i+1):
        print('{0:6}'.format(arr[i][j]), end=" ", sep=" ")
    print()
