#!/usr/bin/env python

from datetime import datetime, date

class SequenceList(list):	
	def __init__(self, six_digits, gender = '', birth_year = ''):
		(self.birth_date, self.gender) = (self.parse_six_digits(six_digits, birth_year), gender.lower())
		self.recursive_search()
	
	def recursive_search(self):
		''' populate list through recursive search and remove impossible numbers '''
		for i in range(1, 10000):
			self.append(str(i).zfill(4))
		
		self[:] = [x for x in self if self.matching_gender(int(x)) and self.matching_first_digit(x)]
		
		if self.birth_date < date(2007, 10, 1):
			''' since October 2007 personal identification numbers do not always validate using the check digit. [wikipedia] '''
			self[:] = [x for x in self if self.matching_modulus_11(x)]
		
	def matching_gender(self, seq_num):
		''' last digit even for women uneven for men '''
		if seq_num % 2 == 0 and self.gender == 'f': return True
		
		if seq_num % 2 == 1 and self.gender == 'm': return True
		
		if self.gender not in {'f', 'm'}: return True

	def matching_first_digit(self, seq_num):
		''' check if sequence number impossible by first digit (or 7th digit in cpr) and within specifc years '''
		first_digit = int(repr(seq_num)[1:-4])
		year = self.birth_date.year

		if year > 1999 and 0 <= first_digit <= 3: return False
		
		if year < 1937 and first_digit == 4: return False
		
		if 2000 > year > 1899 and 5 <= first_digit <= 8: return False
		
		if year < 1937 and first_digit == 9: return False

		return True

	def matching_modulus_11(self, seq_num):
		''' calculate check digit and validate with modulo operation (now depreciated) '''
		factors = [4, 3, 2, 7, 6, 5, 4, 3, 2, 1]
		cpr = self.birth_date.strftime("%d%m%y") + seq_num

		return True if sum(int(cpr_num) * factor for cpr_num, factor in zip(cpr, factors)) % 11 == 0 else False

	def parse_six_digits(self, six_digits, birth_year = ''):
		''' parse six digits into usable date object '''
		if len(six_digits) != 6:
			raise ValueError('date must be 6 digits (format: ddmmyy)')

		try:
			birth_day = datetime.strptime(six_digits,'%d%m%y')
		except ValueError as error:
			raise ValueError('invalid date format (format: ddmmyy)') from error

		if birth_year:
			''' use birth year if provided else assume target is < 100 years old '''
			try:
				parsed_year = datetime.strptime(birth_year, '%Y')
			except ValueError as error:
				raise ValueError('invalid year format (format: yyyy)') from error

			if not parsed_year.strftime('%y') == birth_day.strftime('%y'):
				raise ValueError('year must match last 2 digits of birth date')

			birth_day = birth_day.replace(year = int(birth_year))
		else:
			if birth_day.date() > datetime.today().date():
				birth_day = birth_day.replace(year = birth_day.year - 100)

		return birth_day.date()
