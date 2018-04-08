#用[]表示列表，用逗号来分隔其中的元素
#索引从0开始，不是从1开始
bicycles = ['trek','cannondale','redline','specialized']
message = 'My first bicycle was a ' + bicycles[0].title() + '.'
print(bicycles)
#从列表中提取第一位元素，并大写
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
#从列表中提取最后一位元素(倒数第一位)
print(bicycles[-1])
#从列表中提取倒数第4位元素
print(bicycles[-4])
print(message)