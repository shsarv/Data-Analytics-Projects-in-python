import pandas as pd

def read_data(path):

    countries = pd.read_csv(f'{path}/continents.csv')
    coordinates = pd.read_csv(f'{path}/coordinates.csv')

    return (countries,coordinates)

def get_ctry_to_cont(ctry, coord):

    df = pd.merge(coord, ctry, how='left', on='Country')
    df = df.dropna()
    
    return df

def make_country_to_continent(in_path, out_path):
    
    ctry, coord = read_data(path=in_path)
    df = get_ctry_to_cont(ctry=ctry, coord=coord)

    df.to_csv(f'{out_path}/country_to_continent.csv', index=False)

if __name__ == '__main__':

    in_path = './data/processed'
    out_path = './data/processed'

    make_country_to_continent(in_path=in_path,
                   out_path=out_path)            