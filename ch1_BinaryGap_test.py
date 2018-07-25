import unittest
from ch1_BinaryGap import solution

class example_tests(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(solution(1041), 5)

    def test_example2(self):
        self.assertEqual(solution(15), 0)

class correctness_tests(unittest.TestCase):
    def test_extremes(self):
        self.assertEqual(solution(1), 0)
        self.assertEqual(solution(5), 1)
        self.assertEqual(solution(2147483647), 0)

    def test_trailing_zeroes(self):
        self.assertEqual(solution(6), 0)
        self.assertEqual(solution(328), 2)

    def test_power_of_2(self):
        self.assertEqual(solution(5), 1)
        self.assertEqual(solution(16), 0)
        self.assertEqual(solution(1024), 0)

    def test_simple1(self):
        self.assertEqual(solution(9), 2)
        self.assertEqual(solution(11), 1)

    def test_simple2(self):
        self.assertEqual(solution(19), 2)
        self.assertEqual(solution(42), 0)

    def test_simple3(self):
        self.assertEqual(solution(1162), 3)
        self.assertEqual(solution(5), 1)

    def test_medium1(self):
        self.assertEqual(solution(51712), 2)
        self.assertEqual(solution(20), 1)

    def test_medium2(self):
        self.assertEqual(solution(561892), 3)
        self.assertEqual(solution(9), 2)

    def test_medium3(self):
        self.assertEqual(solution(66561), 9)

    def test_large1(self):
        self.assertEqual(solution(6291457), 20)
        
    def test_large2(self):
        self.assertEqual(solution(74901729), 4)
        
    def test_large3(self):
        self.assertEqual(solution(805306373), 25)
           
    def test_large4(self):
        self.assertEqual(solution(1376796946), 5)
       
    def test_large5(self):
        self.assertEqual(solution(1073741825), 29)

    def test_large6(self):
        self.assertEqual(solution(1610612737), 28)      

if __name__ == '__main__':
    unittest.main()