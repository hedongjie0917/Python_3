user_0 = {
	'username':'eferimi',
	'first':'enrico',
	'last':'ferimi',
	}
#先声明2个变量，用于存储键-值对的键和值，这2个变量可以使用任何名称。
for key,value in user_0.items():
	print('\nkey:' + key)
	print('value' + value)

#下面示例为遍历字典中所有的键-值对。
print('\nP2')
favorite_languages = {
	'jen':'python',
	'sarah':'C',
	'edward':'ruby',
	'phil':'python',
	}
for name , language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + '.')

#下面示例为遍历字典中所有的键，遍历字典时默认就是遍历所有的键，故for语句可以替换为for name in favorite_languages：
print('\nP3')
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
for name in favorite_languages.keys():
	print(name.title())

print('\nP4')
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
friends = ['phil','sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print('Hi ' + name.title() + ', I see your favorite language is ' + favorite_languages[name].title() + '!')
	
print('\nP5')
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
if 'erin' not in favorite_languages.keys():
	print('Erin, please take our poll!')

#按顺序遍历字典中所有的键,使用sorted()来获取按特定顺序排列的键列表的副本。
print('\nP6')
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
for name in sorted(favorite_languages.keys()):
	print(name.title() + ',thank you for taking the poll.')

#遍历字典中所有的值,使用values()即可以返回所有的值，而不会包含键。
print('\nP7')
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
print('The following languages have been mentioned:')
for language in favorite_languages.values():
	print(language.title())

#使用集合（set）可以去除掉输出结果中的重复项。集合类似于列表，但是每个元素都是独一无二的。
print('\nP8')
favorite_languages={
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}
print('The following language have been mentioned:')
for language in set(favorite_languages.values()):
	print(language.title())