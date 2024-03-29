dict = {}

dict['one'] = 'this is one string'

dict['two'] = 'this is 2'

dict['three'] = 3

print('dict = ',dict)

print('dict.keys() = ',dict.keys())
for key in dict.keys():
    print(key)
for value in dict.values():
    print(value)


addr = {'address':'123 Main St', 'city':'hengyang'}

tinydict = {'name':'douming', 'age':39, 'address': addr}

print('result = ',tinydict['address'])
print('result = ',tinydict['address']['address'],tinydict['address']['city'])
