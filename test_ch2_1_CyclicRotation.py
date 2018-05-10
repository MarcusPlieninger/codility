import unittest
from ch2_1_CyclicRotation import solution

class example_tests(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])

    def test_example2(self):
        self.assertEqual(solution([1, 2, 3, 4], 4), [1, 2, 3, 4])     

if __name__ == '__main__':
    unittest.main()