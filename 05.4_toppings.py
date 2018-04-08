requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print('Sorry, we are out of green peppers right now.')
	else:
		print('Adding ' + requested_topping.title()+'.')
print('Finished making your pizza!')

#第11行，在if语句中将列表名用在条件表达式中时，python将在列表至少包含一个元素时返回true，在列表为空时返回false。
print('\nP2')
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print('Adding '+ requested_topping + '.')
	print('\nFinished making your pizza.')
else:
	print('Are you sure you want a plain pizza?')

#
print('\nP3')
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print('Adding ' + requested_topping.title() + '.')
	else:
		print("Sorry, we don't have " + requested_topping.title() + '.')
print('\nFinished making your pizza.')
