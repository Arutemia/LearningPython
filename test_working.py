from working import convert
import pytest

def test_basic():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_with_minutes():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    assert convert("1:05 AM to 12 PM") == "01:05 to 12:00"

def test_invalid():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")