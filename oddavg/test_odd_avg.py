import unittest
from odd_avg import OddAvg

class TestOddAverage(unittest.TestCase):
    def test_general(self):
        test_list = OddAvg()
        self.assertEqual(test_list.odd_average([2,4,1,9]), 5)
    def test_for_zero(self):
        test_list = OddAvg()
        self.assertEqual(test_list.odd_average([0,1,4]), 1)
    def test_for_odd_selection(self):
        test_list = OddAvg()
        self.assertEqual(test_list.odd_average([7,2,4,6,8]), 7)
    def test_for_only_non_odds(self):
        test_list = OddAvg()
        self.assertEqual(test_list.odd_average([4,4,2,0]), 0)
if __name__ == "__main__":
    unittest.main()
