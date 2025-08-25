import random
import string

num = int(input('Enter the number of character you want to generate: '))

all_character = ''

is_l_letter = input('Enter y if you want to use small letter: ')
if (is_l_letter == 'y'):
	all_character += 'abcdefghijklmnopqrstuvwxyz'

is_u_letter = input('Enter y if you want to use capital letter: ')
if (is_u_letter == 'y'):
	all_character += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

is_digits = input('Enter y if you want to use digits: ')
if (is_digits == 'y'):
	all_character += '0123456789'

is_special = input('Enter y if you want to use special characters: ')
if (is_special == 'y'):
	all_character += "`-=[]\\;',./~!@#$%^&*()_+{}|:\"<>?"

generated = ''.join(random.choices(all_character, k = num))

print ("Generated password: " + generated)
