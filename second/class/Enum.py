
from enum import Enum


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

day = Weekday.SATURDAY


print(day==Weekday.FRIDAY)

for name, member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)
