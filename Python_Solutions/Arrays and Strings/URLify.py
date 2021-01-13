import unittest

def urlify(url):

	if url[-1].isspace():
		url = url.rstrip() + "%20"

	urlList = list(url)

	for i in range(len(url)):
		if urlList[i] == " ":
			urlList[i] = "%20"
	return "".join(urlList)

class Test(unittest.TestCase):

	dataT = [(('ronan byrne  '),('ronan%20byrne%20')), (('ronanbyrne '),('ronanbyrne%20'))]

	def test_urlify(self):
		for [test_string, expected] in self.dataT:
			actual = urlify(test_string)
			self.assertEqual(actual, expected)

if __name__ == '__main__':
	unittest.main()