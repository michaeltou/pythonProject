import hashlib

md5 = hashlib.md5()
md5.update('hello world'.encode('utf-8'))
md5.update('many lines1'.encode('utf-8'))

print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('hello world'.encode('utf-8'))
sha1.update('many lines2'.encode('utf-8'))

print(sha1.hexdigest())