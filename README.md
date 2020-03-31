# rnd_person_gen

Generate a random danish person.


### example usage
```
$ ./print_person.py
```
### note
- Names are from list of most common names
- Phone is eight-digits in range 22XXXXXX-99XXXXXX
- CPR is verified using [cpr_seq_list](https://github.com/c7i/cpr_seq_list)
- Credit card is verified using [Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm)
