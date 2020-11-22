from functools import reduce

import pandas as pd

from utils import remove_boats, rename_countries

def read_data(path):
    """
    Read data from the World Bank.
    """

    files = [('SP.DYN.LE00.IN', 'Life expectancy'),
             ('NY.GDP.PCAP.PP.CD', 'GDP per capita'),             
             ('SP.URB.TOTL.IN.ZS', 'Urban population %'),
             ('SP.RUR.TOTL.ZS', 'Rural population %'), 
             ('EN.POP.SLUM.UR.ZS', 'Slum population %'),
             ('SP.POP.TOTL', 'Population'),
             ('SH.XPD.CHEX.GD.ZS', 'GDP Healthcare %')]

    dataframes = []

    for f,desc in files:
        df = pd.read_csv(f'{path}/{f}.csv')
        df = df.rename(columns={df.columns[2]: desc})
        dataframes.append(df)

    return dataframes

def read_codes(path):

    covid_codes = pd.read_csv(f'{path}/continents.csv')

    wb_codes = pd.read_csv(f'{path}/world_bank_codes.csv')

    return covid_codes, wb_codes

def read_stats(path):

    stats = pd.read_csv(f'{path}/country_stats.csv')    

    return stats 

def get_world_bank_data(df):
    """
    Get World Bank data into usable format.
    """
    
    df = df.rename(columns={'country': 'Country', 'date': 'Date'})
    df = df.dropna()

    latest = df.groupby(['Country'])
    latest = latest['Date'].max().to_frame()
    latest = latest.reset_index()

    cols = ['Country', 'Date']
    df = pd.merge(latest, df, left_on=cols, right_on=cols)
    df = df.drop('Date', axis=1)

    return df 

def make_world_bank(in_path, out_path):

    covid_codes, wb_codes = read_codes(path=out_path)

    stats = read_stats(path=out_path)

    dataframes = read_data(path=in_path)

    for i in range(len(dataframes)):
        dataframes[i] = get_world_bank_data(df=dataframes[i])

    outer_join = lambda x, y: pd.merge(x, y, on='Country', how='outer')

    # Merge data from World Bank into one datast
    world_bank = reduce(outer_join, dataframes)
    world_bank = pd.merge(world_bank, wb_codes, left_on=['Country'], right_on=['Country Name'])

    # Get data about covid ready to join.
    countries = pd.merge(covid_codes, stats, on='Country')
    # countries = countries.drop(['Continent', 'Country'], axis=1)

    # Join datasets on 3 letter country code.
    world_bank = pd.merge(countries, world_bank, on='Country Code')

    # Use countries from original covid data.
    world_bank = world_bank.drop(['Country_y', 'Country Name', 'Country Code'], axis=1)
    world_bank = world_bank.rename(columns={'Country_x': 'Country', 'Mortality': 'Mortality %'})

    world_bank = world_bank[world_bank['Confirmed'] > 5000]

    world_bank = world_bank[world_bank['Country'] != 'Yemen']

    median = world_bank['Life expectancy'].median()
    world_bank['Life expectancy'] = world_bank['Life expectancy'].fillna(median)

    median = world_bank['GDP Healthcare %'].median()
    world_bank['GDP Healthcare %'] = world_bank['GDP Healthcare %'].fillna(median)

    median = world_bank['GDP per capita'].median()
    world_bank['GDP per capita'] = world_bank['GDP per capita'].fillna(median)

    world_bank['Cases per mln'] = world_bank['Confirmed'] / world_bank['Population'] / 10 ** 6
    world_bank['Dead per mln'] = world_bank['Dead'] / world_bank['Population'] / 10 ** 6
    world_bank['Recovered per mln'] = world_bank['Recovered'] / world_bank['Population'] / 10 ** 6

    # world_bank['Dead per 100 cases'] = world_bank['Dead'] / world_bank['Confirmed'] / 100
    # world_bank['Recovered per 100 cases'] = world_bank['Recovered'] / world_bank['Confirmed'] / 100    

    world_bank = world_bank[sorted(world_bank.columns)]

    # Missing values
    world_bank = world_bank.drop(['Confirmed', 'Active', 'Dead', 'Recovered', 'Urban population %',
                                  'Slum population %', 'Population'], axis=1)

    print(world_bank.head())

    world_bank.to_csv(f'{out_path}/world_bank.csv', index=False)

if __name__ == '__main__':

    in_path = './data/raw/world_bank'
    out_path = './data/processed'

    make_world_bank(in_path=in_path,
                    out_path=out_path)