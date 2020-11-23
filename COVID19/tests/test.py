import pandas as pd
import unittest

class TestCovidCases(unittest.TestCase):

    def setUp(self):

        self.confirmed_cases = pd.read_csv('./data/processed/confirmed_cases.csv')
        self.recovered_cases = pd.read_csv('./data/processed/recovered_cases.csv')
        self.dead_cases = pd.read_csv('./data/processed/dead_cases.csv')
        self.active_cases = pd.read_csv('./data/processed/active_cases.csv')                

    def test_confirmed_boats(self):

        countries = set(self.confirmed_cases.columns)

        self.assertNotIn('MS Zaandam', countries)
        self.assertNotIn('Diamond Princess', countries)

    def test_recovered_boats(self):

        countries = set(self.recovered_cases.columns)

        self.assertNotIn('MS Zaandam', countries)
        self.assertNotIn('Diamond Princess', countries)

    def test_dead_boats(self):

        countries = set(self.dead_cases.columns)

        self.assertNotIn('MS Zaandam', countries)
        self.assertNotIn('Diamond Princess', countries)

    def test_active_boats(self):

        countries = set(self.active_cases.columns)

        self.assertNotIn('MS Zaandam', countries)
        self.assertNotIn('Diamond Princess', countries)

if __name__ == '__main__':

    unittest.main()