
height = input('How tall are you, in inches? ')
height = int(height)
if height >= 36:
	print('\nYou are tall enough to ride!')
else:
	print("\nYou'll be able to ride when you're a little older.")

# %为求模运算符，它将2个数相除并返回余数，可以根据 % 来判断一个数是偶数还是奇数
number = input('Enter a number, and I will tell you if it is even or odd: ')
number = int(number)

if number % 2 ==0:
	print('\nThe number ' + str(number) + ' is even.')
else:
	print('\nThe number ' + str(number) + ' is odd.')
