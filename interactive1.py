import pandas as pd
import plotly.express as px
import streamlit as st

# Read the data
@st.cache
def load_data(file_path):
    df = pd.read_excel(file_path)
    columns_to_keep = ["Country"] + [str(year) for year in range(2000, 2022)]
    life_expectancy_data = df[columns_to_keep]
    life_expectancy_data = life_expectancy_data.rename(columns={"Unnamed: 0": "Country"})
    return life_expectancy_data.melt(id_vars=["Country"], var_name="Year", value_name="Life Expectancy")

life_expectancy_data_melted = load_data('dati.xlsx')

# Sidebar for country selection
country = st.sidebar.selectbox('Select a Country', life_expectancy_data_melted['Country'].unique())

# Filter data based on selection
filtered_data = life_expectancy_data_melted[life_expectancy_data_melted['Country'] == country]

# Plotting
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
                  title_font=dict(color='white'), 
                  font=dict(color='black'))

# Display the plot
st.plotly_chart(fig)

