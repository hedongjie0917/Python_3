#使用:来对列表进行切片操作，也是从0开始计数，
#需要切取前3个元素，生成一个列表
players=['tom','jim','lilei','hanmeimei']
print('p1')
print(players[0:3])

#需要切取第2到第4个元素，生成一个列表
print('\np2')
print(players[1:4])

#从开头切取到第3位
print('\np3')
print(players[:3])

#从第二位切取到结尾
print('\np4')
print(players[1:])

#从倒数第三个元素开始切割到末尾
print('\np5')
print(players[-3:])

#切取所有元素
print('\np6')
print(players[:])

#遍历切片
print('\np7')
players=['tom','jim','lilei','hanmeimei']
print('Here are the first three players on my team:')
for player in players[:3]:
	print(player.title())

