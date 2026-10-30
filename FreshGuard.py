import time
from datetime import datetime

def proses_data(suhu, kelembapan):
    if suhu >= 25 or kelembapan >= 70:
        status = "PERINGATAN"
    else:
        status = "NORMAL"

    return status

while True:
    suhu = 28.0
    kelembapan = 85.0

    status = proses_data(suhu, kelembapan)

    print(f"Waktu       : {datetime.now():%H:%M:%S}")
    print(f"Suhu        : {suhu} C")
    print(f"Kelembapan  : {kelembapan}%")
    print(f"Status      : {status}")
    print("-" * 30)

    time.sleep(5)