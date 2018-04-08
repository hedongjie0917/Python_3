prompt = "\nPlease input the material you want to add to Pizza."
prompt += "\nEnter 'quit' when you are finished."

while True:
	material = input(prompt)

	if material == 'quit':
		break
	else:
		print("\nThe material you want to add is " + material.title() + '.')


