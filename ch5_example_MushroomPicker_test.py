import unittest
from example_ch5_MushroomPicker import solution

class example_tests(unittest.TestCase):
    def test_example1(self):
        A = [2, 3, 7, 5, 1, 3, 9]
        k = 4 
        m = 6
        self.assertEqual(solution(A, k, m), 25)

class correctness_tests(unittest.TestCase):
    def test_notbig1(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        k = 2
        m = 2
        self.assertEqual(solution(A, k, m), 12)

    def test_notbig2(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        k = 11
        m = 1
        self.assertEqual(solution(A, k, m), 25)

    def test_notbig3(self):
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        k = 9
        m = 9
        self.assertEqual(solution(A, k, m), 145)

    def test_manymovessmallarray(self):
        A = [1, 2, 3]
        k = 2
        m = 9
        self.assertEqual(solution(A, k, m), 6, msg="array length 3, position 2, 9 moves")

if __name__ == '__main__':
    unittest.main()
