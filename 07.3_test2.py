sandwich_orders = ['pastrami','fish','pastrami','meet','pastrami','fruit']
finished_sandwichs = []

print("\nPastrami was sold out.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("I made your " + current_sandwich.title() + " sandwich.")
	finished_sandwichs.append(current_sandwich)
	
print("\nThe following sandwiches had be made:")
for finished_sandwich in finished_sandwichs:
	print(finished_sandwich.title())


