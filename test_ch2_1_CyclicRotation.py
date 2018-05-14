import unittest
from ch2_1_CyclicRotation import solution

class example_tests(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])

    def test_example2(self):
        self.assertEqual(solution([1, 2, 3, 4], 4), [1, 2, 3, 4])
    
    def test_example3(self):
        self.assertEqual(soluation([0, 0, 0], 1), [0, 0, 0])

class my_tests(unittest.TestCase):
    def test_small(self):
        self.assertEqual(solution([1, 0], 6), [1, 0])

    def test_large(self):
        self.assertEqual(solution([-999, -800, -700, -600, -500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 999], 10), [100, 200, 300, 400, 500, 600, 700, 800, 900, 999, -999, -800, -700, -600, -500, -400, -300, -200, -100, 0])

if __name__ == '__main__':
    unittest.main()