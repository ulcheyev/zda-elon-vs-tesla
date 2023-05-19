import pandas as pd
import utils as ut
import matplotlib.dates as dates
import matplotlib.pyplot as plt
from datetime import datetime

DATE_COLUMN_LABEL = 'Date'
COLUMN_VOLUME = 'Volume'
COLUMN_ANALYSIS_LABEL = 'Close'


stocks = ut.get_df('../data/tesla-stock-prices.csv')
stocks_opponent = ut.get_df("../data/google-stock-prices.csv")

df = stocks[[DATE_COLUMN_LABEL, COLUMN_ANALYSIS_LABEL, COLUMN_VOLUME]]
df_opponent = stocks_opponent[[DATE_COLUMN_LABEL, COLUMN_ANALYSIS_LABEL, COLUMN_VOLUME]]


def process_stocks():
    # Change date-time format
    ut.round_col(df, 'Close', 3)
    ut.write_data_frame_to_csv("tesla-stock-prices.csv", df)


def print_info_about_analysis_column():
    print(df.describe())


'''
Draw close plot
'''


def draw_plot(df, col_x, col_y):

    fig, ax = plt.subplots(figsize=(60, 10))
    ax.plot(df[col_x], df[col_y])

    ax.set_xticks(df[col_x][::20])
    ax.tick_params(axis='x', labelrotation=45, labelsize=15)

    plt.show()


'''
Draw diff close plot
'''


def diff_col_plot(df, col_x, col_d):
    df.loc[:, col_d + '_diff'] = df[col_d].diff()
    fig, ax = plt.subplots(figsize=(70, 15))
    ax.plot(df[col_x], df[col_d + '_diff'])

    ax.set_xticks(df[col_x][::20])
    ax.tick_params(axis='x', labelrotation=45, labelsize=15)
    plt.show()



'''
Draw diff proc close plot
'''


def diff_col_pr_plot(df, col_x, col_d, col_n):
    df[col_d+'_%'] = df[col_d] / df[col_n]
    fig, ax = plt.subplots(figsize=(70, 15))
    ax.plot(df[col_x], df[col_d + '_%'])
    ax.set_xticks(df[col_x][::20])
    ax.tick_params(axis='x', labelrotation=45, labelsize=15)
    plt.show()

def volume_col(df):

    fig, ax = plt.subplots(figsize=(70, 15))
    ax.plot(df['Date'], df['Volume'])

    ax.set_xticks(df['Date'][::20])
    ax.tick_params(axis='x', labelrotation=45, labelsize=15)

    plt.show()
def draw_two_plots(df1, df2, col_x, col_y):

    fig, ax = plt.subplots(figsize=(70, 15))
    ax.plot(df1[col_x], df1[col_y], color='blue', label='df1')
    ax.plot(df2[col_x], df2[col_y], color='red', label='df2')
    ax.set_xticks(df[col_x][::20])
    ax.tick_params(axis='x', labelrotation=45, labelsize=15)
    ax.set_xlabel(col_x)
    ax.set_ylabel(col_y)
    ax.legend()
    plt.show()
