#使用continue语句可以返回到循环开头，并根据条件测试结果决定是否继续执行循环。下面实例为打印1~10中的奇数。
#下面实例中，如果为偶数则忽略下面的print语句，从头开始循环执行。
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 ==0:
		continue

	print(current_number)
