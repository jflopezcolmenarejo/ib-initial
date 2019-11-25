import sqlite3
import os

def exchange_list():
    '''
    Returns a dictionary of Exchanges covered by the solution
    '''
    exchanges = {}
    exchanges[0] = ('nyse', 'New York Stock Exchange')
    exchanges[1] = ('amex', 'American Stock Exchange')
    exchanges[2] = ('nasdaq', 'National Association of Securities Dealers Automated Quotations')
    exchanges[3] = ('alpha', 'Toronto Stock Exchange Alpha Exchange')
    exchanges[4] = ('fwb', 'Frankfurt Stock Exchange')
    exchanges[5] = ('lse', 'London Stock Exchange')
    exchanges[6] = ('chixch', 'CHI-X Europe Ltd Swiss')
    exchanges[7] = ('bm', 'Bolsa de Madrid')
    exchanges[8] = ('asx', 'Australian Stock Exchange')
    exchanges[9] = ('tsej', 'Tokyo Stock Exchange')
    exchanges[10] = ('sgx', 'Singapore Exchange')
    exchanges[11] = ('tase', 'Tel Aviv Stock Exchange')
    exchanges[12] = ('batech', 'BATS Europe')
    exchanges[13] = ('sehk', 'Hong Kong Stock Exchange')
    exchanges[14] = ('nse', 'National Stock Exchange of India')
    exchanges[15] = ('mexi', 'Mexican Stock Exchange')
    exchanges[16] = ('bux', 'Budapest Stock Exchange')

    return exchanges


def create_connection(db_path, db_file):
    '''
    Create a database connection to the SQLite database
    specified by db_file
    :param db_file: database file
    :return: Connection object or None
    '''
    conn = None
    os.chdir(db_path)
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_exchange_table(conn):
    c = conn.cursor()
    c.execute('''SELECT count(name) FROM sqlite_master WHERE type="table" AND name="exchange" ''')
    if c.fetchone()[0] != 1:
        c.execute('''CREATE TABLE exchange (id INTEGER PRIMARY KEY,
                  code TEXT UNIQUE, description TEXT)''')
        print('table exchange created')
    else:
        print('table exchange not created')
    return True

def add_record_to_exchange_table(conn, id, code, description):
    sql = "INSERT INTO exchange (id, code, description) VALUES (?,?,?)"
    c = conn.cursor()
    try:
        c.execute("INSERT INTO exchange (id, code, description) VALUES (?,?,?)")
        print(id)
    except:
        print(f'something went wrong: {id} - {code}')
    return c.lastrowid

def main():
    db_path = r'C:\quantitative_value'
    db_file = 'ib.db'
    conn = create_connection(db_path, db_file)
    create_exchange_table(conn)
    exchanges = exchange_list()
    for id, exchange in exchanges.items():
        add_record_to_exchange_table(conn, id, exchange[0], exchange[1])
    
    c = conn.cursor()
    c.execute('''SELECT * FROM exchange''')
    rows = c.fetchall()
    print(rows)

    for row in rows:
        print('row in exchange: ', row)  
    conn.close()

if __name__ == '__main__':
    main()