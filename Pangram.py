def is_pangram():
	abc = 'abcdefghijklmnopqrstuvwxyz '
	xyz = list(abc)
	pang = 'The quick brown fox jumps over the lazy dog'
	new_pang = pang.lower()
	newer_pang = list(pang)
	final = []
	for i in newer_pang:
		if i in newer _pang:
			final.append("yup")
		else:
			final.append("nope")
			
	if "nope" in final:
		print "not Pangram"
	else:
		print "Yay! is PANGRAM!!"		
	
is_pangram()