from random import randrange, choice, sample
from datetime import datetime
from calendar import monthrange
from sequence_list import SequenceList
from random_utils import random_date

class Person():
	def __init__(self):
		self.gender = self.get_gender()
		self.name = self.get_name()
		self.birth_date = self.get_birth_date()
		self.cpr = self.get_cpr(self.birth_date.strftime("%d%m%y"), self.gender)
		self.phone = self.get_phone() 
	
	def get_gender(self):
		return choice(['f', 'm'])

	def get_name(self): # todo: certain chars might not be supported
		first_names = open('names/' + self.gender + '_names.txt').read().splitlines()		
		last_names = open('names/last_names.txt').read().splitlines()		
		return choice(first_names) + ' ' + choice(last_names)

	def get_birth_date(self):
		from_date = datetime.strptime('1/1/1955', '%m/%d/%Y')
		to_date = datetime.strptime('1/1/2000', '%m/%d/%Y')
		return random_date(from_date, to_date).date()
		
	def get_cpr(self, six_digits, gender):
		return six_digits + '-' + choice(SequenceList(six_digits, gender))

	def get_phone(self):
		first_2 = randrange(22, 100) # First two digits start from 22
		remaining_6 = sample(range(0, 100), 3) # Remaining six randomly selected using sample to prevent chance of 6 identical digits
		return str(first_2) + ''.join(str(num).zfill(2) for num in remaining_6)
