
import threading, time

def my_function(name):

    print('param name = %s , thread %s is starting' % (name, threading.current_thread().name))
    n = 0
    while n<5:
        n = n+1
        print('thread {} is running {} times'.format(threading.current_thread().name, n))
        time.sleep(2)
    print('thread %s is ending'%threading.current_thread().name)


t = threading.Thread(target=my_function, args=('John',), name='subthread')
t.start()
t.join()
print('main thread is ending')



