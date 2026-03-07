"""
Today were going to deal with date and time in Python
Python got an in-built module to deal with date and time
In date and time module we only deal with the following functions;
date
datetime
time
timedelta
"""

#Dealing with datetime information

from datetime import datetime
now = datetime.now()
print(now)                      # 2026-03-07 13:32:56.833187
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

#Formatting Date Output using strftime

from datetime import datetime
new_year = datetime(2026, 3, 7) # 2026-03-07
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)
"""
The strftime() method in Python stands for "string format time" 
and is used to convert a date, time, 
or datetime object into a human-readable 
string representation based on a specified format
"""
from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)           # time: 13:43:25
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)        # time one: 03/07/2026, 13:43:25
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)        # time two: 07/03/2026, 13:43:25