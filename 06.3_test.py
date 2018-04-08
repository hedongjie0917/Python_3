rivers_0 = {
	'changjiang':'China',
	'nile':'egypt',
	'ganges':'india',
	}
for river , country in rivers_0.items():
	print('The ' + river.title() + ' through ' + country.title() + '.' )

for river in rivers_0.keys():
	print(river.title())

for country in rivers_0.values():
	print(country.title())

print('\nP2')
favorite_language = {
	'jen':'python',
	'tom':'c',
	'li':'ruby',
	'phil':'python',
	}
people_0 = ['tom','li','phil','zhao','qian']
for person in people_0:
	if person in favorite_language.keys():
		print(person.title() + ' ,thanks for your attention.')
	else:
		print(person.title()+' Could u attend our investigation ?')
