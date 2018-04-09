#传统方法
# 创建一个列表，其中包含需要打印的设计；一个空列表
unprinted_designs = ['iphone','robot','panda']
completed_models = []

#模拟打印每个设计，直到没有未打印的设计为止
#打印设计后，将其移到列表completed_models中
while unprinted_designs:
	current_design = unprinted_designs.pop()

	#模拟根据设计制作3D打印模型的过程
	print('Printing model: ' + current_design)
	completed_models.append(current_design)

#显示打印好的所有模型
print('\nThe following models have been printed:')
for completed_model in completed_models:
	print(completed_model)

#使用2个函数的方法,第一个函数负责处理打印设计工作，第二个负责打印出已经完成的设计
print('\nP2')
def print_models(unprinted_designs,completed_models):
	'''
	模拟打印每个设计，直到没有未打印的设计为止
	打印设计后，将其移到列表completed_models中
	'''
	while unprinted_designs:
		current_design = unprinted_designs.pop()

		#模拟根据设计制作3D打印模型的过程
		print('Printing model: ' + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	'''显示打印好的模型'''
	print('\nThe following models have been printed:')
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone','robot','panda']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
# 上述方法会清空unprinted_designs列表，
#使用print_models(unprinted_designs[:],completed_models)将不会清空





