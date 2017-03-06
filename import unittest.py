import unittest
from tdd import test_solution
class test_solution(unittest.Testcase):
	def test_addition(self):
		self.assertTrue(test_solution.solution(20,20,"+"),40)

	def test_multiplication(self):
		self.assertTrue(test_solution.solution(20,20,"*"),400)

	if __name__=="__main__":
		unittest.main()