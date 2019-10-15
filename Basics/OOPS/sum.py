class Vector:
	def __init__(self , a):
		self.cord = [0] * a

	def __len__(self):
		return len(self.cord)
	def __getitem__(self , j):
		return self.cord[j]
	def __setitem__(self , j , value):
		self.cord[j] = value
	def __add__(self , vect):
		if len(self.cord) != len(vect):
			raise ValueError("Dimensions are expected to be equal")
		result = Vector(len(self))
		for k in range(len(self)):
			result[k] = self[k] + vect[k]
		return result	
	def __str__(self):
		return "<" + str(self.cord)[1:-1] + ">" 
v = Vector(8)

v[2] = 10
v[-1] = 5
p = v + v
print(p)