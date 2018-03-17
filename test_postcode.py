import unittest
from postcode import *  

class validatePostCode(unittest.TestCase):

	def test_len_correct(self):  

		post_code = 'SW1W 0NY'

		result = verify_len(post_code)
        
		self.assertTrue(result)

	def test_len_NOT_correct(self):

		post_code = 'SW1W  0NY'

		result = verify_len(post_code)
        
		self.assertFalse(result)

	def test_outward_correct(self):

		post_code = 'SW14 0NY'

		result = verify_outward(post_code)
        
		self.assertTrue(result)

	def test_outward_NOT_correct(self):

		post_code = 'S114 0NY'

		result = verify_outward(post_code)
        
		self.assertFalse(result)

	def test_inward_correct(self):

		post_code = 'SW1W 0NY'

		result = verify_inward(post_code)

		self.assertTrue(result) 

	def test_inward_correct(self):

		post_code = 'SW1W 0NY'

		result = verify_inward(post_code)

		self.assertTrue(result) 

	def test_inward_NOT_correct(self):

		post_code = 'SW1W 0N5'

		result = verify_inward(post_code)

		self.assertFalse(result) 

if __name__ == '__main__':
    unittest.main()