# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt 
# # Load data
# df = pd.read_csv("real_world.csv")

# df['Continent'] = df['Continent'].astype("str")
# # df['Country/Region'] = df['Country/Region'].astype("str")
# # Drop duplicates for unique selections
# continent_select = df['Continent'].drop_duplicates().tolist()

# # Sidebar for continent selection

# continent_sidebar = st.sidebar.selectbox('Select a continent:', ['None'] + sorted(continent_select))

# # Initialize country_sidebar to None
# country_sidebar = None

# # If a continent is selected (not None)
# if continent_sidebar != 'None':
#     # Filter dataframe based on selected continent
#     df1 = df.loc[df['Continent'] == continent_sidebar]
    
#     # Get the country column from the filtered dataframe
#     df2 = df1['Country/Region']
    
#     # Show country selection in the sidebar
#     country_sidebar = st.sidebar.selectbox('Select a country:',  sorted(df2))

# # Display selected values
# st.write(f"Selected Continent: {continent_sidebar}")
# st.write(f"Selected Country: {country_sidebar}")

# # If a country is selected (not None)
# if country_sidebar and country_sidebar != 'None':
#     # Filter dataframe based on selected country
#     country_data = df.loc[df['Country/Region'] == country_sidebar]
    
#     # Display country-specific information
#     st.write(f"### COVID-19 Data for {country_sidebar}")
#     st.write(country_data[['Population', 'TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases', 
#                             'Tot Cases/1M pop', 'Deaths/1M pop', 
#                            'TotalTests', 'Tests/1M pop', 'WHO Region']])

# st.write("### COVID-19 Cases Distribution")
# labels = ['TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases', ]
# sizes = country_data[['TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases']].values[0]
    
# fig, ax = plt.subplots()
# ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# st.pyplot(fig)



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Load data
df = pd.read_csv("real_world.csv")

df['Continent'] = df['Continent'].astype("str")

# Drop duplicates for unique selections
continent_select = df['Continent'].drop_duplicates().tolist()

# Sidebar for continent selection
continent_sidebar = st.sidebar.selectbox('Select a continent:', ['None'] + sorted(continent_select))

# Initialize country_sidebar to None
country_sidebar = None

# If a continent is selected (not None)
if continent_sidebar != 'None':
    # Filter dataframe based on selected continent
    df1 = df.loc[df['Continent'] == continent_sidebar]
    # st.write(df1)
    # Get the country column from the filtered dataframe
    df2 = df1['Country/Region']
    # st.write(df2)
    
    # Show country selection in the sidebar
    country_sidebar = st.sidebar.multiselect('Select countries:',  sorted(df2))

# Display selected values
st.write(f"Selected Continent: {continent_sidebar}")
st.write(f"Selected Countries: {country_sidebar}")

# If countries are selected
if country_sidebar:
    # Filter dataframe based on selected countries
    country_data = df.loc[df['Country/Region'].isin(country_sidebar)]
    
    # Display country-specific information
    st.write("### COVID-19 Data for Selected Countries")
    st.dataframe(country_data[['Country/Region', 'Population', 'TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases', 
                              'Tot Cases/1M pop', 'Deaths/1M pop', 'TotalTests', 'Tests/1M pop', 'WHO Region']])

    st.write("### Key Metrics")
    for country in country_sidebar:
        country_specific_data = country_data.loc[country_data['Country/Region'] == country]
        st.write(f"#### {country}")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric(label="Total Cases", value=int(country_specific_data['TotalCases']))
        col2.metric(label="Total Deaths", value=int(country_specific_data['TotalDeaths']))
        col3.metric(label="Total Recovered", value=int(country_specific_data['TotalRecovered']))
        col4.metric(label="Active Cases", value=int(country_specific_data['ActiveCases']))

        st.write("### COVID-19 Cases Distribution")
        labels = ['TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases']
        sizes = country_specific_data[['TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases']].values[0]
        
        fig, ax = plt.subplots()
        colors = plt.cm.Paired(range(len(labels))) # Assign colors from the Paired colormap
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        for text in texts + autotexts:
            text.set_fontsize(12)
            text.set_color('black')
        
        st.pyplot(fig)

