

def person(name, age, **kwargs):
    print("Name:", name)
    print("Age:", age)
    print("Other:", kwargs)
    print("type:",type(kwargs))


dict1 = {"city": "Beijing", "country": "China"}

person("John", 30, **dict1)

