from um import count

def test_count_normal():
	assert count("I um, want you.") == 1
	assert count("Um, are we um, here?") == 2
	
def test_count_abnormal():
	assert count("um, Um, UM, uM") == 4
	assert count("album, yummy, mummy") == 0