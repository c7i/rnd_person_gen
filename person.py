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
		self.cc = self.CreditCard()
	
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
		
	class CreditCard():
		def __init__(self):
			self.card_num = self.get_card_num()
			self.exp_date = self.get_exp_date()
			self.cvv = self.get_cvv()

		def get_card_num(self):
			''' MasterCard Bank Identification Number (BIN)
			    Six digits in range 510000-559999 or range 222100-272099 '''
			while(True):
				series_5_bin = randrange(510000, 559999)
				series_2_bin = randrange(222100, 272099)
				random_10_digits = sample(range(0, 100000), 2)

				use_series_2 = False # Newly introduced, rarely used

				if use_series_2:
					bin_num = str(choice([series_5_bin, series_2_bin]))
				else:
					bin_num = str(series_5_bin)
				
				remaining = ''.join(str(num).zfill(5) for num in random_10_digits)
				
				card_num = bin_num + remaining
				
				if self.verify_with_luhn(card_num):
					return card_num
				else:
					continue
				
		def verify_with_luhn(self, card_num):
			last_digit = int(card_num[-1:]) # last check digit

			card_num = [int(num) for num in list(card_num)]	# convert string to int list
			card_num = card_num[:-1] # remove last digit
			card_num = card_num[::-1] # reverse list
	
			for i in range(0, len(card_num), 2):
				card_num[i] *= 2
				if card_num[i] > 9: 
					card_num[i] -= 9
			
			return True if sum(card_num) * 9 % 10 == last_digit else False

		def get_exp_date(self):
			current_year = datetime.now().year
			
			from_date = datetime.strptime('1/' + str(current_year + 1), '%m/%Y')
			to_date = datetime.strptime('12/' + str(current_year + 6), '%m/%Y')	

			exp_date = random_date(from_date, to_date)

			# cc's always expires on last day of month
			last_day = monthrange(exp_date.year, exp_date.month)[1]
			exp_date = exp_date.replace(day = last_day) 
			
			return exp_date.date()

		def get_cvv(self):
			return str(randrange(1, 1000)).zfill(3)
