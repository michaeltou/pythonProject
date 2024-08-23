import threading

local_data = threading.local()


def process_data(data):
    local_data.data = data
    print(local_data.data)


def process_thread(num):
    data = "Data for thread " + str(num)
    process_data(data)


for i in range(5):
    t = threading.Thread(target=process_thread, args=(i,))
    t.start()


