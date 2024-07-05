# import pandas as pd
# import plotly.graph_objects as go
# import streamlit as st

# # Load data from CSV
# df = pd.read_csv('covid_19_clean_complete.csv')

# # Set up Streamlit app
# st.title('COVID-19 Statistics by WHO Region')

# # Group data by WHO Region and aggregate required attributes
# grouped_df = df.groupby('WHO Region').agg({
#     'Confirmed': 'sum',
#     'Deaths': 'sum',
#     'Recovered': 'sum',
#     'Active': 'sum'
# }).reset_index()

# # Create a bar chart using Plotly
# fig = go.Figure()

# # Add bars to the chart
# fig.add_trace(go.Bar(
#     x=grouped_df['WHO Region'],
#     y=grouped_df['Confirmed'],
#     name='Confirmed',
#     marker_color='blue'
# ))

# fig.add_trace(go.Bar(
#     x=grouped_df['WHO Region'],
#     y=grouped_df['Deaths'],
#     name='Deaths',
#     marker_color='red'
# ))

# fig.add_trace(go.Bar(
#     x=grouped_df['WHO Region'],
#     y=grouped_df['Recovered'],
#     name='Recovered',
#     marker_color='green'
# ))

# fig.add_trace(go.Bar(
#     x=grouped_df['WHO Region'],
#     y=grouped_df['Active'],
#     name='Active',
#     marker_color='orange'
# ))

# # Customize layout
# fig.update_layout(
#     title='COVID-19 Statistics by WHO Region',
#     xaxis=dict(title='WHO Region'),
#     yaxis=dict(title='Count'),
#     barmode='group',
#     legend=dict(title='Category'),
#     template='plotly_white'
# )

# # Display plot in Streamlit
# st.plotly_chart(fig)


import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu

# Load data from CSV
df = pd.read_csv('covid_19_clean_complete.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set up Streamlit app
st.title('COVID-19 Statistics by WHO Region')

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        "Menu",
        ["Confirmed Cases", "Deaths", "Recovered", "Active","Aggregate", "Map"],
        icons=["bar-chart-line", "bar-chart-line", "bar-chart-line", "bar-chart-line","bar-chart-line", "map"],
        menu_icon="cast",
        default_index=0,
    )

# Group data by WHO Region and aggregate required attributes
grouped_df = df.groupby('WHO Region').agg({
    'Confirmed': 'sum',
    'Deaths': 'sum',
    'Recovered': 'sum',
    'Active': 'sum'
}).reset_index()

# Create a bar chart using Plotly
fig = go.Figure()

# Determine which data to show based on the selection
if selected == "Confirmed Cases":
    fig.add_trace(go.Bar(
        x=grouped_df['WHO Region'],
        y=grouped_df['Confirmed'],
        name='Confirmed',
        marker_color='blue'
    ))
    title = 'Confirmed COVID-19 Cases by WHO Region'
elif selected == "Deaths":
    fig.add_trace(go.Bar(
        x=grouped_df['WHO Region'],
        y=grouped_df['Deaths'],
        name='Deaths',
        marker_color='red'
    ))
    title = 'COVID-19 Deaths by WHO Region'
elif selected == "Recovered":
    fig.add_trace(go.Bar(
        x=grouped_df['WHO Region'],
        y=grouped_df['Recovered'],
        name='Recovered',
        marker_color='green'
    ))
    title = 'Recovered COVID-19 Cases by WHO Region'
elif selected == "Active": 
    fig.add_trace(go.Bar(
        x=grouped_df['WHO Region'],
        y=grouped_df['Active'],
        name='Active',
        marker_color='orange'
    ))
    title = 'Active COVID-19 Cases by WHO Region'
elif selected == "Map":
    latest_date = df['Date'].max()
    latest_df = df[df['Date'] == latest_date]
    
    fig = px.scatter_geo(latest_df,
                         lat='Lat',
                         lon='Long',
                         hover_name='Country/Region',
                         hover_data={'Confirmed': True, 'Deaths': True, 'Recovered': True, 'Active': True, 'WHO Region': True},
                         size='Confirmed',
                         color='WHO Region',
                         title='Global COVID-19 Map (Latest Data)',
                         template='plotly_white')
    
    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type='equirectangular'
        ),
    )
else:
    for attribute in ['Confirmed', 'Deaths', 'Recovered', 'Active']:
        fig.add_trace(go.Bar(
            x=grouped_df['WHO Region'],
            y=grouped_df[attribute],
            name=attribute
        ))
        title = 'COVID-19 Cases by WHO Region'

# Customize layout
if selected != "Map":
    fig.update_layout(
        title=title,
        xaxis=dict(title='WHO Region'),
        yaxis=dict(title='Count'),
        barmode='group',
        legend=dict(title='Category'),
        template='plotly_white'
    )

# Display plot in Streamlit
st.plotly_chart(fig)
