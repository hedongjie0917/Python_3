def make_shirt(size,sample):
	'''print size and sample in T-shirt'''
	print("\nMy T-shirt's size is " + size +'.')
	print("The sample in my T-shirt is a " + sample + '.')
make_shirt('12','dog')


def make_shirt(size,sample='I love Python'):
	'''print size and sample in shirt'''
	print("\nMy T-shirt's size is " + size +'.')
	print("The sample in my T-shirt is a " + sample + '.')
make_shirt('big')
make_shirt('middle')
make_shirt(size='any',sample='Python is the best')

def describe_city(city_name,country='China'):
	'''print city and it's country'''
	print('\n' + city_name + ' is in ' + country + '.')
describe_city('SH')
describe_city('BJ')
describe_city(city_name='NewYork',country='USA')





