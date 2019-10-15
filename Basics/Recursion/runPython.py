#!/usr/bin/env python
# chmod +x runPython.py
from __future__ import print_function
from builtins import input
import os
def refresh(curDir):
	files = [each for each in os.listdir(curDir) if os.path.isfile(each) if ".py" in each and each!=os.path.basename(__file__)]
	for i,j in enumerate(files):
		print("\n" + str(i) + " = " + str(j))
	print("\ne = Exit")

	return(files)

def checkFile(curDir):
	while True:
		files = refresh(curDir)
		choice = input("\nEnter choice : ")
		try:
			if 0 <= int(choice) <= (len(files) - 1):
				print("\n---  E X E C U T I O N  O F  T H E  C H O S E N  F I L E   ---\n")
				os.system("py " + files[int(choice)])
				print("\n----  Code Ends Here   ----\n")
			else:
				print("\nBad Choice ! Choose the respective option .")
		except ValueError:
			if choice=="e":
				break
			else:
				print("\nBad Choice ! Choose the respective option .")
def main():
	curDir = os.getcwd()
	checkFile(curDir)
if __name__ == "__main__":
	main()