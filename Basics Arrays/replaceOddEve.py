# CHECKING IF THERE IS EVEN IN A LIST AND REPLACING THE NUMBER TO ITS
# PREVIOUS CONSECUTIVE EVEN
n = int(input("Enter number of elements : "))
lst = []
indexx = 0
for i in range(1, n + 1):
    a = int(input("Enter number : "))
    lst.append(a)
print("Prev list : ", lst)
for i in lst:
    if i % 2 == 0:
        indexx = lst.index(i)
        lst[indexx] = i - 2
    else:
        pass
print("New list : ", lst)
