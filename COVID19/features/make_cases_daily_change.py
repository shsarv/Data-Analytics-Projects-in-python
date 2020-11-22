from functools import reduce

import pandas as pd

from utils import read_data

def get_daily_changes(df):   
    """
    
    Calculate daily change in case
    data, ie apply difference operator.
    
    """

    diff = df.drop(['Date'], axis=1) - df.drop(['Date'], axis=1).shift(1)
    diff['Date'] = df['Date']
    diff = diff.fillna(0)

    return diff

def make_cases_daily_change(in_path, out_path):
    conf,_,_ = read_data(in_path)

    df = get_daily_changes(df=conf)

    df.to_csv(f'{out_path}/confirmed_cases_daily_change.csv', index=False)


if __name__ == '__main__':

    in_path = './data/processed'
    out_path = './data/processed'

    make_cases_daily_change(in_path=in_path,
                        out_path=out_path)        