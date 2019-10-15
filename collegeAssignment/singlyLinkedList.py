#--- DATE : April 08, 2019 | 23:32:49
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): Single Linked List

"""
	-------------------------------------------
		Print Details About Code In Console
	-------------------------------------------
"""

class SingleLinkedList(object):
	class _Node(object):
		__slots__ = "_data" , "_next"
		def __init__(self ,item=None):
			self._data = item
			self._next = None

	def __init__(self):
		self._head = None
		self._size = 0
	
	def __len__(self):
		return self._size

	def _isEmpty(self):
		return self._head == None
	

	""" 
		----------------------------------------------
			Insert Opertions of Singly Linked List      
		----------------------------------------------
	"""	
	def insertEnd(self , item):
		if self._isEmpty():
			self._head = self._Node(item)
			self._size+=1
		else:
			last = self._head
			new = self._Node(item)
			while last._next !=None:
				last = last._next
			last._next = new
			self._size+=1

	def insertBeg(self , item):
		if self._isEmpty():
			self._head = self._Node(item)
			self._size+=1
		else:
			new = self._Node(item)
			new._next , self._head = self._head , new
			self._size +=1

	def insertBtw(self , item , nodePrev , nodeNext):
		if self._isEmpty():
			self._head = self._Node(item)
			self._size+=1
		elif (nodePrev == self._head._data or nodeNext == self._head._data) and self._head._next is None:
			new = self._Node(item)
			self._head._next = new
			self._size+=1
		else:
			find = self._head
			prev = self._head
			while find._next is not None:
				if prev._data == nodePrev:
					break
				else:
					prev = find
					find = find._next
			if (find._data == nodeNext):
				new = self._Node(item)
				prev._next, new._next = new , find
				self._size+=1
			else:
				print("Either of node is missing !")

	def insertBefore(self , item , node):
		if self._isEmpty():
			self._head = self._Node(item)
			self._size+=1
		elif node == self._head._data:
			new = self._Node(item)
			self._head , new._next = new , self._head
			self._size+=1
		else:
			find = self._head
			prev = self._head
			while find._next is not None:
				if find._data == node:
					break
				else:
					prev= find
					find = find._next
			if find._next == None and find._data !=node:
				print("Item Is Not present in list !")
			else:
				new = self._Node(item)
				prev._next , new._next = new , find
				self._size+=1
	def insertAfter(self , item ,data):
		if self._isEmpty():
			self._head = self._Node(data)
		elif item == self._head._data:
			new = self._Node(data)
			self._head._next = new
		else:
			curr = self._head 
			nextt = self._head
			while nextt._next is not None:
				if curr._data == item:
					break
				else:
					curr = nextt
					nextt = nextt._next
			new = self._Node(data)
			curr._next , new._next = new , nextt
			self._size+=1

	def printList(self):
		if self._isEmpty():
			print("Empty List !")
		else:
			cur = self._head
			while cur is not None:
				print(cur._data)
				cur = cur._next
	""" 
		---------------------------------------------------------------------------
			Delete Operation On Singly Linked List
		---------------------------------------------------------------------------
	"""	
	def deleteBeg(self):
		if self._isEmpty():
			print("List is empty !")
		else:
			cur , self._head = self._head , self._head._next
			self._size -=1
			del cur
	def deleteLast(self):
		if self._isEmpty():
			print("List is empty !")
		else:
			cur = self._head
			while cur._next._next != None:
				cur = cur._next
			cur._next = None
			self._size -=1
	def deleteAny(self , node):
		if self._isEmpty():
			print("List is empty !")
		elif node == self._head._data:
			print("Data found at first posn. Use 'deleteBeg()' instead !")
		else:
			cur = self._head
			find = self._head
			while find != None:
				if find._data == node:
					break
				else:
					cur = find
					find = find._next

			if find == None:
				print("Node is missing !")
			else:
				cur._next = find._next
				self._size -= 1

