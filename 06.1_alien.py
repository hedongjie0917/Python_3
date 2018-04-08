#python中字典是一系列键-值对，每个键都有一个与之相关的值关联。字典用放在{}中的一系列键-值表示。
#键与值之间用冒号分开，键-值对之间用逗号分开。
alien_0= {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print('You just earned '+str(new_points)+' points!')

#字典是一种动态结构，可以随时在其中添加键-值对。要添加键-值对可以依次指定字典名、用[]括起来的键和相关的值。
#python不关心各个键-值对的顺序，只关心键与值之间的对应关系。
alien_0 = {'color':'green','point':5}
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#先定义一个空字典，再往字典中添加键-值对。
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#修改字典中的值，可依次指定字典名、用方括号括起来的键、与该键相关联的新值。
alien_0 = {'color':'green'}
print('The alien is ' + alien_0['color'] + '.')
alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'] + '.')


alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print('Original x-position:' + str(alien_0['x_position']))
alien_0['speed']='fast'
#向右移动外星人
#据外星人当前速度决定其移动多远
if alien_0['speed'] =='slow':
	x_increment = 1
elif alien_0['speed'] =='medium':
	x_increment = 2
else:
	x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x-position: ' + str(alien_0['x_position']))


#对于字典中不需要的键-值对可以使用del来彻底删除，使用del语句时，必须指定字典名和要删除的键。
alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)


