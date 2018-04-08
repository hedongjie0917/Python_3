#存储所点披萨的信息,当一个键需要关联到多个值时，可以使用在字典中嵌套一个列表的方式。
pizza = {
	'crust':'thick',
	'toppings':['mushroom','extra cheese'],
	}
#概述所点的披萨
print('You ordered a ' + pizza['crust'] + '-crust pizza' + ' with the following toppings:')
for topping in pizza['toppings']:
	print( '\t' + topping)

favorite_languages = {
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','c++'],
	}
for name, languages in favorite_languages.items():
	if len(languages) > 1:
		print('\n' + name.title() + "'s favorite language are :")
		for language in languages:
			print('\t' + language.title())
	elif len(languages) == 1:
		print('\n' + name.title() + "'s favorite language is :" )
		for language in languages:
			print('\t' +language.title())