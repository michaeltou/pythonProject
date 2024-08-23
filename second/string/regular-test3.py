import re


m = re.compile(r'^(\d{3})-(\d{3,8})$')

a = m.match('010-1234567')

print(a.groups())
