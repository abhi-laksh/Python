#--- DATE : April 08, 2019 | 23:32:49
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): Single Linked List

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

	def display(self):
		if self._isEmpty():
			print("List is Empty")
		else:
			cur = self._head
			while cur != None:
				print(" [" , cur._data , end = " ] --> ")
				cur = cur._next
			print(end="[__]\n\n")

	def isPresent(self , node):
		if not self.isEmpty():
			cur = self._head
			found = False
			while cur != None:
				if cur._data == node:
					found = True
					break
				else:
					cur = cur._next
			return found
		else:
			print("Can't Check Presence ! List is Empty !")
	# --------------------------------------------
	# 	Insert Opertions of Singly Linked List      
	# --------------------------------------------
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

	# -------------------------------------------
	# 	Delete Operation On Singly Linked List   
	# -------------------------------------------
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
	#----------------------
	# 	Extra Opertions    
	#----------------------
	def reverseDisplay(self):
		newList = SingleLinkedList()
		cur = self._head
		while cur is not None:
			newList.insertBeg(cur._data)
			cur = cur._next
		newList.display()
		del newList
	def reverse(self):
		cur = self._head
		beforeCur = None
		nextCur = None
		while cur !=None :
			afterCur = cur._next
			cur._next = beforeCur
			beforeCur = cur
			cur = afterCur
		self._head = beforeCur
	def swap(self , nodeA , nodeB):
		if not self._isEmpty():
			nodeA._data , nodeB._data = nodeB._data , nodeA._data
		else:
			print("Can't Swap ! List is Empty !")
	#----------------------
	# 	Extra Opertions    
	#----------------------
	def sortList(self):
		if not self._isEmpty():
			i = 0
			while i < (len(self) - 1):
				cur = self._head
				while cur._next != None:
					afterCur = cur._next
					val = afterCur._data
					if cur._data > val:
						self.swap(cur , afterCur)
					else:
						cur = afterCur
				i+=1
		else:
			print("Can't Sort ! List is empty")

obj = SingleLinkedList()
obj.insertEnd('Q')
obj.insertEnd('W')
obj.insertEnd('E')
obj.insertEnd('R')
# obj.insertEnd(40)
obj.insertEnd('T')
obj.insertEnd('Y')
obj.insertEnd('U')
obj.insertEnd('I')
obj.insertEnd('O')
obj.insertEnd('P')
obj.insertEnd('A')
obj.insertEnd('S')
obj.insertEnd('D')
obj.insertEnd('F')
obj.insertEnd('G')
obj.insertEnd('H')
obj.insertEnd('J')
obj.insertEnd('K')
obj.insertEnd('L')
obj.insertEnd('Z')
obj.insertEnd('X')
obj.insertEnd('C')
obj.insertEnd('V')
obj.insertEnd('B')
obj.insertEnd('N')
obj.insertEnd('M')
# obj.display()
obj.sortList()
obj.display()
obj.reverseDisplay()
