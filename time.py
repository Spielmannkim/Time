import time
import sys

# 1970년 이후 지난 초/s
cur_time_sec = time.time()
print("%d: second" % cur_time_sec)

# 1분 = 60초, 60으로 나눠서 분/m 구하기.
min = cur_time_sec / 60
print("%d: minute" % min)

# 1시간 = 60분, 60으로 나눠서 시/h 구하기.
hour = min / 60
print("%d: hours" % hour)

days = hour / 24
print("%d: days" % days)

years = days / 365
print("passed, after 1970: %d years" % years)

cur_year = 1970 + years
print("%d year" % cur_year)
