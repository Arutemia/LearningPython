import pytest
from seasons import Seasons
from datetime import date, timedelta

def test_invalid_date():
	with pytest.raises(SystemExit):
		Seasons("Invalid date")

def test_date_calculator_one_day():
	yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
	user = Seasons(yesterday)
	assert "One thousand, four hundred forty minutes" in user.date_calculator()
