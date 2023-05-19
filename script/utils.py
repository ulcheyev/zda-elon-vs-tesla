import pandas as pd
from datetime import datetime
import csv


def get_df(filename):
    df = pd.read_csv(filename)
    return df


def write_data_frame_to_csv(filename, data):
    print('Write to file ../data/{}'.format(filename))
    data.to_csv('../data/' + filename)
    print('Write to file ../data/{}:'.format(filename), 'DONE')


def normalize_data_frame(df):
    return (df - df.min()) / (df.max() - df.min())

def round_col(df, cn, n):
    df[cn] = df[cn].apply(lambda x: round(x, n))


def convert_date_col(df, format):
    df.loc[:,'Date'] = df['Date'].apply(lambda x: pd.to_datetime(x, format=format).date())
    #df.loc[:, 'Date'] = pd.to_datetime([datetime.strptime(d, format).date() for d in df['Date']])
