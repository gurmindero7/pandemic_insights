# Necessary Importing
# import pandas as pd
# import plotly.express as px
# #Importing dataset as pandas dataframe
# datasets = pd.read_csv('unified_.csv')
# # Creating and visualizing a scatter plot on Mapbox
# fig = px.scatter_mapbox(datasets, lat="Lat", lon="Long",
#                   color="Confirmed", size="Confirmed",
#                   color_continuous_scale=px.colors.cyclical.IceFire,
#                   size_max=70, zoom=0.75, hover_name='Country', 
#                   hover_data = ['Confirmed', 'Deaths', 'Recovery'], 
#                   title = 'Accumulative COVID-19 Confirmed Cases till 17 June, 2020')
# fig.show()


# fig = px.scatter_mapbox(datasets, lat="Lat", lon="Long",
#             animation_frame = 'Date', animation_group = 'Country', 
#             color="Confirmed", size="Confirmed",
#             color_continuous_scale=px.colors.cyclical.IceFire, 
#             size_max=70, zoom=0.75, hover_name='Country', 
#             hover_data = ['Confirmed', 'Deaths', 'Recovery'], 
#             title = 'Visualizing spread of COVID from 22/1/2020 to 17/6/2020')
# fig.show()

# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Load the CSV file
# uploaded_file = st.file_uploader("Choose a file", type="csv")
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)

#     # Process the DataFrame
#     df['Date'] = pd.to_datetime(df['Date'])
    
#     # Group by Date and Name of State/UT
#     grouped_df = df.groupby(['Date', 'Name of State / UT']).sum().reset_index()

#     # Plot the scatter plot on the Indian map
#     fig = px.scatter_mapbox(grouped_df,
#                          lat='Latitude',
#                          lon='Longitude',
#                          color='Total Confirmed cases',
#                          size='Total Confirmed cases',
#                          hover_name='Name of State / UT',
#                          hover_data={
#                              'Date': True,
#                              'Total Confirmed cases': True,
#                              'Death': True,
#                              'Cured/Discharged/Migrated': True,
#                              'New cases': True,
#                              'New deaths': True,
#                              'New recovered': True
#                          },
#                         #  animation_frame='Date',
#                          title='COVID-19 Spread in India',
#                          mapbox_style='carto-positron',
#                          zoom=3,
#                          center={'lat': 20.5937, 'lon': 78.9629})

#     fig.update_geos(fitbounds="locations", visible=False)
#     st.plotly_chart(fig)


# import warnings
# warnings.filterwarnings('ignore')
# import pandas as pd
# import plotly.express as px
# import streamlit as st
# from streamlit_option_menu import option_menu


# df = pd.read_csv("Latest Covid-19 India Status.csv")
# df = df.replace('Dadra and Nagar Haveli and Daman and Diu', 'Daman and Diu')
# # view_options=['Total Cases']/
# selected = option_menu(
#         "Menu",
#         ["Total Cases", "Deaths", "Recovered"],
#         icons=["map",'map','map'],
#         orientation='horizontal',
#         menu_icon="cast",
#         default_index=0,
#     )
# if selected == 'Total Cases':
#     # col1, col2 = st.columns([6,5])
#     # with col1:
#         fig = px.choropleth(
#             df,
#             geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
#             featureidkey='properties.ST_NM',
#             locations='State/UTs',
#             color='Total Cases',
#             color_continuous_scale='Blues'
#         )

#         fig.update_geos(fitbounds="locations", visible=False)
#         st.plotly_chart(fig)
#     # with col2:
#         fig = px.bar(df, x="State/UTs", y="Total Cases", color="Death Ratio",title="Total Cases as per each State : ")
#         st.plotly_chart(fig)
# elif selected == 'Deaths':
#     fig = px.choropleth(
#         df,
#         geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
#         featureidkey='properties.ST_NM',
#         locations='State/UTs',
#         color='Deaths',
#         color_continuous_scale='mint'
#     )

#     fig.update_geos(fitbounds="locations", visible=False)
#     st.plotly_chart(fig)



# import warnings
# warnings.filterwarnings('ignore')
# import pandas as pd
# import plotly.express as px
# import streamlit as st
# from streamlit_option_menu import option_menu

# # Load the dataset
# df = pd.read_csv("Latest Covid-19 India Status.csv")
# df = df.replace('Dadra and Nagar Haveli and Daman and Diu', 'Daman and Diu')

# # Streamlit app title
# st.title("Covid-19 India Status Dashboard")

# # Option menu for attribute selection
# selected = option_menu(
#     "Menu",
#     ["Total Cases","Active","Deaths", "Discharged"],
#     icons=["activity","activity","activity", "activity"],
#     orientation='horizontal',
#     menu_icon="cast",
#     default_index=0,
# )

# # Create the choropleth map
# if selected == 'Total Cases':
#     fig = px.choropleth(
#         df,
#         geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
#         featureidkey='properties.ST_NM',
#         locations='State/UTs',
#         color='Total Cases',
#         color_continuous_scale='Blues',
#         title="Total Covid-19 Cases in India"
#     )
#     fig.update_geos(fitbounds="locations", visible=False)
#     st.plotly_chart(fig)
#     # create a scatter plot
#     fig = px.scatter(df, x = 'State/UTs', y='Total Cases',size='Total Cases' ,color = df['State/UTs'])
#     st.plotly_chart(fig)
#     # Create the bar chart
#     fig = px.bar(
#         df,
#         x="State/UTs",
#         y="Total Cases",
#         color="Total Cases",
#         color_continuous_scale='Blues',
#         title="Total Cases per State/UT",
#         labels={"State/UTs": "State/UT", "Total Cases": "Total Cases"},
#     )
#     st.plotly_chart(fig)

    
# elif selected == 'Active':
#     # Create the choropleth map for deaths
#     fig = px.choropleth(
#         df,
#         geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
#         featureidkey='properties.ST_NM',
#         locations='State/UTs',
#         color='Active',
#         color_continuous_scale='purples',
#         title="Total Covid-19 Active in India"
#     )
#     fig.update_geos(fitbounds="locations", visible=False)
#     st.plotly_chart(fig)
#     # create the scatter plot
#     fig = px.scatter(df, x = 'State/UTs', y='Active',size='Active Ratio' ,color = df['State/UTs'])
#     st.plotly_chart(fig)

#     # Create the bar chart for active
#     fig = px.bar(
#         df,
#         x="State/UTs",
#         y="Active",
#         color="Active",
#         color_continuous_scale='purples',
#         title="Active per State/UT",
#         labels={"State/UTs": "State/UT", "Active": "Active"},
#     )
#     st.plotly_chart(fig)

    
# elif selected == 'Deaths':
#     # Create the choropleth map for deaths
#     fig = px.choropleth(
#         df,
#         geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
#         featureidkey='properties.ST_NM',
#         locations='State/UTs',
#         color='Deaths',
#         color_continuous_scale='Reds',
#         title="Total Covid-19 Deaths in India"
#     )
#     fig.update_geos(fitbounds="locations", visible=False)
#     st.plotly_chart(fig)
    
#     fig = px.scatter(df, x = 'State/UTs', y='Deaths',size='Death Ratio' ,color = df['State/UTs'])
#     st.plotly_chart(fig)

#     # Create the bar chart for deaths
#     fig = px.bar(
#         df,
#         x="State/UTs",
#         y="Deaths",
#         color="Deaths",
#         color_continuous_scale='Reds',
#         title="Deaths per State/UT",
#         labels={"State/UTs": "State/UT", "Deaths": "Deaths"},
#     )
#     st.plotly_chart(fig)

# elif selected == 'Discharged':
#     # Create the choropleth map for recovered cases
#     fig = px.choropleth(
#         df,
#         geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
#         featureidkey='properties.ST_NM',
#         locations='State/UTs',
#         color='Discharged',
#         color_continuous_scale='Greens',
#         title="Total Recovered Cases in India"
#     )
#     fig.update_geos(fitbounds="locations", visible=False)
#     st.plotly_chart(fig)
#     fig = px.scatter(df, x = 'State/UTs', y='Discharged',size='Discharge Ratio' ,color = df['State/UTs'])
#     st.plotly_chart(fig)


#     # Create the bar chart for recovered cases
#     fig = px.bar(
#         df,
#         x="State/UTs",
#         y="Discharged",
#         color="Discharged",
#         color_continuous_scale='Greens',
#         title="Recovered Cases per State/UT",
#         labels={"State/UTs": "State/UT", "Discharged": "Recovered Cases"},
#     )
#     st.plotly_chart(fig)

# import warnings
# warnings.filterwarnings('ignore')
# import pandas as pd
# import plotly.express as px
# import streamlit as st
# from streamlit_option_menu import option_menu

# # Load the dataset
# df = pd.read_csv("Latest Covid-19 India Status.csv")
# df = df.replace('Dadra and Nagar Haveli and Daman and Diu', 'Daman and Diu')

# # Streamlit app title
# st.title("Covid-19 India Status Dashboard")

# # Sidebar for attribute selection
# with st.sidebar:
#     selected_attr = option_menu(
#         "Select Attribute",
#         ["Total Cases", "Deaths", "Discharged"],
#         icons=["activity", "alert-circle", "heart"],
#         menu_icon="cast",
#         default_index=0,
#     )

# # Sidebar for visualization type selection
# with st.sidebar:
#     selected_viz = option_menu(
#         "Select Visualization",
#         ["Map", "Scatter Plot", "Bar Chart"],
#         icons=["map", "scatter-plot", "bar-chart"],
#         menu_icon="eye",
#         default_index=0,
#     )

# # URL for the geojson file
# geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"

# # Function to create visualizations
# def create_visualizations(attribute, viz_type):
#     if viz_type == "Map":
#         fig = px.choropleth(
#             df,
#             geojson=geojson_url,
#             featureidkey='properties.ST_NM',
#             locations='State/UTs',
#             color=attribute,
#             color_continuous_scale='Blues' if attribute == 'Total Cases' else 'Reds' if attribute == 'Deaths' else 'Greens',
#             title=f"Total Covid-19 {attribute} in India"
#         )
#         fig.update_geos(fitbounds="locations", visible=False)
#     # create scatter plot
#     elif viz_type == "Scatter Plot":
#         fig = px.scatter(df, x='State/UTs', y=attribute, size=attribute, color='State/UTs', title=f"Total Covid-19 {attribute} Scatter Plot")
#     # create bar chart
#     elif viz_type == "Bar Chart":
#         fig = px.bar(
#             df,
#             x="State/UTs",
#             y=attribute,
#             color=attribute,
#             color_continuous_scale='Blues' if attribute == 'Total Cases' else 'Reds' if attribute == 'Deaths' else 'Greens',
#             title=f"Total Covid-19 {attribute} per State/UT",
#             labels={"State/UTs": "State/UT", attribute: attribute}
#         )
#     st.plotly_chart(fig)

# # Display the visualizations based on selected attribute and visualization type
# create_visualizations(selected_attr, selected_viz)
# print(__name__)


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu

# Load the dataset
df = pd.read_csv("Latest Covid-19 India Status.csv")
df = df.replace('Dadra and Nagar Haveli and Daman and Diu', 'Daman and Diu')

# Streamlit app title
st.title("Covid-19 India Status Dashboard")

# Sidebar for attribute selection
with st.sidebar:
    selected_attr = option_menu(
        "Select Attribute",
        ["Total Cases", "Active", "Deaths", "Discharged"],
        icons=["activity", "alert-circle", "skull", "heart"],
        menu_icon="cast",
        default_index=0,
    )

# Sidebar for visualization type selection
with st.sidebar:
    selected_viz = option_menu(
        "Select Visualization",
        ["Map", "Scatter Plot", "Bar Chart"],
        icons=["map", "scatter-plot", "bar-chart"],
        menu_icon="eye",
        default_index=0,
    )

# URL for the geojson file
geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"

# Determine the size attribute for the scatter plot
size_attribute = {
    "Total Cases": "Total Cases",
    "Active": "Active Ratio",
    "Deaths": "Death Ratio",
    "Discharged": "Discharge Ratio"
}

# Function to create visualizations
def create_visualizations(attribute, viz_type):
    if viz_type == "Map":
        fig = px.choropleth(
            df,
            geojson=geojson_url,
            featureidkey='properties.ST_NM',
            locations='State/UTs',
            color=attribute,
            color_continuous_scale='Blues' if attribute == 'Total Cases' else 'Reds' if attribute == 'Deaths' else 'Greens' if attribute == 'Discharged' else 'Purples',
            title=f"Total Covid-19 {attribute} in India"
        )
        fig.update_geos(fitbounds="locations", visible=False)
    elif viz_type == "Scatter Plot":
        fig = px.scatter(
            df, 
            x='State/UTs', 
            y=attribute, 
            size=size_attribute[attribute], 
            color='State/UTs', 
            title=f"Total Covid-19 {attribute} Scatter Plot"
        )
    elif viz_type == "Bar Chart":
        fig = px.bar(
            df,
            x="State/UTs",
            y=attribute,
            color=attribute,
            color_continuous_scale='Blues' if attribute == 'Total Cases' else 'Reds' if attribute == 'Deaths' else 'Greens' if attribute == 'Discharged' else 'Purples',
            title=f"Total Covid-19 {attribute} per State/UT",
            labels={"State/UTs": "State/UT", attribute: attribute}
        )
    st.plotly_chart(fig)

# Display the visualizations based on selected attribute and visualization type
create_visualizations(selected_attr, selected_viz)


