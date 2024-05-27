# ~/Desktop/covid19_dashboard/src/data_processing.py

import pandas as pd

def fetch_data():
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv'
    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def process_data(data):
    if data is None or data.empty:
        print("No data received to process.")
        return pd.DataFrame()
    df = data[['Country_Region', 'Confirmed', 'Deaths', 'Recovered']]
    df.rename(columns={'Country_Region': 'Country', 'Confirmed': 'TotalConfirmed', 'Deaths': 'TotalDeaths', 'Recovered': 'TotalRecovered'}, inplace=True)
    return df

def load_data():
    data = fetch_data()
    return process_data(data)
