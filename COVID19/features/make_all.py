from make_cases import make_cases
from make_cases_daily_change import make_cases_daily_change
from make_cases_since_t0 import make_cases_since_t0
from make_continents import make_continents
from make_coordinates import make_coordinates
from make_country_stats import make_country_stats
from make_country_to_continent import make_country_to_continent
from make_mortality import make_mortality
from make_world_bank import make_world_bank

# Inputs
datahub_path = './data/raw/datahub'
covid_path = './data/raw/COVID-19/csse_covid_19_data/csse_covid_19_time_series'
world_bank_path = './data/raw/world_bank'

# Outputs
out_path = './data/processed'

# Datasets generated from raw data
make_cases(in_path=covid_path, out_path=out_path)

make_coordinates(in_path=covid_path, out_path=out_path)

make_continents(in_path=datahub_path, out_path=out_path)

# Datasets generate from cleaned data
make_cases_since_t0(in_path=out_path, out_path=out_path)        

make_cases_daily_change(in_path=out_path, out_path=out_path)

make_mortality(in_path=out_path, out_path=out_path)

make_country_stats(in_path=out_path, out_path=out_path)

make_country_to_continent(in_path=out_path, out_path=out_path)           

# Merge COVID-19 data with World Bank data
make_world_bank(in_path=world_bank_path, out_path=out_path)
