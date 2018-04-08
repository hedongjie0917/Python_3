supper_together=['zhang','gao','zhou','liu']
print(supper_together)
unable_come=supper_together[-1]
print(unable_come.title()+" can not come to this supper.")
supper_together[-1]='wang'
print(supper_together)

message_01=' could u come to my dinner party?'
print('Hello, Mr.'+ supper_together[0].title()+message_01)
print('Hello, Mr.'+ supper_together[1].title()+message_01)
print('Hello, Mr.'+ supper_together[2].title()+message_01)
print('Hello, Mr.'+ supper_together[3].title()+message_01)

supper_together.insert(0,'zhao')
supper_together.insert(3,'qian')
supper_together.append('sun')
print(supper_together)

print('Hello, Mr.'+ supper_together[0].title()+message_01)
print('Hello, Mr.'+ supper_together[1].title()+message_01)
print('Hello, Mr.'+ supper_together[2].title()+message_01)
print('Hello, Mr.'+ supper_together[3].title()+message_01)
print('Hello, Mr.'+ supper_together[-3].title()+message_01)
print('Hello, Mr.'+ supper_together[-2].title()+message_01)
print('Hello, Mr.'+ supper_together[-1].title()+message_01)
print('I only could invite two friends come to my dinner party.')

message_02="I am very sorry, because the table haven't come, so we can only have dinner next time."
message_03="You could also come to my dinner party."
unable_come_01=supper_together.pop(0)
print('Dear '+unable_come_01.title()+','+message_02)
unable_come_02=supper_together.pop(0)
print('Dear '+unable_come_02.title()+","+message_02)
unable_come_03=supper_together.pop(1)
print('Dear '+unable_come_03.title()+','+message_02)
unable_come_04=supper_together.pop(2)
print('Dear '+unable_come_04.title()+','+message_02)
unable_come_05=supper_together.pop(2)
print('Dear '+unable_come_05.title()+','+message_02)
print(supper_together)
print(len(supper_together))
print('Dear '+supper_together[0].title()+','+message_03)
print('Dear '+supper_together[1].title()+','+message_03)

del supper_together[0]
del supper_together[0]
print(supper_together)
print(len(supper_together))