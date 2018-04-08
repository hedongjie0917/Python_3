#if-elif-else语句适合让python执行超过2个以上的情形时使用，依次检测每个测试条件，遇到通过的条件即跳出测试。
age=12
if age<4:
	print('Your admission cost is $0.')
elif age<18:
	print('Your admission cost is $5.')
else:
	print('Your admission cost is $10.')

#下面的代码可以简化代码，得到相同的结果
age=12
if age<4:
	price=0
elif age<18:
	price=5
else:
	price=10

#包含多个elif语句
age=55
if age<4:
	price=0
elif age<18:
	price=5
elif age<65:
	price=10
else:
	price=5
print('Your admission cost is $'+str(price)+'.')

print('Your admission cost is $'+str(price)+'.')

#if-elif语句中else代码不是必须的，使用elif语句可能更清晰
age=18
if age<4:
	price=0
elif age<18:
	price=5
elif age<65:
	price=10
elif age>=65:
	price=5
print('Your admission cost is $'+str(price)+'.')