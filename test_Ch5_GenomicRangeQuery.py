import unittest
from ch5_GenomicRangeQuery import solution

class example_tests(unittest.TestCase):
    def test_example1(self):
        S = "CAGCCTA"
        P = [2, 5, 0]
        Q = [4, 5, 6]
        self.assertEqual(solution(S, P, Q), [2, 4, 1], msg= "example test")

if __name__ == '__main__':
    unittest.main()