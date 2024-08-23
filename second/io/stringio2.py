from io import StringIO

# create a string buffer
buffer = StringIO('Hello!\nHi!\nGoodbye!')


while True:
    line = buffer.readline()
    if line == '':
        break
    print(line)

buffer.close()