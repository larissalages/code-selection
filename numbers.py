def print_numbers():

	str_result = ""

	for i in range(100):
		if (i % 3 == 0 and i % 5 == 0):
			print "ThreeFive"
			str_result += "ThreeFive\n"
		elif (i % 3 == 0):
			print "Three"
			str_result += "Three\n"
		elif (i % 5 == 0):
			print "Five"
			str_result += "Five\n"
		else:
			print str(i)
			str_result += str(i)+"\n"

	return str_result
