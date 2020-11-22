import pandas as pd

from utils import rename_countries, BOATS

def read_data(path):

    df = pd.read_csv(f'{path}/countries.csv')

    return df

def get_continents(df):
    """
    Get list of countries with 3 letter codes and continents
    """

    to_drop = ['Continent_Code', 
               'Two_Letter_Country_Code', 
               'Country_Number']

    df = df.drop(to_drop, axis=1)

    df['Country'] = df['Country_Name'].apply(lambda x: x.split(", ")[0])
    df = df.rename(columns={"Continent_Name": "Continent", 'Three_Letter_Country_Code': 'Country Code'})
    df = df.drop(['Country_Name'], axis=1)
    df = df.drop_duplicates(subset=['Country'])

    return df

def switch_country_names(df):
    """
    Change values in countries.csv to match covid data.
    """

    to_swap = [('Russian Federation', 'Russia'),
               ('Slovakia (Slovak Republic)', 'Slovakia'),
               ('Kyrgyz Republic', 'Kyrgyzstan'),
               ('Syrian Arab Republic', 'Syria'),
               ('Libyan Arab Jamahiriya', 'Libya'),
               ('Korea, South', 'Korea'),
               ('Brunei Darussalam', 'Brunei'),
               ('Cabo Verde', 'Cape Verde'),
               ('Holy See (Vatican City State)', 'Holy See'),
               ('United States of America', 'US'),
               ('United Kingdom of Great Britain & Northern Ireland', 'United Kingdom'),
               ("Lao People's Democratic Republic", 'Laos'),
               ('Myanmar', 'Burma'),
               ('Czech Republic', 'Czechia'),
               ('Swaziland',  'Eswatini')]

    for x in to_swap:
        df.loc[df['Country'] == x[0], 'Country'] = x[1]

    return df

def make_continents(in_path, out_path):

    df = read_data(in_path)
    df = get_continents(df=df)
    df = switch_country_names(df=df)

    df = df[df['Continent'] != 'Antarctica']

    df.to_csv(f'{out_path}/continents.csv', index=False)

if __name__ == '__main__':

    in_path = './data/raw/datahub'
    out_path = './data/processed'

    make_continents(in_path=in_path,
                   out_path=out_path)        