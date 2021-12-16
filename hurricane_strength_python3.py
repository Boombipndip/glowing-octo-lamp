#calculates strength of hurricane based on wind speed
#uses saffir-simpson scale

wind_speed = eval(input("How fast is the wind in MPH? > "))

if wind_speed < 74:
	print("It's not quite a hurricane")
elif wind_speed >= 74 and wind_speed <= 95:
	print("It's a category 1 hurricane")
elif wind_speed >= 96 and wind_speed <= 110:
	print("It's a category 2 hurricane")
elif wind_speed >= 111 and wind_speed <= 130:
	print("It's a category 3 hurricane")
elif wind_speed >= 131 and wind_speed <= 155:
	print("It's a category 4 hurricane")
else:
	print ("OH SHIT CATEGORY 5! See you in Oz")