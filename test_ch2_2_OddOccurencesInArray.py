import unittest
from ch2_2_OddOccurencesInArray import solution 

class example_tests(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solution([9,3,9,3,9,7,9]), 7)

if __name__ == '__main__':
    unittest.main()
