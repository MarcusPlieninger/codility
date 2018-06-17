import unittest
from ch5_PassingCars import solution

class example_tests(unittest.TestCase):
    def test_example1(self):
        A = [0, 1, 0, 1, 1]
        self.assertEqual(solution(A), [(0,1), (0,3), (0,4), (2,3), (2,4)], msg= "example test")

if __name__ == '__main__':
    unittest.main()