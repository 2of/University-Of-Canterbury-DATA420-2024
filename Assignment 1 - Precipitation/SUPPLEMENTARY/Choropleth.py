import plotly.graph_objects as go
import pandas as pd
import pycountry
import geonamescache
def fips_to_iso(fips_code):
    gc = geonamescache.GeonamesCache()
    countries = gc.get_countries_by_names()
    iso_alpha3 = None
    for country in countries.values():
        if country['fips'] == fips_code:
            iso_alpha3 = country['iso3']
            break
    return iso_alpha3

# Read the CSV file
df = pd.read_csv('2023_rainfall.csv')  # Replace 'your_file.csv' with the path to your CSV file
df['country_iso'] = df['country'].apply(fips_to_iso)


# Define your Plotly choropleth map
mean_avg_measurement = df['avg_measurement'].mean()
print(mean_avg_measurement)
equatorial_guinea_row = df[df['country_iso'] == 'GNQ']
print(equatorial_guinea_row)
# Define hovertemplate
hover_text = []
for index, row in df.iterrows():
    hover_text.append(f'{row["country"]}: {row["avg_measurement"]}')



fig = go.Figure(go.Choropleth(
    locations=df['country_iso'],
    z=df['avg_measurement'].astype(float),
    text=df['country'],
    colorscale='Viridis', 
    autocolorscale=True,
    marker_line_color='white',  
    colorbar_title='Rainfall (MM) P.A.',  

))

# Add title
fig.update_layout(
    title_text='Rainfall MM 2023',
    geo=dict(
        showcoastlines=True,  # show country borders
    )
)



# Show the map
fig.show()



