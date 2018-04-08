#创建一个未验证用户列表
unconfirmed_users = ['alice','brian','candace']
#创建一个已验证用户列表
confirmed_users = []
#while循环不断的运行，直到unconfirmed_users变为空的
while unconfirmed_users:
#pop()函数以每次一个的方式从列表unconfirmed_users末尾删除未验证用户
	current_user = unconfirmed_users.pop()

	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
