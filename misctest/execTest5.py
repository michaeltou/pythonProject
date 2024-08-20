g_var = 42

code = """
local_var = 10
"""

globals = {"global_var": g_var}
exec(code, globals)

print(globals.keys())


