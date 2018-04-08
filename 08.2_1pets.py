#传递实参:位置实参、关键字实参、列表与字典

#下面实例为位置实参，实参和形参有一一对应关系，顺序非常重要。2组实参，1组形参。
print("\nP1")
def describe_pet(animal_type,pet_name):
	'''显示宠物信息'''
	print("I have a " + animal_type + '.')
	print("My " + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet('hamster','harry')
describe_pet('dog','willie')

#下面实例为关键字实参，关键字实参的顺序无关紧要
print("\nP2")
def describe_pet(animal_type,pet_name):
	'''显示宠物信息'''
	print('I have a ' + animal_type + '.')
	print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet(animal_type='hamster',pet_name='harry')

#默认值，编写函数时可以给每个形参设定一个默认值，如有实参则用实参，否则用默认值。
#使用默认值时，在形参列表中必须先列出没有默认值的形参，然后再列出有默认值的形参。
print("\nP3")
def describe_pet(pet_name,animal_type='dog'):
	'''显示宠物信息'''
	print("I have a " + animal_type + '.')
	print("My " + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet(pet_name='willie')
describe_pet(pet_name='Lily')
describe_pet(pet_name='Lucy',animal_type='cat')

# 等效的函数调用，可以使用位置实参、关键字实参和默认值等多种调用方式
print("\nP4")
def describe_pet(pet_name,animal_type='dog'):
	'''显示宠物信息'''
	print('I have a ' + animal_type + '.')
	print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
# 一只名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name = 'willie')

#一只名为Harry的仓鼠
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')

