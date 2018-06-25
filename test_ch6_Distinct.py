'''
Write a function

def solution(A)

that, given an array A consisting of N integers, returns the number of
distinct values in array A.

Assume that:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range 
[−1,000,000..1,000,000].

For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1

the function should return 3, because there are 3 distinct values
appearing in array A, namely 1, 2 and 3.

Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(N) (not counting the storage
 required for input arguments).
'''
import unittest
from ch6_Distinct import solution

class example_tests(unittest.TestCase):
    def test_example1(self):
        A = [2, 1, 1, 3, 4, 1]
        self.assertEquals(solution(A), 3)

class correctness_tests(unittest.TestCase):
    def test_no_distinct(self):
        A = [5, 5, 5, 5, 5]
        self.assertEquals(solution(A), 0)
    def test_empty(self):
        A = []
        self.assertEquals(solution(A), 0)

class performance_tests(unittest.TestCase):
    def test_extremes(self):
        A = [-1000000, 3, 6, 2, 8, 0, -1000000, 1000000, 3, 2, 8, 0]
        self.assertEquals(solution(A), 7)

    def test_maxlength_eachdistinct(self):
        A = [x + 1 for x in range(0, 100001)]
        self.assertEquals(solution(A), 100000)

if __name__ == 'main':
    unittest.main()