users = {
	'hdongjie':{
		'first':'he',
		'last':'dongjie',
		'location':'shanghai',
		},

	'yge':{
		'first':'yang',
		'last':'ge',
		'location':'lingbao',
		}
	}

for username, user_info in users.items():
	print('\nUsername:' + username)
	full_name = user_info['first'] + ' ' + user_info['last']
	location = user_info['location']

	print('\tFull name:' + full_name.title())
	print('\tLocation:' + location.title())