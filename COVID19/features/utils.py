import pandas as pd
from functools import reduce

BOATS = ['Diamond Princess', 'MS Zaandam']

def read_data(path):
    """
    Read cleaned cases datasets.
    """

    conf = pd.read_csv(f'{path}/confirmed_cases.csv')
    recov = pd.read_csv(f'{path}/recovered_cases.csv')
    dead = pd.read_csv(f'{path}/dead_cases.csv')

    return (conf, recov, dead)

def get_country_ts(country, dataframes, columns):
    """
    Extract data for specific country, apply backfill to NaN's.
    """
    
    cols = ['Date'] + columns
    ctry = list()
    
    for df in dataframes:
        tmp = df.loc[:, ['Date', country]]
        ctry.append(tmp) 

    ctry = reduce(lambda x, y: pd.merge(x, y, on='Date', how='outer'), ctry)    
    ctry.columns = cols
    ctry = ctry.fillna(method='bfill')
    
    return ctry

def rename_countries(df):
    """
    Rename countries.
    """

    df['Country'] = df['Country'].apply(lambda x: 'Taiwan' if x == 'Taiwan*' else x)
    df['Country'] = df['Country'].apply(lambda x: 'Korea' if x == 'Korea, South' else x)
    df['Country'] = df['Country'].apply(lambda x: 'Macedonia'  if x == 'North Macedonia' else x)
    df['Country'] = df['Country'].apply(lambda x: 'Cape Verde' if x == 'Cabo Verde' else x)
    df['Country'] = df['Country'].apply(lambda x: 'Congo' if x == 'Congo (Brazzaville)'  else x)
    df['Country'] = df['Country'].apply(lambda x: 'Congo' if x == 'Congo (Kinshasa)' else x)
    
    return df    

def remove_boats(df):
    """
    Remove cases that were recorded on boats.
    """

    df = df.drop(BOATS, axis=1)

    return df    