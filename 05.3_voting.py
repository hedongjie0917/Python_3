age=19
if age>=18:
	print('You are old enough to vote!')
	print('Have you registered to vote yet?')

#if-else语句，非常适合让python执行2种操作的情况，要么执行A，要么执行B。
age=17
if age>=18:
	print('\nYou are old enough to vote!')
	print('Have you registered to vote yet?')
else:
	print('\nsorry, you are too young to vote.')
	print('Please registered to vote as soon as you turn 18!')

#if-elif-else语句，适合检查下超过2个的情形，python只会执行if-elif-else语句中的一个代码块，依次检查每个条件，知道遇到通过的条件则跳出。
age=12
if age<4:
	print('Your adminssion cost is $0.')
elif age<18:
	print('Your adminssion cost is $5.')
else:
	print('Your adminssion cost is $10.')

#使用下面的语句可以简化代码块，可以得到相同的结果。
age=12
if age<4:
	price=0
elif age<18:
	price=5
else:
	price=10
print('Your adminssion cost is $'+str(price)+'.')

#使用多个elif语句
age=12
if age<4:
	price=0
elif age<18:
	price=5
elif age<65:
	price=10
else:
	price=5
print('Your adminssion cost is $'+str(price)+'.')

#else语句并不是必须的，有些情况下是可以省略的
age=12
if age<4:
	price=0
elif age<18:
	price=5
elif age<65:
	price=10
elif age>=65:
	price=5
print('Your adminssion cost is $' + str(price)+'.')
