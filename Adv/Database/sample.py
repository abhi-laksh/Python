












values=[[1,2,3,4,5,6,7,8,9,10],['a','v','c','d','d','d','g'],[12,32,45,8,5,26,652,6,5,9]]
dubList=list(map(tuple, zip(*values[1:])))
print(len(values[0]))
n=0
# for i in range(len(dubList)):
#     for j in range(len(dubList[i])):
#         dubList[i][j]=None

# for i in range(len(values)):
#     for j in range(len(values[i])):
#         dubList[j][i]=values[i][j]

sqlInsert = " VALUES ( " + ",".join(str(tuple(vals)) for vals in values) + " );"
print(dubList)