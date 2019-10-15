class Node:
	def __init__(self, data = None):
		self.vals = data
		self.nextval = None
class SimpleLinkedList:
	def __init__(self):
		self.headval = None

	def printList(self):
		self.items = self.headval
		while self.items is not None:
			print(self.items.vals)
			self.items = self.items.nextval

lst = SimpleLinkedList()
lst.headval = Node("Abhishek")
val2 = Node("Soni")
val3 = Node("Age")
val4 = Node("20")

lst.headval.nextval = val2
val2.nextval = val3
val3.nextval = val4
lst.printList()
