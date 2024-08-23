f = None

try:
    f = open("test.txt", "r")
    print(f.read())

except FileNotFoundError:
    print("File not found")
finally:
    if f:
        print('Closing file')
        f.close()