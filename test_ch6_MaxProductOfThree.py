'''
A non-empty array A consisting of N integers is given. The product of
 triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60

Your goal is to find the maximal product of any triplet.

Write a function:

def solution(A)

that, given a non-empty array A, returns the value of the maximal
product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is
maximal.

Assume that:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].
Complexity:

expected worst-case time complexity is O(N*log(N));
expected worst-case space complexity is O(1) (not counting the storage
required for input arguments).

'''
import unittest
from ch6_MaxProductOfThree import solution
import random

class exampletests (unittest.TestCase):
    def test_example1(self):
        A = [-3, 1, 2, -2, 5, 6]
        self.assertEqual(solution(A), 60, msg="example test")

class performance_tests(unittest.Testcase):

    def medium_range(self):
        A = [x + 1 for x in range(-1001, 1000)]
        self.assertEqual(solution(A), 999000000)
    def medium_random(self):

    def large_random(self):
        A = random.sample(range(-1001, 1000), 100000)
        A = 

    def large_range(self):

    def extreme_large(self):


if __name__ == 'main':
    unittest.main()
