#use def to define a function, 向python指出函数名，在括号内指出函数为完成其任务需要的操作。
def greet_user():
#此处为字符串，描述函数应该是做什么的
	'''显示简单的问候语'''
#下面为函数内的代码行
	print('Hello!')
greet_user()

#下面的例子中，greet_user(username)中的username为形参，greet_user('dongjie')中的dongjie为实参。
#将实参传递给形参。
def greet_user(username):
	'''显示简单问候语'''
	print('Hello, ' + username.title() + '!')
greet_user('dongjie')
