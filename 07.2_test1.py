age = input("\nHow old are you?")
age = int(age)

if age < 3:
	price = 0
elif age < 12:
	price = 10
else:
	price = 15
print("Your ticket price is " + str(price) + '.')
