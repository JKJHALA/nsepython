from nsepython import *
logging.basicConfig(level=logging.CRITICAL)

SYMBOLS =['ITC']
for symbol in SYMBOLS:
    series = "EQ"
    start_date = "01-01-2018"
    end_date ="28-02-2025"
    data =equity_history(symbol,series,start_date,end_date)
    data.shape
    print(f'done {symbol}')
    data.to_csv(f'data/{symbol}v2.csv')

print('done')