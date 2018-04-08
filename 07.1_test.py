car = input('Which car do you want to rent? ')
print('Let me see if I can find a ' + car + '.')



perple_number = input('How many people are eating? ')
perple_number = int(perple_number)
if perple_number > 8:
	print('\nSorry, we do not have available table for you.')
elif perple_number >=1:
	print('\nWe have available table for you.')
else:
	print('\nAre you kitting me?')


number = input('Enter a number and I will tell you if it could divided by 10. ')
number = int(number)
if number % 10 ==0:
	print('\nhe number ' + str(number) + ' could divided by 10.')
else:
	print('\nThe number ' + str(number) + ' could not divided by 10.')
