from plates import is_valid


def test_starts_with_two_letters():
	assert is_valid("CS50") == True
	assert is_valid("C050") == False
	
def test_maximum_of_6_characters():
	assert is_valid("PYTHON") == True
	assert is_valid("PYTHON1") == False
	
def test_minimum_of_2_characters():
	assert is_valid("CS50") == True
	assert is_valid("1") == False
	
def test_no_number_in_the_middle_of_a_plate():
	assert is_valid("CS50P") == False
	
def test_only_alphanumeric():
	assert is_valid("CS50") == True
	assert is_valid(". ?!#$%") == False
	
