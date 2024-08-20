code = """
def add(x, y):
    return x + y

print(add(2, 3))
"""

compiled_code = compile(code, "filename", "exec")

exec(compiled_code)

expr = "2+ 3*4"
compiled_expr = compile(expr, "filename", "eval")

result = eval(compiled_expr)

print(result)
