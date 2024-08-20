
class Chain:
    def __init__(self, path):
        self.__path = path

    def __getattr__(self, attr):
        return Chain(self.__path + '/' + attr)

    def __str__(self):
        return self.__path



# Example usage:
c = Chain('/status')
myUrl = c.user.timeline.list.getdata
print(myUrl)

