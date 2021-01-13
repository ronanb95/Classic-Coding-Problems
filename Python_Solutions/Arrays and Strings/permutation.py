#bac,cab,abc are all permutations of abc
import collections
import unittest

def permutation(s1, s2):
	
	if len(s1) != len(s2):
		return False

	s1_letters = collections.Counter(s1)
	s2_letters = collections.Counter(s2)

	if s1_letters == s2_letters:
		return True

	return False
	

class Test(unittest.TestCase):

	dataT = [("ronan","nanor"),("abcd0","0acbd"),(" ", " ")]
	dataF = [("ronan","ronaq"),("gareth","garets")]

	def test_permutation(self):
		#true check
		for data in self.dataT:
			actual = permutation(*data)
			self.assertTrue(actual)
		#False check
		for data in self.dataF:
			actual = permutation(*data)
			self.assertFalse(actual)

if __name__ == "__main__":
	unittest.main()







	 

