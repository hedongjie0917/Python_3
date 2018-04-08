#for循环
magicians=['alice','david','tom']
for magician in magicians:
	print(magician.title())

#for循环后面缩进的代码会被执行多次，没有缩进的代码只会执行一次
magicians=['alice','david','tom']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + '.\n')
print('Thank you, everyone. That was a great magic show!')