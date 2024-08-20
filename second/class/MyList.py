
class MyList:
    def __getitem__(self, index):
        return index*2


my_list = MyList()

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])