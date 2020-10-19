import os
import sys
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

import db_session as db_session

def main():
    print('Main was called')
    db_setup()

def db_setup():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'my_db.sqlite')

    db_session.global_init(db_file)

if __name__ == '__main__':
    main()


