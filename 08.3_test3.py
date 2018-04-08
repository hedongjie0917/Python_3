def make_album(songer_name,song_name,number=' '):
	song_info = {'songer':songer_name.title(),'song':songer_name.title()}
	if number:
		song_info['number'] = number
	return song_info

while True:
	print('Please input a song info:')
	print("enter 'q' at any time to quit")

	songer_name = input('songer name: ')
	if songer_name == 'q':
		break

	song_name = input('song name: ')
	if song_name == 'q':
		break
	bingyu = make_album(song_name,song_name,3)
	print(bingyu)