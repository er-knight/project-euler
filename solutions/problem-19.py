from datetime import datetime, timedelta

c = 0
d = datetime(1901, 1, 1)
e = datetime(2000, 12, 1)
while d < e:
    if d.day == 1 and d.weekday() == 6: # 6 -> sunday
        c += 1
    d += timedelta(days=1)

print(c)