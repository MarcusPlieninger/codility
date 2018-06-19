import unittest
from ch5_GenomicRangeQuery import solution

class example_tests(unittest.TestCase):
    def test_example1(self):
        S = "CAGCCTA"
        P = [2, 5, 0]
        Q = [4, 5, 6]
        self.assertEqual(solution(S, P, Q), [2, 4, 1], msg= "example test")

class correctness_tests(unittest.TestCase):
    def extreme_single(self):
        S = "C"
        P = [0]
        Q = [0]
        self.assertEqual(solution(S, P, Q), [2], msg= "single character string")

    def extreme_double(self):
        S = "GT"
        P = [0]
        Q = [1]
        self.assertEqual(solution(S, P, Q), [2, 4, 1], msg= "double character string")

    def simple(self):
        S = "CAG"
        P = [0, 0]
        Q = [1, 2]
        self.assertEqual(solution(S, P, Q), [2, 4, 1], msg= "simple tests")

    def small_length_string(self):
        S = "CAGCCTA"
        P = [2, 5, 0]
        Q = [4, 5, 6]
        self.assertEqual(solution(S, P, Q), [2, 4, 1], msg= "small length simple string")

    def small_random(self):
        S = "CAGCCTA"
        P = [2, 5, 0]
        Q = [4, 5, 6]
        self.assertEqual(solution(S, P, Q), [2, 4, 1], msg= "small random string, length = ~300")

class performance_tests(unittest.TestCase):
    def almost_all_same_letters(self):
        S = "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGTCGGGGGGGGGGGGGGGGGGGGGCAGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
        P = [2, 5, 0]
        Q = [4, 5, 6]
        self.assertEqual(solution(S, P, Q), [2, 4, 1], msg= "example test")

    def large_random(self):
        S = "CGTACTGATCGCTACGACGAGACGAGACTTACACTACTACATACATCGACTACGATCAAGACAATACGACATGAAGGACATTACGACTACGACATACGACTACGACTAGC"
        P = [2, 5, 0]
        Q = [4, 5, 6]
        self.assertEqual(solution(S, P, Q), [2, 4, 1], msg= "example test")

    def extreme_large(self):
        S = "CTGACTGACGCTAGCTAGCTGCTAGCTAGCTCTCTAGCTCGCTCGATCGCGATCGCGAATCGCTCGGAGCTGCGAGCTGCGGCGGATCGAGCTGGCTATATCGATCGATCGATCGATGCTAGCTGATCCTAGCTAGCTGGAT"
        P = [2, 5, 0]
        Q = [4, 5, 6]
        self.assertEqual(solution(S, P, Q), [2, 4, 1], msg= "example test")

    
if __name__ == '__main__':
    unittest.main()