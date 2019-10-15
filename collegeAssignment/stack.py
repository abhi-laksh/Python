#--- DATE : June 01, 2019 | 00:56:23
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): 
about=''
print('About :' + about)

class Stack(object):
	"""docstring for Stack"""
	def __init__(self, n):
		self._size = n
		self._stack = [None for i in range(self._size)]
		self._top = -1
	def __len__(self):
		return self._size
	def _overflow(self):
		return self._top == self._size
	def _underflow(self):
		return self._top == -1
	def display(self):
		i = self._top
		while i >=0:
			print(self._stack[i])
			i-=1
	def insert(self , item):
		if self._overflow():
			print("Stack is full")
		else:
			self._top+=1
			self._stack[self._top] = item
	def delete(self):
		if self._underflow():
			print("Stack is Empty !")
		else:
			waste = self._stack[self._top] 
			self._top -= 1


def infToPostfix():
	ques = "a+b*c"
	