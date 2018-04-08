#使用and和or来实现检查多个条件
#使用and时，两个条件都满足时才返回True，其余都返回False。使用or时只要有一个条件满足即返回True。
age_0=22
age_1=18
print(age_0>=21 and age_1>=21)
age_1=23
print((age_0>=21) and (age_1>=21))

print('\np2')
age_0=22
age_1=18
print(age_0>=21 or age_1>=21)
print(age_0>=25 or age_1>=25)

#使用in来检查特定的值是否在列表中
print('\np3')
requested_toppings=['mushroom','onions','pineapple']
print('mushroom' in requested_toppings)
print('orange'in requested_toppings)
