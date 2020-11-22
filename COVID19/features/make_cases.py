import pandas as pd

from utils import remove_boats, rename_countries

def read_data(path):
    """
    Read data from ../data/COVID-19
    """

    conf = pd.read_csv(f'{path}/time_series_covid19_confirmed_global.csv')
    recov = pd.read_csv(f'{path}/time_series_covid19_recovered_global.csv')
    dead = pd.read_csv(f'{path}/time_series_covid19_deaths_global.csv')

    return (conf, recov, dead)

def process_data(df):
    """    
    Convert data from columns to rows.    
    """
    
    # Drop columns
    df = df.drop(['Lat', 'Long', 'Province/State'], axis=1)
    df = df.rename(columns={"Country/Region": "Country"})    
    
    # Rename countries
    df = rename_countries(df=df)
    
    # Enforce countries are unique
    df = df.groupby('Country', as_index=False).sum()        
    
    # Switch to colum format
    df = df.transpose()
    
    # Copy headers from first row
    df.columns = df.iloc[0, :].to_list()
    df['Date'] = df.index
    df = df[1:]    

    # Drop boats
    df = remove_boats(df=df)    
    
    # Convert dates
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Convert to ints
    cols = df.columns.to_list()
    cols.remove('Date')
    for col in cols:
        df[col] = df[col].astype(int)
    
    # Reorder & Sort    
    cols = ['Date'] + sorted(cols)
    df = df[cols]
        
    # Reset index
    df = df.reset_index(drop=True)
    df.head()    
    
    return df    

def make_cases(in_path, out_path):

    conf, recov, dead = read_data(path=in_path)

    conf = process_data(df=conf)
    recov = process_data(df=recov)
    dead = process_data(df=dead)

    active = conf.drop(['Date'], axis=1) 
    active -= recov.drop(['Date'], axis=1) 
    active -= dead.drop(['Date'], axis=1)
    active['Date'] = conf['Date']

    conf.to_csv(f'{out_path}/confirmed_cases.csv', index=False)
    recov.to_csv(f'{out_path}/recovered_cases.csv', index=False)
    dead.to_csv(f'{out_path}/dead_cases.csv', index=False)
    active.to_csv(f'{out_path}/active_cases.csv', index=False)

if __name__ == '__main__':

    in_path = './data/raw/COVID-19/csse_covid_19_data/csse_covid_19_time_series'
    out_path = './data/processed'

    make_cases(in_path=in_path,
               out_path=out_path)
