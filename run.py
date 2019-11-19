import threading

import app.models
import app.view
from app.models.database_engine import session
from app.models.tools import Tools
from app.models.users import Users


def init_database():
    app.models.__init__
    print('DATABASE ON')


def init_gui():
    app.view.__init__
    print('LAUNCHING CLIENT')


if __name__ == '__main__':
    print(session.query(Users).all())
    # using separate threads for each package to improve the performance
    t = threading.Thread(target=init_database, args=())
    t.daemon = True
    t.start()

    t = threading.Thread(target=init_gui, args=())
    t.daemon = True
    t.start()

