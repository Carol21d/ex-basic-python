### Dates ###

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime


now = datetime.now()


def print_date(date):
    print(date.year)
    print(date.month)

    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(now)


year_2023 = datetime(2023, 1, 1)
print_date(year_2023)


current_time = time(21, 6, 0)  # aqui pasamos los parametros
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


current_time = date.today()
print(current_time.year)
print(current_time.month)
print(current_time.day)

current_time = date(2023, 6, 15)

current_time = date(current_time.year+1,
                    current_time.month + 1, current_time.day+1)
print(current_time.year, current_time.month, current_time.day)

diff = year_2023 - now
diff = year_2023.date() - current_time
print(diff)
