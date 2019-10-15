#--- DATE : May 22, 2019 | 22:15:53
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): Doubly Linked List
class DoublyLinkedList(object):
# --------------------------------------------------------------------------------
# 	Class for declaring nodes which will have two pointers ( _prev , _next )	
# --------------------------------------------------------------------------------
	class _Node(object):
		__slots__ = "_data" , "_prev" , "_next"
		def __init__(self , item=None):
			self._data = item
			self._prev = None
			self._next = None
# 	----------------------------------------------------------
# 		Class for declaring operations on DoublyLinkedList    	
# 	----------------------------------------------------------
	def __init__(self):
		self._head = None
		self._size = 0
	
	def __len__(self):
		return self._size

	def isEmpty(self):
		return self._head == None

	def display(self):
		if self.isEmpty():
			print("List is Empty")
		else:
			cur = self._head
			while cur != None:
				print(" [" , cur._data , end = " ] <--> ")
				cur = cur._next
			print(end="[__]\n\n")

	def isPresent(self , node , needPos = False):
		if not self.isEmpty():
			cur = self._head
			found = False
			posn = 0
			while cur != None:
				if cur._data == node:
					found = True
					break
				else:
					cur = cur._next
					posn +=1
			if needPos and found:
				return posn
			return found
		else:
			print("Can't Check Presence ! List is Empty !")
# --------------------------
# 	Inserting Operations 	   	
# --------------------------
	def insertBeg(self , item):
		new = self._Node(item)
		if self.isEmpty():
			self._head = new
			self._size += 1
		else:
			new._next , self._head  , self._head._prev =  self._head , new , new
			self._size += 1

	def insertEnd(self , item):
		new = self._Node(item)
		if self.isEmpty():
			self._head = new
			self._size += 1
		else:
			cur = self._head
			while cur._next != None:
				cur = cur._next
			cur._next , new._prev = new , cur
			self._size += 1
#-----------------------------------------------------------------------------------
# 	Insert btw 'prev' and 'cur' while only 'cur' is known ( Insert before 'cur' )     	
#----------------------------------------------------------------------------------- 
	def insertBefore(self , item , node):
		if self.isPresent(node):
			new = self._Node(item)
			cur = self._head
			prev = self._head
			while cur._data != node:
				prev = cur
				cur = cur._next
			prev._next , new._prev , cur._prev , new._next= new , prev , new , cur
			self._size += 1
		else:
			print("Node is not present.")
#-----------------------------------------------------------------------------------
# 	Insert btw 'cur' and 'after' while only 'cur' is known ( Insert after 'cur' )     	
#----------------------------------------------------------------------------------- 
	def insertAfter(self , item , node):
		if self.isPresent(node):
			new = self._Node(item)
			cur = self._head
			after = self._head
			while cur._data != node:
				cur = after
				after = after._next
			cur._next , new._prev ,  new._next , after._prev  = new , cur , after , new
			self._size += 1
			# after._prev , new._prev , cur._next , new._next= new , cur , new , after
		else:
			print("Node is not present.")
#------------------------------------------------------------------------------
# 	Insert btw 'nodeBefore' and 'nodeAfter' while strictly both are known.         	
#------------------------------------------------------------------------------ 
	def insertBtw(self , item , nodeBefore , nodeAfter):
		if self.isPresent(nodeBefore) and self.isPresent(nodeAfter):
			new = self._Node(item)
			cur = self._head
			after = self._head
			while cur._data != nodeBefore:
				cur = after
				after = after._next
			if after._data == nodeAfter:
				cur._next , new._prev ,  new._next , after._prev  = new , cur , after , new
				self._size += 1
			else:
				print("Nodes must be consecutive !")
		else:
			print("Node is not present.")
#-----------------------
# 	Delete operation
#-----------------------
	def deleteBeg(self):
		if self.isEmpty():
			print("List is empty !")
		else:
			waste , self._head = self._head , self._head._next
			del waste
			self._size -= 1

	def deleteEnd(self):
		if self.isEmpty():
			print("List is Empty")
		else:
			cur = self._head
			while cur._next._next != None:
				cur = cur._next
			waste , cur._next = cur._next , None
			del waste
			self._size -= 1

	def deleteAny(self , node):
		if self.isEmpty():
			print("List is Empty")
		else:
			if self.isPresent(node):
				cur = self._head
				prev = self._head
				while cur._data != node:
					prev = cur
					cur = cur._next
				if cur._next == None:
					print("Node is present at the end. Use 'deleteEnd' instead.")
				elif cur == self._head:
					print("Node is present at the begining. Use 'deleteBeg' instead.")
				else:
					prev._next , cur._next._prev = cur._next , prev
					del cur
					self._size -= 1
			else:
				print("Can't delete ! Node is not found")
#----------------------
# 	Extra operations
#----------------------
	def swap(self , nodeA , nodeB):
		if not self.isEmpty():
			nodeA._data , nodeB._data = nodeB._data , nodeA._data
		else:
			print("Can't Swap ! List is Empty !")

	def reverseDisplay(self):
		if not self.isEmpty():
			cur = self._head
			print(end=" [ ")
		#---------------
		#	Go to End    
		#---------------
			while cur._next!= None:
				cur = cur._next
		#------------------------
		#	Print End to Start   
		#------------------------
			while cur !=None:
				print(cur._data , end = " ] <--> [ ")
				cur = cur._prev
			print(end="__ ]\n")
		else:
			print("List is Empty !")

	def reverseList(self):
		if not self.isEmpty():
			newList = DoublyLinkedList()
			cur = self._head
			while cur !=None:
				newList.insertBeg(cur._data)
				cur = cur._next
			return newList
		else:
			print("List is Empty !")
	def reverse(self):
		if not self.isEmpty():
			cur = self._head
			prevCur = None
			nextCur = None
			while cur !=None :
				prevCur , cur._prev = cur._prev , cur._next
				cur._next , cur = prevCur , cur._prev
			self._head = prevCur._prev
		else:
			print("List is Empty !")
	def sortList(self):
		if not self.isEmpty():
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
obj = DoublyLinkedList()
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
obj.display()
# new = obj.reverseList()
obj.sortList()
obj.reverse()
obj.display()
obj.reverseDisplay()
