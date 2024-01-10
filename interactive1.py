import pandas as pd
import plotly.express as px
from ipywidgets import interact

file_path = '/Users/caterinasapuppo/Desktop/dati.xlsx'

df = pd.read_excel(file_path)

columns_to_keep = ["Country"] + [str(year) for year in range(2000, 2022)]
life_expectancy_data = df[columns_to_keep]
life_expectancy_data = life_expectancy_data.rename(columns={"Unnamed: 0": "Country"})
life_expectancy_data_melted = life_expectancy_data.melt(id_vars=["Country"], var_name="Year", value_name="Life Expectancy")

def plot_life_expectancy(country):
    filtered_data = life_expectancy_data_melted[life_expectancy_data_melted['Country'] == country]
    fig = px.line(filtered_data, 
                  x="Year", 
                  y="Life Expectancy", 
                  title=f"Life Expectancy at Birth for {country} from 2000 to 2021",
                  markers=True)
    
    fig.update_traces(line=dict(color='black', width=2))
    fig.update_xaxes(showline=True, linewidth=1, linecolor='black', mirror=True, title='')
    fig.update_yaxes(showline=True, linewidth=1, linecolor='black', mirror=True, title='')
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)
    fig.update_layout(autosize=False, width=800, height=600, 
                      plot_bgcolor='white', 
                      margin=dict(l=20, r=20, t=50, b=20),
                      title_font=dict(color='black'), 
                      font=dict(color='black'))
    
    fig.show()

interact(plot_life_expectancy, country=life_expectancy_data['Country'].unique())
