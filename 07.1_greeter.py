name = input('Please enter your name: ')
print('Hello, ' + name + '!')

#该实例讲解创建多行字符串的方法，第一行的消息存储在prompt中，在第2行中，使用+=在prompt字符串末尾再附件一个字符串。
prompt = 'If you tell us who you are, we can personalize the messages you see.'
prompt += '\nWhat is your first name? '

name = input(prompt)
print('\nHello, ' + name + '!')

