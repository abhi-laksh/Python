# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.

class getPrint:
	
	def getString(self):
		self.string=str(input("Enter a string : "))
		print("You entered : " , self.string)
	def setString(self):
		print(self.string.upper())

x= getPrint()
x.getString()
x.setString()