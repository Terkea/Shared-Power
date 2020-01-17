import calendar
from datetime import date, datetime

today = date.today()
test_date = datetime(2020, 1, 31)
this_month = today.strftime("%m")

def get_last_day_of_month(month):
    return calendar.monthrange(2020, month)[1]

# print(test_date.strftime("%d"))
# print(last_day_of_month)

if int(test_date.strftime("%d")) is int(get_last_day_of_month(int(this_month))):
    print("yee")
else:
    print("noo")