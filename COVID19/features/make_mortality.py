from functools import reduce

import numpy as np
import pandas as pd

from utils import get_country_ts, read_data

def get_mortality_data(country, confirmed, dead):
    """    
    Calculate mortality rate over time
    for specific country.    
    """
    
    df = get_country_ts(country=country, 
                        dataframes=[confirmed, dead], 
                        columns=['Confirmed', 'Deaths'])

    df = df[df['Confirmed'] > 0]
    df['Mortality'] = df['Deaths'] / df['Confirmed']
    df['Mortality'] = df['Mortality'] * 100
    df['Mortality'] = np.round(df['Mortality'], 2)
    df = df[['Date', 'Mortality']]
    df.columns = ['Date', country]
    
    return df

def make_mortality(in_path, out_path):

    conf,_,dead = read_data(in_path)

    all_countries = sorted(set(conf.drop('Date', axis=1).columns))

    mort = list()
    for c in all_countries:
        tmp = get_mortality_data(country=c, 
                                confirmed=conf, 
                                dead=dead)
        mort.append(tmp)
        
    mort = reduce(lambda x, y: pd.merge(x, y, on='Date'), mort)    

    mort.to_csv(f'{out_path}/mortality_rate.csv', index=False)

if __name__ == '__main__':

    in_path = './data/processed'
    out_path = './data/processed'

    make_mortality(in_path=in_path,
                   out_path=out_path)    
