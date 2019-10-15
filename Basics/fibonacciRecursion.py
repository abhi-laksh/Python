n=int(input("Enter nth term for fibonacci : "))

def fibonacci(num):
    if num<=1:
        return num
    else:
        calc=fibonacci(num-1)+fibonacci(num-2)
        return calc

if n<0:
    print("Only Positive numbers please")
else:
    for i in range(n):
        print(fibonacci(i))