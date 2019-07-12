import time
from datetime import datetime
import threading

s_dt = datetime.now()
print(s_dt) # 타임 스탬프 : 보통 로그 작성 또는 프로그램 성능 측정시 사용하는 명령어

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print('End')

e_dt = datetime.now()
print(e_dt)
print(e_dt-s_dt)
