from functools import reduce

import pandas as pd

from utils import read_data

def get_cases_since_t0(df, n_cases_start=100):

    all_countries = sorted(df.drop('Date', axis=1).columns)

    conf_t0 = list()
    for country in all_countries:
        t0 = df[[country]]
        t0 = t0.loc[t0[country] >= n_cases_start]
        t0 = t0.reset_index(drop=True)
        conf_t0.append(t0)
        
    outer_join = lambda x, y: pd.merge(left=x, 
                                       right=y, 
                                       left_index=True, 
                                       right_index=True, 
                                       how='outer')

    conf_t0 = reduce(outer_join, conf_t0)    
    conf_t0.columns = all_countries
    conf_t0 = conf_t0.head(n_cases_start)
    # conf_t0 = conf_t0.dropna(axis=1)

    return conf_t0

def make_cases_since_t0(in_path, out_path):
    conf,_,_ = read_data(in_path)

    df = get_cases_since_t0(df=conf)

    df.to_csv(f'{out_path}/confirmed_cases_since_t0.csv', index=False)


if __name__ == '__main__':

    in_path = './data/processed'
    out_path = './data/processed'

    make_cases_since_t0(in_path=in_path,
                        out_path=out_path)        