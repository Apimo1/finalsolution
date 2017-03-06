import unittest
from tdd import test_solution
class test_solution(unittest.Testcase):
	def test_addition(self):
		self.assertTrue(test_solution.solution(20,20,"+"),40)

	if __name__=="__main__":
		unittest.main()