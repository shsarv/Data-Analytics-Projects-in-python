import pandas as pd

from utils import rename_countries, BOATS

def read_data(path):

    df = pd.read_csv(f'{path}/time_series_covid19_confirmed_global.csv')

    return df

def get_coords(df):
    """
    Get a list of countries with coordinates
    """

    df = df.rename(columns={"Country/Region": "Country"})   
    df = df.loc[~df['Country'].isin(BOATS)]
    df = rename_countries(df=df)
    df = df[['Country', 'Lat', 'Long']]
    df = df.groupby('Country', as_index=False).mean()
    df = df.sort_values('Country')
    df.transpose()
    df = df.reset_index(drop=True)

    return df

def make_coordinates(in_path, out_path):

    df = read_data(in_path)
    df = get_coords(df=df)
    
    df.to_csv(f'{out_path}/coordinates.csv', index=False)

if __name__ == '__main__':

    in_path = './data/raw/COVID-19/csse_covid_19_data/csse_covid_19_time_series'
    out_path = './data/processed'

    make_coordinates(in_path=in_path,
                   out_path=out_path)        