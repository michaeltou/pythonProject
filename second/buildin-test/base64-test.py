import base64


# base64_str = base64.b64encode(b"hello world")
# print(base64_str)

base64_str1 = 'aGVsbG8gd29ybGQ='

base64_str = base64.b64decode(base64_str1)
print(str(base64_str))