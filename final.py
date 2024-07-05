import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from streamlit_option_menu import option_menu
import warnings
warnings.filterwarnings("ignore")



# to load global csv files
def load_global_data():
    df_real_world = pd.read_csv("real_world.csv")
    df_day_wise = pd.read_csv('day_wise.csv')
    df_covid_clean = pd.read_csv('covid_19_clean_complete.csv')
    return df_real_world, df_day_wise, df_covid_clean

# to load indian csv file
def load_india_data():
    df_india = pd.read_csv("Latest Covid-19 India Status.csv")
    df_india = df_india.replace('Dadra and Nagar Haveli and Daman and Diu', 'Daman and Diu')
    return df_india

# Load additional datasets
def load_additional_data():
    dataset1 = pd.read_csv("covid.csv")
    dataset2 = pd.read_csv("covid_grouped.csv")
    return dataset1, dataset2


# global section
def global_section():
    df_real_world, df_day_wise, df_covid_clean = load_global_data()
    dataset1, dataset2 = load_additional_data()

    # Sidebar for navigation
    with st.sidebar:
        selected = option_menu(
            "Menu",
            ["Continent and Country Selection", "Statistics Over Time", "WHO Region Statistics"],
            icons=["globe", "graph-up", "bar-chart"],
            menu_icon="cast",
            default_index=0,
        )

    # Section 1: Continent and Country Selection
     

    if selected == "Continent and Country Selection":
        df_real_world['Continent'] = df_real_world['Continent'].astype("str")


        # Drop duplicates for unique selections
        continent_select = df_real_world['Continent'].drop_duplicates().tolist()

        # Sidebar for continent selection
        continent_sidebar = st.sidebar.selectbox('Select a continent:', ['None'] + sorted(continent_select), index=2)

        # Initialize country_sidebar to None
        country_sidebar = None

        # If a continent is selected (not None)
        if continent_sidebar != 'None':
            # Filter dataframe based on selected continent
            df1 = df_real_world.loc[df_real_world['Continent'] == continent_sidebar]
            # Get the country column from the filtered dataframe
            df2 = df1['Country/Region']
            # Show country selection in the sidebar
            country_sidebar = st.sidebar.multiselect('Select countries:', sorted(df2), default='India')

        # Display selected values    
        col1,col2=st.columns(2)
        with col1:st.subheader(f"Selected Continent: {continent_sidebar}")
        with col2: st.subheader(f"Selected Countries: {country_sidebar}")

        # Sidebar for additional visualizations
        viz_option = st.sidebar.selectbox(
            'Select a visualization',
            [
                'None',
                'Bar Chart: Total Cases by Country',
                'Scatter Plot: Total Cases by Continent',
                'Scatter Plot: Total Tests by Continent (Log Scale)',
                'Scatter Plot: Total Cases by Country (Log Scale)',
                'Scatter Plot: Total Deaths by Country',
                'Scatter Plot: Tests per 1M pop by Country',
                'Scatter Plot: Total Cases vs Total Deaths (Log Scale)',
                'Choropleth Map: Confirmed Cases'
            ]
        )
        
        # If countries are selected
        if country_sidebar:
            # Filter dataframe based on selected countries
            country_data = df_real_world.loc[df_real_world['Country/Region'].isin(country_sidebar)]

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
                colors = plt.cm.Paired(range(len(labels)))   # Assign colors from the Paired colormap
                wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
                ax.axis('equal')    # Equal aspect ratio ensures that pie is drawn as a circle.
                for text in texts + autotexts:
                    text.set_fontsize(12)
                    text.set_color('black')
                st.pyplot(fig)

        # Display additional visualizations
        if viz_option != 'None':
            if viz_option == 'Bar Chart: Total Cases by Country':
                fig1 = px.bar(dataset1.head(15), x='Country/Region', y='TotalCases', color='TotalDeaths', height=500, hover_data=['Country/Region', 'Continent'], color_continuous_scale='Plasma')
                st.plotly_chart(fig1)

            elif viz_option == 'Scatter Plot: Total Cases by Continent':
                fig2 = px.scatter(dataset1, x='Continent', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='TotalCases', size='TotalCases', size_max=80, color_continuous_scale='Viridis')
                st.plotly_chart(fig2)

            elif viz_option == 'Scatter Plot: Total Tests by Continent (Log Scale)':
                fig3 = px.scatter(dataset1.head(50), x='Continent', y='TotalTests', hover_data=['Country/Region', 'Continent'], color='TotalTests', size='TotalTests', size_max=80, log_y=True, color_continuous_scale='Plasma')
                st.plotly_chart(fig3)

            elif viz_option == 'Scatter Plot: Total Cases by Country (Log Scale)':
                fig4 = px.scatter(dataset1.head(30), x='Country/Region', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='TotalCases', size='TotalCases', size_max=80, log_y=True, color_continuous_scale='Plasma')
                st.plotly_chart(fig4)

            elif viz_option == 'Scatter Plot: Total Deaths by Country':
                fig5 = px.scatter(dataset1.head(10), x='Country/Region', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='TotalDeaths', size='TotalDeaths', size_max=80, color_continuous_scale='Viridis')
                st.plotly_chart(fig5)

            elif viz_option == 'Scatter Plot: Tests per 1M pop by Country':
                fig6 = px.scatter(dataset1.head(30), x='Country/Region', y='Tests/1M pop', hover_data=['Country/Region', 'Continent'], color='Tests/1M pop', size='Tests/1M pop', size_max=80, color_continuous_scale='Plasma')
                st.plotly_chart(fig6)

            elif viz_option == 'Scatter Plot: Total Cases vs Total Deaths (Log Scale)':
                fig7 = px.scatter(dataset1.head(30), x='TotalCases', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='TotalDeaths', size='TotalDeaths', size_max=80, log_x=True, log_y=True, color_continuous_scale='Viridis')
                st.plotly_chart(fig7)

            elif viz_option == 'Choropleth Map: Confirmed Cases':
                fig8 = px.choropleth(dataset2, locations="iso_alpha", color="Confirmed", hover_name="Country/Region", color_continuous_scale="Viridis", animation_frame="Date")
                st.plotly_chart(fig8)

                 
    
    # Section 2: COVID-19 Statistics Over Time
    elif selected == "Statistics Over Time":

        # Convert 'Date' column to datetime
        df_day_wise['Date'] = pd.to_datetime(df_day_wise['Date'])

        # Set up Streamlit app
        st.title('COVID-19 Statistics Over Time')

        # Ensure min_date and max_date are datetime.date objects
        min_date = df_day_wise['Date'].min().date()
        max_date = df_day_wise['Date'].max().date()
        st.write(f"Data available from {min_date} to {max_date}")

        # Create a sidebar option menu
        view_options = ['Line Plot', 'Bar Plot', 'Pie Chart']
        selected_view = st.sidebar.radio('Select view:', view_options)

        # Create a date range slider
        start_date, end_date = st.sidebar.slider('Select date range:', min_value=min_date, max_value=max_date, value=(min_date, max_date))
        
        # Filter data based on the selected date range
        filtered_df = df_day_wise[(df_day_wise['Date'] >= pd.to_datetime(start_date)) & (df_day_wise['Date'] <= pd.to_datetime(end_date))]
        
        # Create a Plotly figure based on the selected view
        if selected_view == 'Line Plot':
            fig = go.Figure()

            # List of attributes to plot
            attributes = ['Confirmed', 'Deaths', 'Recovered', 'Active', 'New cases', 'New deaths', 'New recovered', 
                          'Deaths / 100 Cases', 'Recovered / 100 Cases', 'Deaths / 100 Recovered', 'No. of countries']
            
            # Add traces for each attribute
            for attribute in attributes:
                fig.add_trace(go.Scatter(
                    x=filtered_df['Date'],
                    y=filtered_df[attribute],
                    mode='lines',
                    name=attribute
                ))

            # Customize layout    
            fig.update_layout(
                title='COVID-19 Statistics Over Time',
                xaxis_title='Date',
                yaxis_title='Count / Rate',
                legend_title='Attributes',
                template='plotly_white'
            )

        # create a bar plot
        elif selected_view == 'Bar Plot':
            fig = go.Figure()

            # Add traces for each attribute
            for attribute in ['Confirmed', 'Deaths', 'Recovered', 'Active']:
                fig.add_trace(go.Bar(
                    x=filtered_df['Date'],
                    y=filtered_df[attribute],
                    name=attribute
                ))

            # Customize layout
            fig.update_layout(
                title='COVID-19 Statistics Over Time',
                xaxis_title='Date',
                yaxis_title='Count',
                legend_title='Attributes',
                template='plotly_white'
            )

        # Create a pie chart for the latest date    
        elif selected_view == 'Pie Chart':
            latest_date = filtered_df['Date'].max()
            latest_data = filtered_df[filtered_df['Date'] == latest_date][['Confirmed', 'Deaths', 'Recovered', 'Active']].iloc[0]
            fig = go.Figure(data=[go.Pie(labels=list(latest_data.index), values=list(latest_data.values))])
            fig.update_layout(
                title=f"COVID-19 Statistics on {latest_date.date()}",
                template='plotly_white'
            )

        # Display plot in Streamlit    
        st.plotly_chart(fig, use_container_width=True)
    
    # Section 3: COVID-19 Statistics by WHO Region
    elif selected == "WHO Region Statistics":

        # Convert Date column to datetime
        df_covid_clean['Date'] = pd.to_datetime(df_covid_clean['Date'])

        # Set up Streamlit app
        st.title('COVID-19 Statistics by WHO Region')

        # Sidebar for navigation
        with st.sidebar:
            selected_region = option_menu(
                "",
                ["Confirmed Cases", "Deaths", "Recovered", "Active", "Aggregate", "Map"],
                icons=["bar-chart-line", "bar-chart-line", "bar-chart-line", "bar-chart-line", "bar-chart-line", "map"],
                menu_icon="cast",
                default_index=0,
        )
            
        # Group data by WHO Region and aggregate required attributes    
        grouped_df = df_covid_clean.groupby('WHO Region').agg({
            'Confirmed': 'sum',
            'Deaths': 'sum',
            'Recovered': 'sum',
            'Active': 'sum'
        }).reset_index()

        # Create a bar chart using Plotly
        fig = go.Figure()

        # Determine which data to show based on the selection
        if selected_region == "Confirmed Cases":
            fig.add_trace(go.Bar(
                x=grouped_df['WHO Region'],
                y=grouped_df['Confirmed'],
                name='Confirmed',
                marker_color='blue'
            ))
            title = 'Confirmed COVID-19 Cases by WHO Region'
        elif selected_region == "Deaths":
            fig.add_trace(go.Bar(
                x=grouped_df['WHO Region'],
                y=grouped_df['Deaths'],
                name='Deaths',
                marker_color='red'
            ))
            title = 'COVID-19 Deaths by WHO Region'
        elif selected_region == "Recovered":
            fig.add_trace(go.Bar(
                x=grouped_df['WHO Region'],
                y=grouped_df['Recovered'],
                name='Recovered',
                marker_color='green'
            ))
            title = 'Recovered COVID-19 Cases by WHO Region'
        elif selected_region == "Active": 
            fig.add_trace(go.Bar(
                x=grouped_df['WHO Region'],
                y=grouped_df['Active'],
                name='Active',
                marker_color='orange'
            ))
            title = 'Active COVID-19 Cases by WHO Region'
        elif selected_region == "Map":
            latest_date = df_covid_clean['Date'].max()
            latest_df = df_covid_clean[df_covid_clean['Date'] == latest_date]
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
        if selected_region != "Map":
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

# India section
def india_section():
    df_india = load_india_data()
    
    # set up the streamlit app
    st.title("Covid-19 India Status Dashboard")
    
    # Sidebar for attribute selection
    with st.sidebar:
        selected_attr = option_menu(
            "Select Attribute",
            ["Total Cases","Deaths", "Discharged"],
            icons=["activity","skull", "heart"],
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
    
    size_attribute = {
    "Total Cases": "Total Cases",
    "Deaths": "Death Ratio",
    "Discharged": "Discharge Ratio"
     }

    # Function to create visualizations
    def create_visualizations(attribute, viz_type):
        if viz_type == "Map":
            fig = px.choropleth(
                df_india,
                geojson=geojson_url,
                featureidkey='properties.ST_NM',
                locations='State/UTs',
                color=attribute,
                color_continuous_scale='Blues' if attribute == 'Total Cases' else 'Reds' if attribute == 'Deaths' else 'Greens',
                title=f"Total Covid-19 {attribute} in India"
            )
            fig.update_geos(fitbounds="locations", visible=False)

        # create scatter plot    
        elif viz_type == "Scatter Plot":
            fig = px.scatter(
                df_india, 
                x='State/UTs', 
                y=attribute, 
                size=size_attribute[attribute], 
                color='State/UTs', 
                title=f"Total Covid-19 {attribute} Scatter Plot"
            )
        # create bar chart
        elif viz_type == "Bar Chart":
            fig = px.bar(
                df_india,
                x="State/UTs",
                y=attribute,
                color=attribute,
                color_continuous_scale='Blues' if attribute == 'Total Cases' else 'Reds' if attribute == 'Deaths' else 'Greens',
                title=f"Total Covid-19 {attribute} per State/UT",
                labels={"State/UTs": "State/UT", attribute: attribute}
            )
        st.plotly_chart(fig)
    
    # Display the visualizations based on selected attribute and visualization type
    create_visualizations(selected_attr, selected_viz)

# create the main function
def main():
    # Sidebar for main menu
    with st.sidebar:
        main_menu = option_menu(
            "Main Menu",
            ["Global", "India"],
            icons=["globe", "flag"],
            menu_icon="cast",
            default_index=0,
        )
    
    if main_menu == "Global":
        global_section()
    elif main_menu == "India":
        india_section()

if __name__ == "__main__":
    main()

