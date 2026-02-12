import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata
import pandas as pd

# Load the gapminder dataset
df = pldata.gapminder()

# Get unique countries
countries = df['country'].unique()
countries = sorted(countries)

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server

# Define the layout
app.layout = html.Div([
    html.H1("GDP Per Capita Growth Dashboard"),
    
    html.Div([
        html.Label("Select Country:"),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': country, 'value': country} for country in countries],
            value='Canada'
        )
    ], style={'width': '40%', 'display': 'inline-block', 'marginBottom': '20px'}),
    
    dcc.Graph(id='gdp-growth')
])

# Define the callback
@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    # Filter the dataset for the selected country
    filtered_df = df[df['country'] == selected_country]
    
    # Create a line plot
    fig = px.line(filtered_df, 
                  x='year', 
                  y='gdpPercap',
                  title=f'GDP Per Capita Growth in {selected_country}',
                  labels={'year': 'Year', 'gdpPercap': 'GDP Per Capita (USD)'},
                  markers=True)
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
