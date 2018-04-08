#实例中返回值为字典
def build_person(first_name,last_name):
	'''返回一个字典，其中包含有关一个人的信息'''
	person = {'first':first_name,'last':last_name}
	return person
musican = build_person('jimi','hendrix')
print(musican)

# 为上一个函数的扩展，新增一个可选形参age
def build_person(first_name,last_name,age = ''):
	'''返回一个字典，其中包含有关一个人的信息'''
	person = {'first':first_name,'last':last_name}
	if age:
		person['age'] = age
	return person
musican = build_person('jimi','hendrix',age = 28)
print(musican)
