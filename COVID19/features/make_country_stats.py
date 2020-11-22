from functools import reduce

import pandas as pd

from utils import read_data

def read_extra_data(path):

    active = pd.read_csv(f'{path}/active_cases.csv')    
    mort = pd.read_csv(f'{path}/mortality_rate.csv')        

    return (active, mort)

def get_country_stats(dataframes, names):
    """    
    Create dataframe with cases summarized by country.    
    """
    
    stats = []
    for df,name in zip(dataframes, names):
        tmp = df.tail(1).drop('Date', axis=1)
        tmp = tmp.transpose()
        tmp = tmp.reset_index()
        tmp.columns = ['Country', name]
        stats.append(tmp)

    stats = reduce(lambda x, y: pd.merge(x, y, on='Country', how='outer'), stats)    
    
    return stats

def make_country_stats(in_path, out_path):

    dataframes = list(read_data(path=in_path))
    dataframes += list(read_extra_data(path=in_path))
    
    names = ['Confirmed', 'Recovered', 'Dead', 'Active', 'Mortality']

    stats = get_country_stats(dataframes=dataframes, names=names)    

    stats.to_csv(f'{out_path}/country_stats.csv', index=False)

if __name__ == '__main__':

    in_path = './data/processed'
    out_path = './data/processed'

    make_country_stats(in_path=in_path,
                   out_path=out_path)    