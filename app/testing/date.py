# day + booking_period
# 2020/01/15 + 3
import datetime

x = datetime.datetime(2020, 1, 15)
deltatime_other_booking = x + datetime.timedelta(days=2.5)
print(f"other booking {x}")
print(f"other booking deltatime {deltatime_other_booking}")

# my_day + my_booking_period
# 2020/01/16 + 1
print("\n")

y = datetime.datetime(2020, 1, 16)
deltatime_my_booking = y + datetime.timedelta(days=1)
print(f"my booking {y}")
print(f"my booking deltatime {deltatime_my_booking}")

print(f"AVAILABILITY: {deltatime_other_booking-deltatime_my_booking}")

print(deltatime_other_booking > deltatime_my_booking)