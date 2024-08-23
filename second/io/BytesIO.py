
from io import BytesIO


# create a BytesIO object
f = BytesIO()

# write some bytes to the object
f.write('Hello, world!你好，世界！'.encode('utf-8'))
f.flush()

# read the bytes back
data = f.getvalue()

# print the data
print(data)