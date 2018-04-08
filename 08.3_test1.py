def city_country(city_name,country_name):
	'''city and it's country'''
	formatted_city_country = '"' + city_name + ', ' + country_name + '"'
	return formatted_city_country.title()

china_capital = city_country('beijing','china')
print('\n' + china_capital)

japan_capital = city_country('tokyo','japan')
print('\n' + japan_capital)

UK_capital = city_country('UK','london')
print('\n' + UK_capital)

