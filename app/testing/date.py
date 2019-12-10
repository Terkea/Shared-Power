from datetime import date, timedelta, datetime

today = date.today()
today_string = '2019-12-10'
deadline = '3.5'
round_deadline = round(float(deadline))

print(f"TODAY: {today}")
print(f"ROUNDED: {round_deadline}")
print(f"DEADLINE: {(datetime.strptime(today_string, '%Y-%m-%d') + timedelta(round_deadline))}")