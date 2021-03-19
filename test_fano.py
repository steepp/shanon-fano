import unittest
import fano


class TestFanoSplitting(unittest.TestCase):

    def test_sums_equal(self):
        s= [.20, .09, .01, .13, .12, .10, .04, .07, .01, .04, .02, .17]
        s.sort()
        part = fano.fano(s)
        l = sum(s[:part])
        r = sum(s[part:])
        self.assertEqual(l, 0.5, 'Should be 0.5') 
        self.assertEqual(r, 0.5, 'Should be 0.5') 

    def test_left_sum(self):
        t2 = [0.01, 0.01, 0.02, 0.04, 0.04, 0.07, 0.09, 0.1, 0.12]
        t2.sort()
        part = fano.fano(t2)
        l = sum(t2[:part])
        r = sum(t2[part:])
        self.assertEqual(l, 0.28, 'Should be 0.28') 
        self.assertEqual(r, 0.22, 'Should be 0.22') 

    def test_right_sum(self):
        t2 = [0.01, 0.01, 0.02, 0.04, 0.04, 0.07, 0.09]
        t2.sort()
        part = fano.fano(t2)
        l = sum(t2[:part])
        r = sum(t2[part:])
        self.assertEqual(r, 0.16, 'Should be 0.16') 
        self.assertEqual(l, 0.12, 'Should be 0.12') 


if __name__ == '__main__':
    unittest.main()
