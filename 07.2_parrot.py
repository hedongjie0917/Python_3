#下面的代码输入quit时会推出程序，但是也会执行一次程序，输入quit
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
	message = input(prompt)
	print(message)


#下面的代码输入quit不会打印出quit，而是直接退出程序
prompt = "\nTell me sth and I will repeat it back to you."
prompt +="\nEnter 'quit' to end the program."
message = ""
while message !='quit':
	message = input(prompt)

	if message != 'quit':
		print(message)

#本实例结果和上面相同，但是使用了“标志”，使用True来判断程序是否为激活状态，如果为True则程序执行，如果为Fales则终止。
prompt = "\nTell me sth and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)

