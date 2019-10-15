#--- DATE : April 07, 2019 | 16:43:57
#---  ---  By Abhishek Soni 
#--- About (also write in below variable): Basic Queue Operation
about='Basic Queue Operation'
print('About : ' + about)

class CircularQueue(cqject):
	def __init__(self , n):
		self._size = n
		self._queue = [None for each in range(self._size)]
		self._front = self._rear = -1
	def __len__(self):
		return self._size
	def display(self):
		if self._front != -1 :
			j = self._front
			while True:
				print(self._queue[j])
				j = (j + 1) % self._size
				if j == (self._rear + 1) % self._size:
					break
		else:
			print("Queue is empty")
	
	def __overflow(self):
		return True if ((self._rear + 1) % self._size) == self._front else False
	
	def __underflow(self):
		return True if self._front == self._rear == -1 else False
	
	def insert(self , data):
		if self.__overflow():
			print("Queue is full ! Delete some items.")
		elif self._front == self._rear == -1:
			self._front = 0
			self._rear = 0
			self._queue[self._rear] = data
		else:
			self._rear = (self._rear + 1) % self._size
			self._queue[self._rear] = data
	
	def delete(self):
		if self.__underflow():
			print("Queue is empty")
		else:
			if self._front == self._rear:
				waste , self._queue[self._front] = self._queue[self._front] , None
				self._rear = self._front = -1
			else:
				waste , self._queue[self._front] = self._queue[self._front] , None
				self._front = (self._front + 1) % self._size
			print("F " , self._front)
			print("R" ,self._rear)
			

def main():
	cq = CircularQueue(5)
	while True:
		print("\nChoose : \n 1) Insert 2) Delete 3) Display 4) Exit \n ")
		choice = input("Enter choice : ")
		if (choice == "1"):
			item = input("Enter item to insert : ")
			cq.insert(item)
		elif (choice == "2"):
			print("\nDeleted Successfully\n")
			cq.delete()
		elif (choice == "3" ):
			print("\nYour Queue :") ,
			cq.display()
		elif (choice == "4"):
			print("\nByeee\n")
			break
		else:
			print("\nBad choice ! Choose Again ! \n")

if __name__ == "__main__":
	main()
