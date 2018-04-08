#从1到10这十个整数的平方
squares=[]	#创建一个空列表
for value in range(1,11):	#使用range()函数让python遍历1~10的值
	square=value**2		#计算value的平方，并存储到square中
	squares.append(square)	#将计算得到的square附加到squares的末尾
print(squares)

squares=[]
for value in range(1,11):
	squares.append(value**2)
print(squares)

#计算一个数字列表里的最大值、最小值和求和
digits=[1,2,3,4,5,7,11,20]
print(min(digits))
print(max(digits))
print(sum(digits))

#使用列表解析来简化代码，最左边的value**2为一个需要存储到列表中的表达式，然后是一个for循环，末尾没有冒号。
squares=[value**2 for value in range(1,11)]
print(squares)

