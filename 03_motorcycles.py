motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

#修改第0位的元素，改为lifan
motorcycles[0]='lifan'
print(motorcycles)

#使用append()在列表末尾添加新元素
motorcycles=['hongda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

#创建一个新的空列表，再使用append()语句来添加元素
motorcycles=[]
motorcycles.append('hongda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#在列表中添加新元素,使用insert来往指定的位置添加新元素
motorcycles=['hongda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

#从列表中删除元素，使用del()删除。使用del删除后该元素即消失了，再也无法访问到该元素了
motorcycles=['hongda','yamaha','suzuki']
print(motorcycles)
del motorcycles[-1]
print(motorcycles)

#从列表中删除元素，使用pop()删除,使用pop删除文件后，还可以继续使用该元素，pop意思为弹出.默认情况下使用pop()会删除列表末尾的元素.
#使用pop(X)可以指定删除列表中元素的位置
motorcycles=['hongda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles=motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles=['hongda','yamaha','suzuki']
last_owned=motorcycles.pop()
print('The last motorcycle I owned was a ' + last_owned.title()+'.')

motorcycles=['hongda','yamaha','suzuki']
second_owned=motorcycles.pop(1)
print('The second motorcycle I owned was a ' + second_owned.title() + '.' )

#使用remove()根据元素的值来删除元素。remove()只能删除第一个指定的值，如果列表中的该元素出现多次，需要用循环判断来删除所有的值。
motorcycles=['hongda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
#删除后还可以继续使用该元素的值
motorcycles=['hongda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA '+ too_expensive.title() + ' is too expensive for me.')

