from time import sleep
import threading


def get_data(data):
    while True:
        print(f'{threading.currentThread().name} - {data}')
        sleep(1)


thr = threading.Thread(target=get_data, args=('some data', ), name='thr-1')
thr.start()

for i in range(1000):
    print('current_thread')
    sleep(0.3)

    if i % 10 == 0:
        print('active thread: ', threading.active_count())
        print('enumerate: ', threading.enumerate())
        print('thr-1 is active: ', thr.is_alive())

        print('name: ', threading.main_thread().name)
        threading.main_thread().setName('new_name')
        print('name: ', threading.main_thread().name)
