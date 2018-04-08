for number in range(1,21):
	print(number)

numbers=list(range(1,1001))
print(numbers)

numbers=list(range(1,1001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers=list(range(1,21,2))
for odd_number in odd_numbers:
	print(odd_number)

plus3_numbers=list(range(3,31,3))
for plus3_number in plus3_numbers:
	print(plus3_number)

cube_numbers=list(range(1,11))
for cube_number in cube_numbers:
	print(cube_number**3)

cube_numbers=[cube_number**3 for cube_number in range(1,11)]
print(cube_numbers)