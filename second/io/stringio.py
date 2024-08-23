from io import StringIO

# create a string buffer
buffer = StringIO()


# write some data to the buffer
buffer.write("Hello, ")
buffer.write("World!")
print(buffer.getvalue())
buffer.close()