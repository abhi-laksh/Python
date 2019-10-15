# - - - Coded in UTF-8
#  - - - This is a Linear Regression self-defined class (exported as a module named LR_module) 
#  
# !!! Created by @abhi-laksh aka Abhishek Soni
#     on 22nd December 2018 10:55:19 ( GMT + 5:30 )  !!!

class LinearReg:

	def sumIt(self,nums):
		self.s=0
		for n in nums:
			self.s+=n
		return self.s

	def intercept(self,x,y):
		self.n=len(x)

		# c = (Sx * Sxy) / ( (Sx)^2 - n * Sx^2 ) where S defines Summation , n -> no. of obv.

		# !! Since 'sumIt()' is a func.  of same class we use 'self.sumIt()' !!

		self.numer=( ( self.sumIt(x) ) * ( self.sumIt(x*y) ) ) - ( ( self.sumIt(x**2) ) * self.sumIt(y) )
		self.denumer= ( (self.sumIt(x)) ** 2 ) - ( self.n * self.sumIt(x**2) )
		self.c= self.numer / self.denumer
		return self.c

	def slope(self,x,y,c):

		# m = ( Sxy - c * Sx ) / Sx^2 where S defines Summation , c-> intercept

		self.numerator= self.sumIt(x*y) - (c * self.sumIt(x))
		self.denumerator= self.sumIt(x**2)

		self.m=self.numerator / self.denumerator
		return self.m

	def predict(self , x , c , m):
		self.y = m * x + c  # Equation of straight line 

		return self.y
