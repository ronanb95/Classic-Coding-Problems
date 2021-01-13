import collections
import unittest

#Basically want to just check, if given a random string, it is possible to make a palindrome
#eg. tact coa ==> tacocat
#eg. racecar ==> racecar
#eg. rei d red ==> redired

def palidrome_perm(s):

	'''Method to check if a palidrome can be created from input'''
	
	if len(s) == 1 or len(s) == 2:
		return True

	s = "".join(s.split())
	s = s.lower()
	
	s1 = collections.Counter(s)
	print(s1)
	
	odds = 0
	for value in s1.values():
		if value % 2 != 0:
			odds -= 1
		else:
			odds += 1

	print(odds)

	return odds > 1


class Test(unittest.TestCase):

	dataT = ["tact coa", "racecar", "rei d red"]
	dataF = ["ronan","testcase", "abcdefg"]

	def test_palidrome_perm(self):
		#True test
		for data in self.dataT:
			actual = palidrome_perm(data)
			self.assertTrue(actual)
		#False test
		for data in self.dataF:
			actual = palidrome_perm(data)
			self.assertFalse(actual) 

if __name__ == "__main__":
	unittest.main()

# testcase => 


