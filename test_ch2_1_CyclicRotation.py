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
        self.assertEqual(solution([-999, -800, -700, -600, -500, -400, -300,
                                  -200, -100, 0, 100, 200, 300, 400, 500, 600, 
                                  700, 800, 900, 999], 10), 
                         [100, 200, 300, 400, 500, 600, 700, 800, 900, 999, 
                          -999, -800, -700, -600, -500, -400, -300, -200, 
                          -100, 0])

class correctness_tests(unittest.TestCase):
    def test_extreme_empty(self):
        # empty array
        self.assertEqual(solution([], 0), [])
        self.assertEqual(solution([], 3), [])

    def test_single(self):
        # one element, 0 <= K <= 5
        self.assertEqual(solution([1], 0), [1])
        self.assertEqual(solution([1], 3), [1])
        self.assertEqual(solution([1], 5), [1])
    
    def test_double(self):
        # two elements, K <= N
        self.assertEqual(solution([0, 1], 0), [1,0])
        self.assertEqual(solution([0, 1], 2), [1,0])

    def test_small1(self):
        # small functional tets, K < N
        self.assertEqual(solution([0, 3, 5, 7, 9], 4), [3, 5, 7, 9, 0])
        self.assertEqual(solution([0, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 1), 
                         [21, 0, 3, 5, 7, 9, 11, 13, 15, 17, 19])

    def test_small2(self): 
        # small functional tests, K >= N
        self.assertEqual(solution([0, 3, 5, 7, 9], 4), [3, 5, 7, 9, 0])
        self.assertEqual(solution([0, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 1), 
                         [21, 0, 3, 5, 7, 9, 11, 13, 15, 17, 19])

    def test_small_random_all_rotations(self):
        # small random sequence, all rotations, N = 15
        self.assertEqual(solution([0, 0, 0], 1), [0, 0, 0])

    def test_medium_random(self):
        # medium random sequence, N = 100
        self.assertEqual(solution([0, 0, 0], 1), [0, 0, 0])

    def test_maximal(self):
        #maximal N and K
        self.assertEqual(solution([0, 0, 0], 1), [0, 0, 0])


if __name__ == '__main__':
    unittest.main()