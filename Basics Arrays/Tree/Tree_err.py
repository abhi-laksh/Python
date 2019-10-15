#--- DATE : April 07, 2019 | 16:43:46
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): 
about='Implementation of Binary tree'
print('About :' + about)


class Tree(object):

	class _Node(object):
		__slots__ = "_data" , "_left" , "_right" , "_parent" , "_postion"
		def __init__(self , item , par = None):
			self._data = item 
			self._left = self._right = None
			self._parent = par
			self._postion = 0

	def __init__(self):
		self._root = None
		self._size = 0

	def __len__(self):
		return self._size

	def isEmpty(self):
		return self._size == 0 or self._root == None

	def isParent(self,item):
		return self._root._data == item
	
	def isLeaf(self,item):
		return item._left == None and item._right == None
		
	def getSibling(self,p):
		if not self.isEmpty():
			if p._left != None:
				return p._right._data
			if p._right != None:
				return p._left._data

	def getRoot(self):
		if not self.isEmpty(): return self._root

	def getChildren(self , p):
		children = []
		if not self.isEmpty():
			if not self.isLeaf(p):
				if p._left == None:
					children.append(p._right._data)
				elif p._right == None:
					children.append(p._left._data)
				else:
					children.append(p._left._data)
					children.append(p._right._data)
				return children
			else:
				raise ValueError("No children ! The given node is leaf node.")
		else:
			raise ValueError("The Tree is empty")

	def addRoot(self,item):
		if self.isEmpty():
			self._root = self._Node(item)

	def addLeft(self , p, item):
		new = self._Node(item,p)
		p._left = new
		
	def addRight(self , p, item):
		new = self._Node(item,p)
		p._right = new

	def display(self):
		if not self.isEmpty():
			self._displayTree(self._root)

	def _displayTree(self,node):
		if node != None:
			print(self._displayTree(node._left))
			print(str(node._data)) + " "
			print(self._displayTree(node._right))

ob = Tree()
ob.addRoot("A")
ob.addLeft("A","B")
ob.addRight("A","C")
ob.display()