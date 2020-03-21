#!/usr/bin/env python
from person import Person
from datetime import datetime
rperson = Person()

print('gender: ' + rperson.gender)
print('name: ' + rperson.name)
print('birth_date: ' + str(rperson.birth_date))
print('cpr: ' + rperson.cpr)
print('phone: +45' + rperson.phone)
print('card: ' + str(rperson.cc.card_num))
print('exp: ' + str(rperson.cc.exp_date.strftime('%m-%y')) + ' (mm-yy)')
print('cvv: ' + str(rperson.cc.cvv))
