print("P1")
def make_album(songer_name,song_name):
	song_info = {'songer':songer_name.title(),'song':song_name.title()}
	return song_info
bingyu = make_album('liu dehua','ice-rain')
print(bingyu)

woniu = make_album('zhou jielun','snail')
print(woniu)

zuimeideqidai = make_album('zhou bichang','best-expectation')
print(zuimeideqidai)

print('\nP2')
def make_album(songer_name,song_name,number=''):
	song_info = {'songer':songer_name.title(),'song':songer_name.title()}
	if number:
		song_info['number'] = number
	return song_info
bingyu = make_album('liu dehua','ice-rain',3)
print(bingyu)

woniu = make_album('zhou jielun','snail')
print(woniu)

