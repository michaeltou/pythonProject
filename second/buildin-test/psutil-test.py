import psutil

print("CPU count:", psutil.cpu_count())

print("CPU count:", psutil.cpu_count(logical=False))


print("CPU usage: ", psutil.cpu_percent(percpu=True))

print("Memory usage:", psutil.virtual_memory().percent)

print("Disk usage:", psutil.disk_usage('/').percent)