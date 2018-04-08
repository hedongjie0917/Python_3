#每条if语句的核心都是一个值True或False的表达式，这种表达式称为条件测试。
#python根据条件测试的值为True或False来决定是否执行if语句中的代码，为True则执行，为False则不执行。
#下面实例中，如果检测到为bmw则大写，否则首字母大写。
cars=['audi','bmw','subaru','toyota']
for car in cars:
	if car =='bmw':
		print(car.upper())
	else:
		print(car.title())

car='bmw'	#使用“=”来进行赋值
print(car=='bmw')	#使用“==”来进行检测

car='audi'
print(car=='bmw')

#python中检查是否相等时区分大小写的
car='Audi'
print(car=='audi')

#使用lower()函数将car转化为小写，再进行比较，并且不会改变原有的值。
car='Audi'
print(car.lower()=='audi')
print(car)





