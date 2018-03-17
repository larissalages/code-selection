def verify_len(post_code):
	
	len_code = len(post_code)

	if(len_code > 8 or len_code < 6):
		return False
	else:
		return True

def verify_outward(post_code):

	index_space = post_code.find(" ")

	if index_space == -1:
		return False;

	if(index_space > 4 or index_space < 2):
		return False

	#Always starts with an alphabetic character 
	if(post_code[0].isalpha() == False):
		return False

	#Only two characters in outward code
	if(index_space == 2):
		if(post_code[1].isdigit()):
			return True;
		else:
			return False;

	#Only three characters in outward code
	if(index_space == 3):
		if(post_code[1].isalpha() and post_code[2].isdigit()):
			return True
		elif(post_code[1].isdigit() and post_code[2].isdigit()):
			return True
		elif(post_code[1].isdigit() and post_code[2].isalpha()):
			return True
		else:
			return False

	#Four characters in outward code
	if(index_space == 4):
		if(post_code[1].isalpha() and post_code[2].isdigit()):
			if(post_code[3].isalpha()):
				return True
			elif(post_code[3].isdigit()):
				return True
		else:
			return False

def verify_inward(post_code):

	index_space = post_code.find(" ")

	if index_space == -1:
		return False

	len_inward = len(post_code) - index_space -1

	if(len_inward != 3):
		return False

	last_index = len(post_code) - 1
	if(post_code[last_index].isalpha() and post_code[last_index-1].isalpha() and post_code[last_index-2].isdigit()):
		return True
	else:
		return False

