import pytest
from fuel import convert, gauge

def test_convert_normal_values():
	assert convert("3/4") == 75
	assert convert("1/2") == 50
	assert convert("1/100") == 1
	assert convert("99/100") == 99
	
def test_convert_zero_denominator():
	with pytest.raises(ZeroDivisionError):
		convert("1/0")
		
def test_not_numeric_values():
	with pytest.raises(ValueError):
		convert("cat/10")
	with pytest.raises(ValueError):
		convert("10/cat")
	with pytest.raises(ValueError):
		convert("one/ten")
		
def test_negative_values():
	with pytest.raises(ValueError):
		convert("-1/10")
		
def test_x_is_greater_than_y():
	with pytest.raises(ValueError):
		convert("100/1")
		
def test_for_gauge_full_and_empty():
	assert gauge(1) == "E"
	assert gauge(99) == "F"
	assert gauge(0) == "E"
	assert gauge(100) == "F"
	
def test_for_gauge_numbers():
	assert gauge(50) == "50%"
	assert gauge(33) == "33%"
