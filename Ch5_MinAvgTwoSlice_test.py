import unittest
from ch5_MinAvgTwoSlice import solution

class example_tests(unittest.TestCase):
    def test_example1(self):
        A = [4, 2, 2, 5, 1, 5, 8]
        self.assertEqual(solution(A), 1, msg= "example test")

class performance_tests(unittest.TestCase):
    def test_largegap(self):
        A = [1, 100, 10, 20]
        self.assertEqual(solution(A), 2, msg= "large gap")

if __name__ == '__main__':
    unittest.main()
