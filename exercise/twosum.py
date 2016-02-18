def twosum(nums,target):
	print "pass"
import unittest
from two_sum import two_sum
class TwoSumTestSuite(unittest.TestCase):
	def test_list_range_4(self):
		res = two_sum([2,5,1,7],8)
		self.assertEqual(res,[2,3])

if __name__ == "__main__":
	unittest.main()