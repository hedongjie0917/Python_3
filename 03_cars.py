#使用sort()对列表进行永久性排序，按照字母的顺序来排序。sort[sɔ:t]分类、排序
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#按照字母顺序相反的方向排序，reverse[rɪˈvɜ:s]反转
cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

#使用sorted()对列表进行临时排序
cars=['bmw','audi','toyota','subaru']
print('Here is the original list:')
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

print('\nHere is the sorted list again:')
print(sorted(cars, reverse=True))

#使用reverse()来反转列表中元素的排序,该改变是永久的
cars=['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

#使用len()快速获悉列表的长度
cars=['bmw','audi','toyota','subaru']
print(len(cars))
