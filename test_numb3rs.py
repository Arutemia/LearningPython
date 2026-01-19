from numb3rs import validate

def test_valid():
	assert validate("125.250.35.2") == True
	assert validate("1.2.3.4") == True
	assert validate("255.255.255.255") == True
	assert validate("1.1.1.1") == True
	assert validate("0.0.0.0") == True

def test_invalid():
	assert validate("500.500.500.500") == False
	assert validate("001.002.003.004") == False
	assert validate("cat") == False
	assert validate("256.233.2.2") == False
	assert validate("255.256.2.2") == False
	assert validate("25.233.256.2") == False
	assert validate("26.233.2.256") == False

def test_missing_parts():
	assert validate("500..2.3") == False
	assert validate("1.2.3") == False
	assert validate("") == False
	assert validate("..1.1") == False