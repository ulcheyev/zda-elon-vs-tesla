from datetime import datetime
import utils
import yfinance as yf

DATE_STR_FORMAT = '%Y-%m-%d'


def get_stocks(filename, company_name, since, until):
    print('Getting stock prices: {}, interval: {} - {}'
          .format(company_name, since, until))
    company = yf.Ticker(company_name)
    prices = company.history(start=since, end=until)
    print('Getting stock prices: DONE')
    utils.write_data_frame_to_csv(filename, prices)


date_since = datetime(2012, 1, 2).strftime(DATE_STR_FORMAT)
date_until = datetime(2023, 1, 2).strftime(DATE_STR_FORMAT)

# Tesla
# get_stocks('tesla-stock-prices.csv', 'TSLA', date_since, date_until)

# Opponent
# get_stocks('google-stock-prices.csv', 'KO', date_since, date_until)
