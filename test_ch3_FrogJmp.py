import unittest
from ch3_FrogJmp import solution

class example_tests(unittest.TestCase):
    def test_example1(self):
        X = 10
        Y = 85
        D = 30
        self.assertEqual(solution(X, Y, D), 3)

class correctness_tests(unittest.TestCase):
    def test_simple1(self):
        X = 1
        Y = 3
        D = 1
        self.assertEqual(solution(X, Y, D), 2)       

    def test_simple2(self):
        X = 20
        Y = 79
        D = 20
        self.assertEqual(solution(X, Y, D), 3)

    def test_extreme_position(self): # no jump needed
        X = 11
        Y = 10
        D = 10
        self.assertEqual(solution(X, Y, D), 0)

    def test_small_extreme_jump(self): # one big jump
        X = 1
        Y = 6000
        D = 7000
        self.assertEqual(solution(X, Y, D), 1)

class performance_tests(unittest.TestCase):
    def test_many_jump1 (self): # many jumps, D = 2
        X = 1
        Y = 9999990000
        D = 2
        self.assertEqual(solution(X, Y, D), 4999995000)

    def test_many_jump2(self):  # many jumps, D = 99
        X = 500000
        Y = 9327146785
        D = 99
        self.assertEqual(solution(X, Y, D), 94208554)  

    def test_many_jump3(self): # many jumps, D = 1283
        X = 10
        Y = 999999999
        D = 1283
        self.assertEqual(solution(X, Y, D), 779424)

    def test_big_extreme_jump_jump(self): # maximal number of jumps
        X = 1
        Y = 999999999
        D = 30
        self.assertEqual(solution(X, Y, D), 33333334)

    def test_small_jumps (self): # many small jumps
        X = 1
        Y = 500000
        D = 5
        self.assertEqual(solution(X, Y, D), 100000)

if __name__ == '__main__':
    unittest.main()