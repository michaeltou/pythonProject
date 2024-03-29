import io


with open("asttest.py", 'rb') as f:
    buffer = f.read()
    print(buffer)
    myio = io.BytesIO(buffer)
    print(myio)