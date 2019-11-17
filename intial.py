from web_scraper import simple_get
from record_man import parse_ib_symbol_record
from bs4 import BeautifulSoup
import time
import os
import csv

def ib_url_builder(exchange):
    return 'https://www.interactivebrokers.com/en/index.php?f=2222&exch=' + exchange + '&showcategories=STK&p=&cc=&limit=100&page='


def page_scraper(ib_exchange_url):
    '''
    It takes a page url (Interactive Brokers)
    It returns a dictionary mapping each symbol with a tuple
    (company name, symbol, currency)
    '''
    page = 0
    symbols = {}
    while True:
        page += 1
        time.sleep(1.01)
        print(page)
        url = ib_exchange_url + str(page)
        valid_page = False
        try:
            raw_html = simple_get(url)
            soup = BeautifulSoup(raw_html, 'html.parser')
            a = soup.find_all('tr')
            for tr in a:
                tr_str = str(tr).replace('\n', '')
                if tr_str[0:8] == '<tr><td>':
                    symbol_data = parse_ib_symbol_record(tr_str)
                    symbols[symbol_data[0]] = tuple ([symb for symb in symbol_data[1:]])
                    valid_page = True
        except:
            break
        if valid_page == False: break
    return symbols

def main():
    '''
    Source of data: https://www.interactivebrokers.com/en/index.php?f=1562
    Exchanges:
    - nasdaq
    - myse
    - amex
    - mexi
    - alpha: Exchange - Alpha ATS (ALPHA)
    - fwb: Frankfurt Stock Exchange (FWB)
    - bm: Exchange - Bolsa de Madrid (BM)
    - lse: London Stock Exchange (LSE)
    - chixch: CHI-X Europe Ltd Swiss (CHIXCH)
    - tase: Tel Aviv Stock Exchange
    - batech: BATS Europe (BATECH)
    - bux: Budapest Stock Exchange
    - asx: Australian Stock Exchange (ASX)
    - sehk: Hong Kong Stock Exchange (SEHK)
    - nse: National Stock Exchange of India (NSE)
    - tsej: Tokyo Stock Exchange (TSEJ)
    - sgx: Singapore Exchange (SGX)
    '''

    exchanges = ('nasdaq', 'nyse', 'amex', 'mexi', 'alpha',
                 'fwb', 'bm', 'lse', 'chixch', 'tase', 'batech',
                 'bux', 'asx', 'sehk', 'nse', 'sgx')

    output_folder = r'C:\quantitative_value\symbols_files'
    os.chdir(output_folder)

    for exchange in exchanges:
        print(f'exchange: {exchange}')
        symbols = page_scraper(ib_url_builder(exchange))
        file_name = exchange + '.csv'
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for symbol in symbols.keys():
                row = [symbol, ] + [item for item in symbols[symbol]]
                writer.writerow(row)

if __name__ == '__main__':
    main()
