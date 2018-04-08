users=['zhao','qian','sun','li','admin']
for user in users:
	if user == 'admin':
		print('Hello ' + user.title() + ',' + ' would you like to see a status report?')
	else:
		print('Hello ' + user.title() + ',' + ' thank your for logging it again.')


print('\nP2')
users=[]
if users:
	for user in users:
		if user == 'admin':
			print('Hello ' + user.title() + ',' + ' would you like to see a status report?')
		else:
			print('Hello ' + user.title() + ',' + ' thank your for logging it again.')
else:
	print('We need to find some users!')


print('\nP3')
current_users=['tom','jim','wang','li','jin']
new_users=['Tom','jim','zhao','qian','jIn']
for user in new_users:
	if user.lower() in current_users:
		print(user + ' was used now, please try some other usernames.')
	else:
		print(user + ' could be used by you.')