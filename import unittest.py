import unittest
from tdd import test_solution
class test_solution(unittest.Testcase):
	def test_addition(self):
		self.assertTrue(test_solution.solution(20,20,"+"),40)

	def test_multiplication(self):
		self.assertTrue(test_solution.solution(20,20,"*"),400)

	def test_division(self):
		self.assertTrue(test_solution.solution(20,20,"/"),1)
	def test_subtraction (self):
		self.assertTrue(test_solution.solution(20,20,"-"),0)

	def test_addition (self):
		self.assetFalse(test_solution.solution(20,20),10)


	if __name__=="__main__":
		unittest.main()
		