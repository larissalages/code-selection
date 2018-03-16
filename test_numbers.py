import unittest
from numbers import print_numbers 

class VerificarPrint(unittest.TestCase):
	def test_check_print_number(self):

		file  = open('expected_results_numbers.txt', 'r')
		print_test = file.read()  		

		prints_result = print_numbers()

		self.assertEqual(print_test,prints_result)