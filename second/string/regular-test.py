import re

if re.match(r'^\d{3}-\d{3,8}$', '010-12345'):
    print('valid')
else:
    print('invalid')



if re.match(r'^\d{3}-\d{3,8}$', '010 12345'):
    print('valid')
else:
    print('invalid')