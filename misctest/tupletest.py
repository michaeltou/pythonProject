# tuple = ( 'maxsu', 786 , 2.23, 'yiibai', 70.2  )
# tinytuple = (999.0, 'maxsu')
#
# # tuple[1] = 'new item value' 不能这样赋值
#
# print ('tuple = ', tuple)           # Prints complete tuple
# print ('tuple[0] = ', tuple[0])        # Prints first element of the tuple
# print ('tuple[1:3] = ', tuple[1:3])      # Prints elements starting from 2nd till 3rd
# print ('tuple[-3:-1] = ', tuple[-3:-1])       # 输出结果是什么？
# print ('tuple[2:] = ', tuple[2:])       # Prints elements starting from 3rd element
# print ('tinytuple * 2 = ',tinytuple * 2)   # Prints tuple two times

tuple = ('maxsu', 786,2.23,'yiibai',70.2)
tinytuple = (999.0,'maxsu')

print('tuple = ',tuple)
print('tinytuple = ',tinytuple)
print('tuple[1:3] = ',tuple[1:3])
print('tuple[-3:-1] = ',tuple[-3:-1])
print('tuple[2:] = ',tuple[2:])
print('tinytuple * 2',tinytuple * 2)
print('tinytuple + tuple = ',tinytuple + tuple)