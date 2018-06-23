import unittest
from ch6_MaxProductOfThree import solution

class exampletests (unittest.TestCase):
    def test_example1(self):
        A = [-3, 1, 2, -2, 5, 6]
        self.assertEqual(solution(A), 60, msg="example test")

if __name__ == 'main':
    unittest.main()
