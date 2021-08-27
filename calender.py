import calendar
# some more liberaries like "import datetime", "import time"
# ("3" is print three first 3 characters of day)
#print(calendar.weekheader(3))
#print()

#print(calendar.firstweekday())
#print()

#print(calendar.month(2021, 2, w=3))

#print(calendar.monthcalendar(2021, 2))  # two dimensional Array

print(calendar.calendar(2021))  # whole year calender

day_of_the_week = calendar.weekday(2021, 1, 1)
#print(day_of_the_week)

is_leap = calendar.isleap(2021)
#print(is_leap)


how_many_leap_days = calendar.leapdays(2000, 2021)
#print(how_many_leap_days)