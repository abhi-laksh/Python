#--- DATE : May 12, 2019 | 18:34:53
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): 
about='Linear Queue Implementation \n'
print('ABOUT :' + about.replace("" , " "))

class Queue(object):
	'''
		-----------------------------------------------	
			FIFO Principle
			Variables: front and rear ( Default -1 )
			Operation : insert , delete and display    
		-----------------------------------------------
	'''
	def __init__(self,n):
		self._front = self._rear = -1
		self._size = n
		self._queue = [None for i in range(self._size)]

	def _isEmpty(self):
		return self._front == self._rear == -1
	
	def _isFull(self):
		return self._rear == (self._size - 1)

	def display(self):
		if self._isEmpty():
			print("\nQueue is Empty !\n")
		else:
			for i in range(self._front , self._rear + 1):
				print(self._queue[i], end=" | ")
		print("\n")
	
	def insert(self , data):
		if self._isFull():
			print("\nCan't Insert ! Queue is full !\n")
		else:
			if self._front == self._rear == -1:
				self._rear = 0
				self._front = 0
				self._queue[self._rear] = data
			else:
				self._rear += 1
				self._queue[self._rear] = data
	
	def delete(self):
		if self._isEmpty():
			print("\nCan't Delete ! Queue is Empty !\n")
		else:
			if (self._front == self._rear == (self._size - 1)) or (self._front == self._rear == 0):
				waste ,self._queue[self._front] = self._queue[self._front] , None
				self._front = self._rear = -1
			else:
				waste , self._queue[self._front] = self._queue[self._front] , None
				self._front += 1
def main():
	# n = int(input("ENTER SIZE : "))
	n = 5
	# q = Queue(n)
	# q.insert(10)
	# q.insert(20)
	# q.insert(30)
	# q.insert(40)
	# q.insert(50)
	# q.display()
	# q.insert(60)
	# q.display()
	# q.delete()
	# q.delete()
	# q.display()
	# q.insert(70)

	lq = Queue(n)
	while True:
		print("\nChoose : \n 1) Insert 2) Delete 3) Display 4) Check Size e) Exit \n ")
		choice = input("Enter choice : ")
		if (choice == "1"):
			item = input("Enter item to insert : ")
			lq.insert(item)
		elif (choice == "2"):
			print("\nDeleted Successfully\n")
			lq.delete()
		elif (choice == "3" ):
			print("\nYour Queue :") ,
			lq.display()
		elif (choice == "e"):
			print("\nByeee\n")
			break
		else:
			print("\nBad choice ! Choose Again ! \n")

if __name__ == "__main__":
	main()

