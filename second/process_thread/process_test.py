
import os

print("Process ID:", os.getpid())

pid = os.fork()

if pid == 0:
    print("Child process ID:", os.getpid())
else:
    print("Parent process ID:", os.getpid())