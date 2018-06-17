import unittest
from ch5_CountDiv import solution

class example_tests(unittest.TestCase):
    def test_example1(self):
        A = 6
        B = 11
        K = 2
        self.assertEqual(solution(A, B, K), 3, msg= "example test")

class correctness_tests(unittest.TestCase):
    def test_smallrangesmalldivisor(self):
        A = 1
        B = 4
        K = 2
        self.assertEqual(solution(A, B, K), 2, msg= "small range, small divisor")

    def test_smallrangelargedivisor(self):
        A = 1
        B = 3
        K = 50
        self.assertEqual(solution(A, B, K), 0, msg="small range, divisor oustside of range")
    
    def test_mediumrangelargedivisor(self):
        A = 1
        B = 12
        K = 13
        self.assertEqual(solution(A, B, K), 0, msg= "medium range, no divisible integers")

    def extrem_ifempty(self):
        A = 10
        B = 10
        K = 5
        self.assertEqual(solution(A, B, K), 1, msg= "extreme, empty")

if __name__ == '__main__':
    unittest.main()

