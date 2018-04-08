#嵌套，将字典存储在列表中、将列表存储到字典中、将字典存储到字典中均称为嵌套。
#先创建3个alien的字典，然后将这些字典都放在aliens的列表中，然后遍历整个列表。
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)

print('\nP2')
#创建一个用于存储外星人的空列表
aliens = []
#创建30个绿色外星人,并使用append语句添加到列表末尾
for alien_number in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
#显示前5个外星人
for alien in aliens[:5]:
	print(alien)
print('...')
#显示创建多少个外星人
print('Totle number of aliens: ' + str(len(aliens)))

print('\nP3')
aliens = []
for alien_number in range(0,30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
#将前3个中颜色为green的修改为下面的信息。
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yelow'
		alien['speed'] = 'medium'
		alien['points'] = 10
for alien in aliens[0:5]:
	print(alien)
print('...')

print('\nP4')
aliens = []
for alien_number in range(0,30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
for alien in aliens[0:5]:
	print(alien)
print('....')
print('Totle number of alien ' + str(len(aliens)))
