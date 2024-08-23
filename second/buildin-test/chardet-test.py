
import chardet

res = chardet.detect(b'Hello, world!')
print(res)

data = 'abc你好世界，一岁一哭了'.encode('gbk')
res = chardet.detect(data)
print(res)