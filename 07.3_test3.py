places = {}

polling_active = True
while polling_active:
	name = input("\nWhat's your name?")
	place = input("If your could visit ont place in the world, where would you go?")
	places[name] = place

	repeat = input("\nWould u like other person to respond? (yes/no)")
	if repeat == 'no':
		polling_active = False
print("\n----Poll Result----")
for name, place in places.items():
	print(name.title() + " want to visit " + place.title())