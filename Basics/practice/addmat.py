row=int(input("Enter number of rows : "))
col=int(input("Enter number of cols : "))

result=[]
# --- - --- - Creating Matrix   
def create(r,c):
	mat=[]
	for i in range(1,c+1):
		rowss=[]
		zeroes=[]

		mat.append(rowss)
		if len(result)!=c:
			result.append(zeroes)
		else:
			pass
		for j in range(1,r+1):
			a=int(input("Enter a number for rows : "))
			rowss.append(a)
			if len(zeroes)!=r:
				zeroes.append(0)
			else:
				pass
	return mat

mat1=create(row,col)
mat2=create(row,col)

print("Matrix A : ",mat1,"\n","Matrix B : ",mat2)
print(result)
# --- - --- - Adding Matrix   

def adding(matA, matB):
	for i in range(len(matA)):
		for j in range(len(matA[0])):
			result[i][j]= matA[i][j] + matB[i][j]
	

adding(mat1,mat2)

print("the answer is : \n",result)


def multiply(matA,matB):
	for i in range(len(matA)):
		for j in range(len(matB[0])):
			for k in range