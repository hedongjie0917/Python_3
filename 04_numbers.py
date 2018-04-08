#使用range()函数生成一系列数字，range()函数让python从指定的第一个值开始数，并在到达指定的第二个值后停止，因此输出不包含指定的第二个值。
for value in range(1,5):
	print(value)

for value in range(1,6):
	print(value)

#使用list()函数将数字转换为列表
numbers=list(range(1,6))
print(numbers)

#使用range()指定步长
#从2开始数，不断的加2，直到达到或超过11时终止。打印出1到10内的偶数
even_numbers=list(range(2,11,2))
print(even_numbers)

#从1开始数，不断的加2，直到达到或超过11时终止。打印出1到10内的奇数
odd_numbers=list(range(1,11,2))
print(odd_numbers)



