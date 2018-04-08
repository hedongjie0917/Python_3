#if-elif-else语句只适合于只有一个条件满足的情况，通过测试后python就跳过余下的测试。如果需要检查所有关心的条件，只能使用简单的if语句。
requested_toppings=['mushroom','extra cheese']
if 'mushroom' in requested_toppings:
	print('Adding mushroom.')
if 'pepper' in requested_toppings:
	print('Adding pepper.')
if 'extra cheese' in requested_toppings:
	print('Adding extra cheese.')
print('\nFinished making your pazza!')

