import unittest
from ch4_FrogRiverOne import solution

class example_tests(unittest.TestCase):
    def test_example1(self):
        X = 5 
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        self.assertEqual(solution(X, A), 5)

if __name__ == '__main__':
    unittest.main()

