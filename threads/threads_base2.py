from time import sleep, time
import threading


def get_data(data, value):
    for _ in range(value):
        print(f'{threading.current_thread().name} - {data}')
        sleep(0.5)


thr_list = []

for i in range(3):
    thr = threading.Thread(target=get_data, args=(str(time()), i), name=f'thr-{i}')
    thr.start()
    thr_list.append(thr)

for thr in thr_list:
    thr.join()

print('finish')

# автор оставил без ответа столь занимательный вывод
# thr-1 - 1678638830.0354524
# thr-2 - 1678638830.0356212
# thr-2 - 1678638830.0356212
# finish