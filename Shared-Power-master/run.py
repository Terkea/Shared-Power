import threading

import app.models
import app.view

import calendar
from datetime import date, datetime

from app.models import session
from app.models.booking import Booking
from app.models.returns import Returns


def init_database():
    app.models.__init__


def init_gui():
    app.view.__init__

def generate_invoices():
    # today = date.today()
    # this_month = today.strftime("%m")
    # if int(today.strftime("%d")) is int(get_last_day_of_month(int(this_month))):
    #     _returns = session.query(Returns).filter(Returns.date < get_last_day_of_month(int(this_month))).all()
    #     _bookings = []
    #     for returns in _returns:
    #         amount = 0
    #         booking = session.query(Booking).filter(Booking.id == returns.booking_id)
    #         # returns.booking_id
    #         if returns.date > booking.booked_date + datetime.timedelta(days=float(booking.duration_of_booking)):
    #             amount += booking.daily_price
    pass


def get_last_day_of_month(month):
    return calendar.monthrange(2020, month)[1]


if __name__ == '__main__':
    # using separate threads for each package to improve the performance
    t = threading.Thread(target=init_database, args=())
    t.daemon = True
    t.start()

    t = threading.Thread(target=init_gui, args=())
    t.daemon = True
    t.start()

    t = threading.Thread(target=generate_invoices, args=())
    t.daemon = True
    t.start()
