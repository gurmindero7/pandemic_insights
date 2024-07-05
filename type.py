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
            icons=["globe", "line-chart", "bar-chart"],
            menu_icon="cast",
            default_index=0,
        )

    # Section 1: Continent and Country Selection
    if selected == "Continent and Country Selection":
        df_real_world['Continent'] = df_real_world['Continent'].astype("str")

        # Drop duplicates for unique selections
        continent_select = df_real_world['Continent'].drop_duplicates().tolist()

        # Sidebar for continent selection
        continent_sidebar = st.sidebar.selectbox('Select a continent:', ['None'] + sorted(continent_select))

        # Initialize country_sidebar to None
        country_sidebar = None

        # If a continent is selected (not None)
        if continent_sidebar != 'None':
            # Filter dataframe based on selected continent
            df1 = df_real_world.loc[df_real_world['Continent'] == continent_sidebar]
            # Get the country column from the filtered dataframe
            df2 = df1['Country/Region']
            # Show country selection in the sidebar
            country_sidebar = st.sidebar.multiselect('Select countries:', sorted(df2))

        # Display selected values    
        st.write(f"Selected Continent: {continent_sidebar}")
        st.write(f"Selected Countries: {country_sidebar}")

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
        st.write(f"Date Range: {min_date} to {max_date}")

        # Date selection using slider
        date_range = st.slider('Select date range:', min_date, max_date, (min_date, max_date))
        start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])

        # Filter data for the selected date range
        df_filtered = df_day_wise[(df_day_wise['Date'] >= start_date) & (df_day_wise['Date'] <= end_date)]

        st.write(f"Selected Date Range: {date_range[0]} to {date_range[1]}")

        st.write("### Daily Statistics")
        st.write(df_filtered)

        st.write("### Key Metrics Over Time")
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df_filtered['Date'], df_filtered['Confirmed'], label='Confirmed Cases')
        ax.plot(df_filtered['Date'], df_filtered['Deaths'], label='Deaths')
        ax.plot(df_filtered['Date'], df_filtered['Recovered'], label='Recovered')
        ax.set_xlabel('Date')
        ax.set_ylabel('Number of Cases')
        ax.set_title('COVID-19 Key Metrics Over Time')
        ax.legend()
        st.pyplot(fig)

    # Section 3: WHO Region Statistics
    elif selected == "WHO Region Statistics":
        st.write("WHO Region Statistics (under development)")

# india section
def india_section():
    df_india = load_india_data()
    st.title("COVID-19 India Status")
    st.dataframe(df_india)

    st.write("### Key Metrics")
    total_cases = df_india['Total Cases'].sum()
    total_deaths = df_india['Death'].sum()
    total_recovered = df_india['Discharged'].sum()
    active_cases = total_cases - (total_deaths + total_recovered)
    st.write(f"Total Cases in India: {total_cases}")
    st.write(f"Total Deaths in India: {total_deaths}")
    st.write(f"Total Recovered in India: {total_recovered}")
    st.write(f"Active Cases in India: {active_cases}")

    st.write("### State-wise Data")
    st.dataframe(df_india[['Name of State / UT', 'Total Cases', 'Death', 'Discharged', 'Active Ratio (%)', 'Death Ratio (%)', 'Discharge Ratio (%)']])

    st.write("### COVID-19 Cases Distribution in India")
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.pie([total_cases, total_deaths, total_recovered, active_cases], labels=['Total Cases', 'Deaths', 'Recovered', 'Active Cases'], autopct='%1.1f%%', startangle=90, colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'])
    ax.axis('equal')
    st.pyplot(fig)

# main function
def main():
    st.sidebar.title("COVID-19 Dashboard")
    option = st.sidebar.radio("Select a section", ("Global", "India"))

    if option == "Global":
        global_section()
    elif option == "India":
        india_section()

if __name__ == "__main__":
    main()