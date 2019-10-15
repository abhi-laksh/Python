#--- DATE : May 26, 2019 | 13:04:01
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): 
about='Array Operation'
print('About :' + about)

class Array():
	def __init__(self , row , col=0):
		if (isinstance(row , int) and isinstance(col , int)) and (row>=0 and col >=0):
			self._rows = row
			self._cols = col
			if self._cols == 0:
				self._size = row
				self._arr1d = [None for i in range(self._rows)]
				2dArr = False
			else:
				self._size = self._rows * self._cols
				self._arr2d = [[None] * self._cols for i in range(self._rows)]
				arr2d = True
		else:
			raise ValueError("Rows and Cols must be integers")
	def __len__(self):
		return self._size
	def __getitem__(self , indRow , indCol = 0):
		if 2dArr and indCol >= 0:
			return self._arr2d[indRow][indCol]
		else:
			return self._arr1d[indRow]
	