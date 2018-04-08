#返回值，在函数中使用return语句将值返回到调用函数的代码行
print('\nP1 first_name + last_name')
def get_formatted_name(first_name,last_name):
	'''返回整洁的姓名'''
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

print('\nP2 first_name + middle_name + last_name')
def get_formatted_name(first_name,middle_name,last_name):
	'''返回整洁的姓名'''
	full_name = first_name + ' ' + middle_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('john','lee','hooker')
print(musician)

# 并不是所有人都有middle name，故给middle name指定一个默认值--空字符串
# 结果是不管有无middle name，该程序都可以正常运行，middle_name必须放在最后一位。
print('\nP3')
def get_formatted_name(first_name,last_name,middle_name = ''):
	'''返回整洁的姓名'''
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)
