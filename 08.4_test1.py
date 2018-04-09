magicians_name = ['Tom','Robert','li']
def show_magicians(magicians):
	'''print magicians's name'''
	for magician in magicians:
		msg = 'Welcome magician ' + magician.title() + '!'
		print(msg)

#将列表作为形参传递给show_magicians()
show_magicians(magicians_name)

print('\nP2')
def make_great(magicians):
	for magician in magicians:
		msg = 'The Great ' + magician + ' !'
		print(msg)
make_great(magicians_name)
