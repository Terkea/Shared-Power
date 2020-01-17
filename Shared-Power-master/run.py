import threading

import app.models
import app.view

import calendar
from datetime import datetime
from datetime import date

from app.models import session
from app.models.booking import Booking
from app.models.returns import Returns


def init_database():
    app.models.__init__


def init_gui():
    app.view.__init__


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
