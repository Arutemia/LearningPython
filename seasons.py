from datetime import date, datetime
import sys
import inflect


class Seasons:

	p = inflect.engine()

	def __init__(self, birth_date):
		try:
			self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
		except  ValueError:
			sys.exit("Invalid date")

	def __str__(self):
			return f"{self.birth_date}"

	def date_calculator(self):

		today = date.today()
		difference = today - self.birth_date
		minutes = difference.days * 24 * 60
		return Seasons.p.number_to_words(minutes, andword="").capitalize() + " minutes"


def main():
	birth_date = input("Date of Birth: ")
	user_date = Seasons(birth_date)
	print(user_date.date_calculator())

if __name__ == "__main__":
	main()
