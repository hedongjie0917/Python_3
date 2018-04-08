#定义一个空字典
responses = {}

#设置一个标志，用于指出调查是否继续
polling_active = True
#只要polling_active为True，Python就继续运行while循环中的代码
while polling_active:
#提示用户输入自己的名字和喜欢的山
	name = input("\nWhat is your name?")
	response = input("While mountain would you like to climb someday?")
#将上述信息存储在字典
	responses[name] = response

	repeat = input("Would you like to let another person respond? (yes/no)")
	if repeat == 'no':
		polling_active = False
print("\n----Poll Result----")
for name, response in responses.items():
	print(name + "would like to climb " + response + ".")
