#使用break可以控制程序流程，break可以立刻退出while循环，所有python循环语句都可以使用break语句。
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + '!')

