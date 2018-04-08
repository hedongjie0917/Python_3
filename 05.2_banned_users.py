#使用not in来检查特定的值不在列表中。布尔运算的结果要么为True，要么为False
banned_users=['andrew','elijah','huck']
user='jinqi'
if user not in banned_users:
	print(user.title()+', you can post a response if you wish.')

car='subaru'
print("Is car=='subaru'? I predict True.")
print(car=='subaru')

print("\nIs car=='audi'? I predict False.")
print(car=='audi')

colour_01='red'
print(colour_01=='red')
colour_02='blue'
print(colour_02!='black')
car_01='Bmw'
print(car_01=='bmw')
print(car_01.lower()=='bmw')

a=3
b=4
print(a>b)
