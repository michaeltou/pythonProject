
import pickle

d = dict(name='bob', age=25, occupation='Software Engineer')

f = open('test.pkl', 'wb')
pickle.dump(d, f)
f.close()



f= open('test.pkl', 'rb')
d = pickle.load(f)
print(d)
f.close()