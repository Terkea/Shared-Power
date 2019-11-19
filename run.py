import threading

import app.models
import app.view

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

