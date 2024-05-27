# ~/Desktop/covid19_dashboard/src/dashboard.py

from dash import Dash, dcc, html
import plotly.express as px
from data_processing import load_data

# Load and process data
data = load_data()
print(data.head())  # Add this line to print the first few rows of the data for debugging

# Initialize the Dash app
app = Dash(__name__)

def create_dashboard(data):
    if data.empty:
        return html.Div([
            html.H1("COVID-19 Data Dashboard"),
            html.P("Failed to load data.")
        ])
    
    # Create bar charts
    fig_confirmed = px.bar(data, x='Country', y='TotalConfirmed', title='Total Confirmed Cases by Country')
    fig_deaths = px.bar(data, x='Country', y='TotalDeaths', title='Total Deaths by Country')
    fig_recovered = px.bar(data, x='Country', y='TotalRecovered', title='Total Recovered Cases by Country')

    return html.Div([
        html.H1("COVID-19 Data Dashboard"),
        dcc.Graph(figure=fig_confirmed),
        dcc.Graph(figure=fig_deaths),
        dcc.Graph(figure=fig_recovered)
    ])

app.layout = create_dashboard(data)

if __name__ == "__main__":
    app.run_server(debug=True)
