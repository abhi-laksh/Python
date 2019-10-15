# PRINT A SQUARE MATRIX (3X3)

a = int(input("Enter number of rows or colmns ? : "))
mat = []

row1 = []
row2 = []
row3 = []
ind = 0

for i in range(1, a + 1):
    a = int(input("Enter number for row 1 : "))
    b = int(input("Enter number for row 2 : "))
    c = int(input("Enter number for row 3 : "))
    row1.append(a)
    row2.append(b)
    row3.append(c)

mat.append(row1)
mat.append(row2)
mat.append(row3)

print(mat[0])
print(mat[1])
print(mat[2])
