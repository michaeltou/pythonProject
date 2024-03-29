
from enum import Enum

Month = Enum('Month',('January', 'February', 'March', 'April', 'May', 'June'))

for name,member in Month.__members__.items():
    print(name,member,member.value)