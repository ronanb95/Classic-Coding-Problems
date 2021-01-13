import unittest

def unique(s):

	if len(s) > 128:
		return False
	
	char_set = [False for i in range(128)]

	for char in s:
		val=ord(char)
		if char_set[val]:
			return False
		char_set[val] = True

	return True

class Test(unittest.TestCase):

	dataT = [("Rona"), ("abcd"), ("")]
	dataF = [("Ronan"), ("abca")]

	def test_unique(self):
		#true checks
		for test_s in self.dataT:
			actual = unique(test_s)
			self.assertTrue(actual)
		#false
		for test_s in self.dataF:
			actual = unique(test_s)
			self.assertFalse(actual)

if __name__ == "__main__":
	unittest.main()


