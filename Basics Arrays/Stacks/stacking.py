class Stack(object):
	def __init__(self , size):
		# SET top=-1 , take size and assign to variable
		self._top = -1
		self._size = size
		self._stack = [None for i in range(self._size)]
		#  setting precedence ... 
		self.__precedence = {"+" :1 , "-" : 1 , "*":2 , "/" :2,"%" :2 , "^":3}

	# Super Class : len(stack)  
	def __len__(self):
		return self._size
	# display the stack
	def display(self):
		if self._top != -1:
			stackTemp = [i for i in self._stack if i!=None]
			print(stackTemp)
		else:
			print("Stack is empty !")
	# returns True if stack is empty (underflow conditon) else False
	def isEmpty(self):
		if self._top == -1:
			return True
		else:
			return False
	# returns True if stack is full (overflow conditon) else False

	def isFull(self):
		if self._top == len(self._stack) -1:
			return True
		else:
			return False
	# puch operatioon for stack
	def push(self , item):

		if self.isFull():
			raise Exception("Overflow")
		else:
			self._top+=1
			self._stack[self._top] = item
	# pop operatioon for stack -> pops out the item which is at top of stack returns it

	def pop(self):
		
		if self.isEmpty():
			raise Exception("Underflow")
		else:
			self._stack[self._top] , item = None , self._stack[self._top]
			self._top-=1
			return item
	# returns the item which is at top of stack without popping
	def top(self):
		if self.isEmpty():
			raise Exception("Underflow")
		else:
			self.__tempStack = [i for i in self._stack if i!=None]
			topElem = self.__tempStack[-1]
			return topElem