
# 教程:https://zhuanlan.zhihu.com/p/521012399


globals = {}
globals['a'] = 3

locals = {}


exec("b= 4",globals,locals)



print(globals.keys())

print(locals.keys())




