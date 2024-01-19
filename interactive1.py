import pandas as pd
import plotly.express as px
import streamlit as st

# Function to load data and preprocess
@st.cache
def load_and_preprocess_data(file_path):
    df = pd.read_excel(file_path)
    
    # Select relevant columns (years 2000-2021)
    columns_to_keep = ["Country"] + [str(year) for year in range(2000, 2022)]
    life_expectancy_data = df[columns_to_keep]
    
    # Rename columns
    life_expectancy_data = life_expectancy_data.rename(columns={"Unnamed: 0": "Country"})
    
    # Melt the data for better visualization
    life_expectancy_data = life_expectancy_data.melt(id_vars=["Country"], var_name="Year", value_name="Life Expectancy")
    
    return life_expectancy_data

# Load and preprocess the data
life_expectancy_data_melted = load_and_preprocess_data('dati.xlsx')

# Sidebar for country selection
country = st.sidebar.selectbox('Select a Country', life_expectancy_data_melted['Country'].unique())

# Filter data based on the selected country
filtered_data = life_expectancy_data_melted[life_expectancy_data_melted['Country'] == country]

# Create a line plot using Plotly Express
fig = px.line(
    filtered_data, 
    x="Year", 
    y="Life Expectancy", 
    title=f"Life Expectancy at Birth for {country} from 2000 to 2021",
    markers=True,
    line_shape='linear',  # Use linear line shape
    line=dict(color='black', width=2)  # Customize line color and width
)

# Customize axes and plot layout
fig.update_xaxes(
    showline=True, 
    linewidth=1, 
    linecolor='black', 
    mirror=True, 
    title='', 
    showgrid=False,  # Remove grid lines
    zeroline=False  # Remove zero line
)

fig.update_yaxes(
    showline=True, 
    linewidth=1, 
    linecolor='black', 
    mirror=True, 
    title='', 
    showgrid=False,  # Remove grid lines
    zeroline=False  # Remove zero line
)

fig.update_layout(
    autosize=False, 
    width=800, 
    height=600, 
    plot_bgcolor='white', 
    margin=dict(l=20, r=20, t=50, b=20),
    title_font=dict(color='darkgrey'), 
    font=dict(color='black')
)

# Display the plot in Streamlit
st.plotly_chart(fig)
