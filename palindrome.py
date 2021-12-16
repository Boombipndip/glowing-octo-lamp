def palindrome(x):
	y = []
	nonos = ['.' , '?', '!', '&', ' ']
	for i in x.lower():
		if i not in nonos: 
			y += i
	print (y[::-1])	
	if y == y[::-1]:
		print ("It's a dang ol palindrome.")
	else:
		print ("I aint no linguist or nothin... but that aint a palindrome.")
		
palindrome("Was it a rat I saw?")
		
