import csv
import os

def remove_extension(file_name):
    return file_name[0:file_name.find('.')]

def main():
    exchanges = ('nyse', 'amex')
    input_folder = r'C:\quantitative_value\symbols_files'
    output_folder = r'C:\quantitative_value\provisional'
    os.chdir(input_folder)

    ib_symbols_col = {}

    print(os.listdir(input_folder))

    for exchange_file in os.listdir(input_folder):
        exchange = remove_extension(exchange_file)
        with open(exchange_file, newline='') as r:
                r_reader = csv.reader(r, delimiter=',')
                for ib_symbol_record in r_reader:
                    ib_symbol = ib_symbol_record[0]
                    firm_name = ib_symbol_record[1]
                    symbol = ib_symbol_record[2]
                    currency = ib_symbol_record[3]
                    if ib_symbol in ib_symbols_col.keys():
                        ib_symbols_col[ib_symbol][3].append(exchange)
                        ib_symbols_col[ib_symbol][4].append(currency)
                    else:
                        ib_symbols_col[ib_symbol] = [ib_symbol, symbol, firm_name,
                                                     [exchange,], [currency,]]

    os.chdir(output_folder)

    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for ib_symbol in ib_symbols_col.keys():
            row = [item for item in ib_symbols_col[ib_symbol]]
            writer.writerow(row)
    
    exchanges = ('nasdaq', 'nyse', 'amex', 'mexi', 'alpha',
                 'fwb', 'bm', 'lse', 'chixch', 'tase', 'batech',
                 'bux', 'asx', 'sehk', 'nse', 'sgx')

    with open('nasdaq_no_nyse.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for ib_symbol in ib_symbols_col.keys():
            if 'nasdaq' in ib_symbols_col[ib_symbol][3] and 'nyse' not in ib_symbols_col[ib_symbol][3]:
                row = [item for item in ib_symbols_col[ib_symbol]]
                writer.writerow(row)


if __name__ == '__main__':
    main()