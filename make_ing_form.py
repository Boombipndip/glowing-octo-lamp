#verb in infinitive form returns its present participle form. Test your function with words such as lie, see, move and hug. However, you must not expect such simple rules to work for all cases.
def make_ing_form(x):
	vowels = ['a','e','i','o','u']
	y = []
	for i in x:
		y += i
	print y
	if y[-1] == 'e' and y[-2] != 'e' and y[-2] != 'b' and y[-2] != 'i':
		y[-1] = 'i' 
		z = ''.join(y) + 'ng'
		print z
	elif y[-1] == 'e' and y[-2] == 'i':
		y[-2] = 'y'
		y[-1] = 'i'
		z = ''.join(y) + 'ng'
		print z
	elif y[-1] not in vowels and y[-2] in vowels and y[-3] not in vowels:
		z = ''.join(y) + str(y[-1]) + 'ing'
		print z
	else:
		z = ''.join(y) + 'ing'
		print z
	
		
		
		
make_ing_form('leg')