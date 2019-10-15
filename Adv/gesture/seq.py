def adding():
    arr=[]
    while True:
        elem=int(input("Enter a number : "))
        arr.append(elem)
        ask=str(input("Continue  ?? ( Y / N ) "))[0].lower()
        if ask=='y':
            continue
        else:
            break
    return arr


array=adding()
print(array)