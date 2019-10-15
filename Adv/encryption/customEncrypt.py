

import getpass

# pswd = getpass.getpass('Password:')
class birds:
	def __init__(self):
		print("a message from parent.")
	def setname(self,name):
		self.name = name
		return self.name
	def swim(self):
		print("Swims")

class parrot(birds):
	def __init__(self):
		super().__init__()
	def run(self):
		print("run ")

peg = parrot()
peg.setname("abhi")
peg.swim()
peg.run()