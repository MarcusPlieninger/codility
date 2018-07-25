import unittest
from ch2_OddOccurencesInArray import solution 

class example_tests(unittest.TestCase):
    def test_example1(self):
        A = [9,3,9,3,9,7,9]
        self.assertEqual(solution(A), 7)

if __name__ == '__main__':
    unittest.main()
