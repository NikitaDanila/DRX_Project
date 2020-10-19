import os
import time

import db_session as db_session
from echipamente import Echipamente
from producatori import Producatori




def main():
    init_db()
    insert_rows()


def insert_rows():

    session = db_session.create_session()
    start_time = time.time()
    row_num = 5000  # int(input("Select how many number of rows to insert: "))

    for i in range(row_num):
        p = Producatori()
        p.nume_producator = "DRX"
        e = Echipamente()
        e.nume_echipament = "Cablaj"
        session.add(e)
        session.add(p)
        if i % 1000 == 0:
            session.flush()

    session.commit()
    print("--- %s seconds ---" % (time.time() - start_time))


def init_db():
    top_folder = os.path.dirname(__file__)
    rel_file = os.path.join('..', 'db', 'my_db.sqlite')
    db_file = os.path.abspath(os.path.join(top_folder, rel_file))
    db_session.global_init(db_file)


if __name__ == '__main__':
    main()
