#Task3

import plotly.express as px
import plotly.data as pldata
import webbrowser

# Load the wind dataset
df = pldata.wind(return_type='pandas')

# Print the first and last 10 lines of the DataFrame
print("First 10 lines of the DataFrame:")
print(df.head(10))
print("\nLast 10 lines of the DataFrame:")
print(df.tail(10))

# Clean the data - convert 'strength' column to float
# Use str.replace() with regex to remove any non-numeric characters except decimal point
df['strength'] = df['strength'].astype(str).str.replace(r'[^\d.]', '', regex=True)
df['strength'] = df['strength'].astype(float)

# Create an interactive scatter plot
fig = px.scatter(df, 
                 x='frequency', 
                 y='strength',
                 color='direction',
                 title='Wind Strength vs. Frequency by Direction',
                 labels={'frequency': 'Frequency', 'strength': 'Strength', 'direction': 'Direction'},
                 hover_data=['frequency', 'strength', 'direction'])

# Save the HTML file
fig.write_html('wind.html')
print("\nHTML file saved as wind.html")

# Load and display the HTML file
webbrowser.open('wind.html')
print("Opening wind.html in default web browser...")

# Show the plot
fig.show()
