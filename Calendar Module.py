import calendar

# print(calendar.calendar(2020))
# print(calendar.TextCalendar(firstweekday=6).formatyear(2015))
# # print(calendar.weekday(year, month, day))
# print(calendar.weekday(2015, 8, 5))

mm ,dd, yy = map(int, input().split())
print(calendar.weekday(yy, mm, dd))
d = calendar.weekday(yy, mm, dd)
print(calendar.day_name[d].upper())
# if d == 0:
#     print("MONDAY")
# elif d == 1:
#     print("TUESDAY")
# elif d == 2:
#     print("WEDNESDAY")
# elif d == 3:
#     print("THURSDAY")
# elif d == 4:
#     print("FRIDAY")
# elif d == 5:
#     print("SATURDAY")
# elif d == 6:
#     print("SUNDAY")