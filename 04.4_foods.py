#使用[:]来复制列表
my_foods=['pizza','falafel','carrot','cake','tomato']
friend_foods=my_foods[:]
print('p1')
print(my_foods)
print('\np2')
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print('\np3')
print('my favorite foods are:')
print(my_foods)
print('\np4')
print('my firend foods are:')
print(friend_foods)
print('\np5')
print('The first three items in my_foods are:')
print(my_foods[:3])
print('\np6')
print('Three items from the middle of the list are:')
print(my_foods[1:4])
print('\np7')
print('The last three items in the list are:')
print(my_foods[-3:])

