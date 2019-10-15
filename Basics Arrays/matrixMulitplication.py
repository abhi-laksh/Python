# MULTIPLYING A SQUARE MATRIX (3X3)

a = int(input("Enter number of rows or colmns ? : "))
mat1 = []
# For mat1
row1 = []
row2 = []
row3 = []

mat1 = [row1, row2, row3]
# For mat2
row4 = []
row5 = []
row6 = []
mat2 = [row4, row5, row6]

ind = 0
result = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
for i in range(1, a + 1):
    # For mat2
    a = int(input("Enter number for row 1 for matrix 1 : "))
    row1.append(a)
    b = int(input("Enter number for row 2 for matrix 1 : "))
    row2.append(b)
    c = int(input("Enter number for row 3 for  matrix 1 : "))
    row3.append(c)
    # For mat2
    d = int(input("Enter number for row 4  for  matrix 2 : "))
    row4.append(d)
    e = int(input("Enter number for row 5  for  matrix 2 : "))
    row5.append(e)
    f = int(input("Enter number for row 6  for  matrix 2 : "))
    row6.append(f)
multiply = True
for i in range(len(mat1)):
    for j in range(len(mat2[0])):
        for k in range(len(mat2)):
            result[i][j] += mat1[i][k]*mat2[k][j]

print(result)