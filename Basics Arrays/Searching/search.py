def bubbly_sortish(data):
    for nums in range(len(data)**2):
        i, j = nums//len(data), nums%len(data)
        if i<j and data[i] > data[j]:
            data[i], data[j] = data[j], data[i]

A = [5, 1, 2, 3, 5, 6, 10]
bubbly_sortish(A)

print(A) 