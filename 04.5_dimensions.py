#列表是可以修改的，使用[]来表示。不可修改的成为元组，使用()来表示。
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
	print(dimension)

#如果需要对列表进行修改，可以使用以下方法来修改
dimensions=(100,300)
print('original dimensions:')
for dimension in dimensions:
	print(dimension)

dimensions=(500,300)
print('\nmodified dimensions:')
for dimension in dimensions:
	print(dimension)