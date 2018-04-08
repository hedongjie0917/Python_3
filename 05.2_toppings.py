#使用“!=”表示不等于，这种情况如果不等于则返回True，如果等于则返回False
requested_topping='mushrooms'
if requested_topping!='fish':
	print('Hold the fish, please!')

age=18
print(age==18)

answer=42
if answer!=42:
	print('That is not the correct answer. Please try again!')
else:
	print('congratulations! U r right!')

age=19
print(age<21)
print(age<=21)
print(age>21)
print(age>=21)

#需要检查适合的所有条件，有可能有多个True，每个条件为True时都采取相应措施。
requested_toppings=['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
	print('Adding mushroom.')
if 'pepperoni' in requested_toppings:
	print('Adding peppetoni')
if 'extra cheese' in requested_toppings:
	print('Adding extra cheese.')
print('\nFinished making your pizza!')


