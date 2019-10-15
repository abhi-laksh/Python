#--- DATE : July 10, 2019 | 09:08:22
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): 
about=''
print('About :' + about)

class Tree:
	def __init__(self):
		self._root = None
		self._size = 0
	class _Node(object):
		__slots__ = "_data" , "_left" , "_right" , "_parent"
		def __init__(self , item , par = None):
			self._data = item 
			self._left = self._right = None
			self._parent = par
			self._postion = 0

	class Position:
		def __init__(self , container , node):
			self._container = container
			self._node = node
		def getData(self):
			return self._node._data

	def __len__(self):
		return self._size

	def isEmpty(self):
		return self._size == 0 or self._root == None

	def isParent(self,item):
		return self._root._data == item
	
	def isLeaf(self,item):
		return item._left == None and item._right == None
	
	def _validate(self):
		if not isinstance(p,self.Position):
			raise TypeError("p is not proper position")
		if p._container is not self:
			raise ValueError('p does not belong to this container')
		if p._node._parent is p._node:
			raise ValueError("p already exists")
		return p._node

	def _setPos(self,item):
		return self.Position(self,item) if item is not None else None

