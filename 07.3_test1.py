sandwich_orders = ['fish','meet','fruit']
finished_sandwichs = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("I made your " + current_sandwich.title() + " sandwich.")
	finished_sandwichs.append(current_sandwich)
	
print("\nThe following sandwiches had be made:")
for finished_sandwich in finished_sandwichs:
	print(finished_sandwich.title())


