Peter = {'dog':'yg'}
Lily = {'cat':'hdj'}
Lucy = {'dog':'yjq'}
pets = [Peter,Lily,Lucy]
for pet in pets:
	print(pet)

print('\nP2')
favourite_places = {
	'dongjie':['SH','BJ'],
	'yangge':['ZZ','TG'],
	'YJQ':['WX','SZ','SH'],
	}
for username, places in favourite_places.items():
	print('\n' + username.title() + "'s favorite places are: ")
	for place in places:
		print('\t' + place)

print('\nP3')
favorite_numbers = {
	'zhao':[1,3],
	'qian':[2,4,6],
	'sun':[3,5,7],
	'li':[100,110,120],
	'he':[7],
	}
for name, numbers in favorite_numbers.items():
	 print('\n' + name.title() + "'s favorite numbers are:")
	 for number in numbers:
	 	print('\t' + str(number))

print('\nP4')
favorite_numbers = {
	'zhao':[1,3],
	'qian':[2,4,6],
	'sun':[3,5,7],
	'li':[100,110,120],
	'he':[7],
	}
for name, numbers in favorite_numbers.items():
	if len(numbers) > 1:
		print('\n' + name.title() + "'s favorite numbers are:")
		for number in numbers:
			print('\t' + str(number))
	elif len(numbers) == 1:
		print('\n' + name.title() + "'s favorite numbers is:")
		for number in numbers:
			print('\t' + str(number))
print('\nP5')
cities = {
	'shanghai':{
		'country':'china',
		'population':'1100W',
		'fact':'biggest city in China'
		},

	'beijing':{
		'country':'china',
		'population':'1000W',
		'fact':'captial of China',
		},

	'NewYork':{
		'country':'USA',
		'population':'900W',
		'fact':'very bustling',
		}
	}
for city, city_info in cities.items():
	print('\nCity: ' + city.title())
	print('\tCountry: ' + city_info['country'])
	print('\tPopulation: ' + city_info['population'])
	print('\tFact: ' + city_info['fact'])
